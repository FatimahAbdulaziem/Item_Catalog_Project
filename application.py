from flask import Flask, render_template, request, redirect, url_for, flash,\
                  jsonify, make_response
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Company, Computers, User
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import random
import string
import httplib2
import json
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secret.json', 'r')
                       .read())['web']['client_id']
APPLICATION_NAME = "Item Catalog Application"

'#To solve thread problem we use "?check_same_thread=false" that has been'\
  'quote from https://uconnectsaudi.slack.com/messages/CCHEAJ877/details/'
engine = create_engine('sqlite:///ComputerCompanieswithusers.db?'
                       'check_same_thread=false')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
Session = DBSession()


'# Create anti-forgery state token to do the authentication and authorization'\
   'using google account'


@app.route('/login')
def showLogin():
    state = ''.join(
                   random.choice
                   (string.ascii_uppercase + string.digits)for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


'#GConnect -- Callback & Send one time code to server'


@app.route('/gconnect', methods=['POST'])
def gconnect():
    '#Validate state token'
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    '#Obtain authorization code (Take one time code)'
    code = request.data
    try:
        '# Upgrade the authorization code into a credentials object'
        oauth_flow = flow_from_clientsecrets('client_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps("Failed to upgrade the\
        authorization code"), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    '#Check that the access token is valid.'
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    '# If there was an error in the access token info, abort.'
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    '# Verify that the access token is used for the intended user.'
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    '# Verify that the access token is valid for this app.'
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response
    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
                                json.dumps
                                ("Current user is already connected."), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    '# Store the access token in the session for later use.'
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    '# Get user information'
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = answer.json()
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    userID = getUserID(login_session['email'])
    if userID:
        print "User is exist"
    else:
        userID = createUser(login_session)
        print "new user has been created"
    login_session['userid'] = userID
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;\
                          "-webkit-border-radius: 150px;"\
                          "-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


'# DISCONNECT - Revoke a current user"s token and reset their login_session'


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(
                                json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = ('https://accounts.google.com/o/oauth2/revoke?token=%s'
           % login_session['access_token'])
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        flash("you are Successfully logged out")
        return redirect(url_for('showCatalog'))
    else:
        flash("Failed to revoke token for you")
        return redirect(url_for('showCatalog'))


'# Show the categories of catalog'
'# add new category , edit and delete linkes will not appear to the user'\
   'unless he logged into the system '


@app.route('/')
@app.route('/computer_catalog')
def showCatalog():
    Categories = Session.query(Company).all()
    LastItemList = []
    for Category in Categories:
        '#func.max()has been getten from'\
         'https://docs.sqlalchemy.org/en/latest/orm/query.html'
        Item = (Session.query(Computers.name, func.max(Computers.id),
                Computers.company_id).filter_by(company_id=Category.id).one())
        LastItemList.append(Item)
    if 'username' not in login_session:
        Isloggedin = False
    else:
        Isloggedin = True
    return render_template('Catalog.html', Categories=Categories,
                           LastItemList=LastItemList, Isloggedin=Isloggedin)


'#Show Categories as a JSON'
   

@app.route('/computer_catalog/JSON')
def CategoriesJSON():
    Categories = Session.query(Company).all()
    return jsonify(Categories= [r.serialize for r in Categories])


'# Add New category to the catalog'


@app.route('/computer_catalog/new', methods=['GET', 'POST'])
def addNewCategory():
    if request.method == 'POST':
        if request.form['submit'] == 'Create':
            newCategory = Company(name=request.form['Company_name'],
                                  user_id=login_session['userid'])
            Session.add(newCategory)
            Session.commit()
            flash("New category has been added successfully")
            return redirect(url_for('showCatalog'))
        else:
            return redirect(url_for('showCatalog'))
    else:
        return render_template('newCategory.html')


'# Edit existing category (Company) from the catalog'
'# The user who add new category, he only can edit  that category'


@app.route('/computer_catalog/<int:category_id>/edit', methods=['GET', 'POST'])
def editCategory(category_id):
    Category = Session.query(Company).filter_by(id=category_id).one()
    if Category.user_id != login_session['userid']:
        flash("You are not authorized to edit the desired category")
        return redirect(url_for('showCatalog'))
    else:
        if request.method == 'POST':
            if request.form['submit'] == 'Edit':
                Category.name = request.form['Edited_Name']
                Session.add(Category)
                Session.commit()
                flash("Editing category has been completed successfully")
                return redirect(url_for('showCatalog'))
            else:
                return redirect(url_for('showCatalog'))
        else:
            return render_template('editCategory.html',
                                   category_id=category_id, Category=Category)


'#Delete existing category from the catalog'
'#The user who add the category, he only can delete that category'


@app.route('/computer_catalog/<int:category_id>/delete',
           methods=['GET', 'POST'])
def deleteCategory(category_id):
    Category = Session.query(Company).filter_by(id=category_id).one()
    if Category.user_id != login_session['userid']:
        flash("You are not authorized to delete the desired category")
        return redirect(url_for('showCatalog'))
    else:
        if request.method == 'POST':
            if request.form['submit'] == 'Delete':
                Session.delete(Category)
                Session.commit()
                flash("deleting category has been completed successfully")
                return redirect(url_for('showCatalog'))
            else:
                return redirect(url_for('showCatalog'))
        else:
            return render_template('deleteCategory.html',
                                   category_id=category_id, Category=Category)


'#Show Items for specific category'
'#add new item , edit and delete linkes will  appear only to'\
 'the categorys creater when he logged into the sytem'


@app.route('/computer_catalog/<int:category_id>/items')
def showCategoryItems(category_id):
    Category = Session.query(Company).filter_by(id=category_id).one()
    Items = Session.query(Computers).filter_by(company_id=category_id).all()
    Creator = getUserInfo(Category.user_id)
    print Creator.id
    '#Isloggedin used to save the status of login/logout button in HTML page'
    if 'username' not in login_session:
        Isloggedin = False
    else:
        Isloggedin = True
    '#IsCreator used to decide the user accessibility'\
        'to AddnewItem,Edit and Delete Linkes'
    if ('username' not in login_session or
            Creator.id != login_session['userid']):
        IsCreator = False
    else:
        IsCreator = True
    return render_template('CategoryItems.html', Items=Items,
                           Category=Category, Isloggedin=Isloggedin,
                           IsCreator=IsCreator)


'#Show Items for Specific Category as a JSON'


@app.route('/computer_catalog/<int:category_id>/items/JSON')
def CategoryItemsJSON(category_id):
    Category = Session.query(Company).filter_by(id=category_id).one()
    Items = Session.query(Computers).filter_by(company_id=category_id).all()
    Creator = getUserInfo(Category.user_id)
    return jsonify(Creator=Creator.serialize, Company=Category.serialize,
                   Company_Computers=[i.serialize for i in Items])


'#Show Specific Item details as a JSON'


@app.route('/computer_catalog/<int:category_id>/items/<int:item_id>/JSON')
def ItemJSON(category_id, item_id):
    Category = Session.query(Company).filter_by(id=category_id).one()
    Item = Session.query(Computers).filter_by(id=item_id,
                                              company_id=category_id).one()
    Creator = getUserInfo(Category.user_id)
    return jsonify(Creator=Creator.serialize, Company=Category.serialize,
                   Company_Computer=Item.serialize)


'# Add new Items for specific category'


@app.route('/computer_catalog/<int:category_id>/items/new',
           methods=['GET', 'POST'])
def addNewItem(category_id):
    Category = Session.query(Company).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['submit'] == 'Create':
            newItem = (Computers(name=request.form['Item_name'],
                                 computer_type=request.form['Computer_Type'],
                                 description=request.form['Description'],
                                 company_id=category_id,
                                 user_id=login_session['userid']))
            Session.add(newItem)
            Session.commit()
            flash("New item has been added successfully")
            return redirect(url_for('showCategoryItems',
                                    category_id=category_id))
        else:
            return redirect(url_for('showCategoryItems',
                                    category_id=category_id))
    else:
        return render_template('newCategoryItem.html', category_id=category_id,
                               Category=Category)


'# Edit an existing Item'


@app.route('/computer_catalog/<int:category_id>/items/<int:item_id>/edit',
           methods=['GET', 'POST'])
def editItem(category_id, item_id):
    Category = Session.query(Company).filter_by(id=category_id).one()
    Item = Session.query(Computers).filter_by(id=item_id,
                                              company_id=category_id).one()
    if request.method == 'POST':
        if request.form['submit'] == 'Edit':
            Item.name = request.form['Item_name']
            Item.computer_type = request.form['Computer_Type']
            Item.description = request.form['Description']
            Session.add(Item)
            Session.commit()
            flash("Editing item has been completed successfully")
            return redirect(url_for('showCategoryItems',
                                    category_id=category_id))
        else:
            return redirect(url_for('showCategoryItems',
                                    category_id=category_id))
    else:
        return render_template('editCategoryItem.html', Category=Category,
                               Item=Item)


'# Delete an existing Item'


@app.route('/computer_catalog/<int:category_id>/items/<int:item_id>/delete',
           methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    Category = Session.query(Company).filter_by(id=category_id).one()
    Item = Session.query(Computers).filter_by(id=item_id,
                                              company_id=category_id).one()
    if request.method == 'POST':
        if request.form['submit'] == 'Delete':
            Session.delete(Item)
            Session.commit()
            flash("Deleting item has been completed successfully")
            return redirect(url_for('showCategoryItems',
                            category_id=category_id))
        else:
            return redirect(url_for('showCategoryItems',
                                    category_id=category_id))
    else:
        return render_template('deleteCategoryItem.html', Category=Category,
                               Item=Item)


def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    Session.add(newUser)
    Session.commit()
    return newUser.id


def getUserInfo(user_id):
    user = Session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = Session.query(User).filter_by(email=email).one()
        return user.id
    except IndexError:
        return None


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
