# Item Catalog (Computers Catalog App)
Item Catalog is **a web application** that has been developed using Python (Flask Framework) and sqlite to provide lists of computers' information within a variety of manufactorer comapnies as well as provide a user registration and authentication system using third-party (Google API). Registered users can post, edit and delete their own items using CRUD operations

## Installation
Pre-requested tools have to be installed orderly to run the project :
  - Download and Install Python 2.7.12 from [here](https://www.python.org/downloads/)
  - Install Linux-based virtual machine from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
  - Install vagrant Software from [here](https://www.vagrantup.com/downloads.html) - this software used to configure the VM and share files between the VN and the Host Computer  
  - Use Github to clone or download the Configuration folder for VM 
     ```
     $git clone  https://github.com/udacity/fullstack-nanodegree-vm.git
     ```
  - Start the VM using `vagrant up ` and `vagrant ssh` command in your command line 
  - Change the directory to `/vagrant`
  - Finally, change directory to the project's directory and run the application by following steps that mentiond in **Running the Computers Catalog App** section

## Running the Computers Catalog App
To Run the project in VM:
- Initialize the data base using `python database_setup.py`
- Full the data base with per_collected data using `python seeder.py`
- Run Falsk web server using `python application.py` 
- In Web Browser write http://localhost:8000 to reach to the application
- Note: 
    - To have ability to add categories and items, you have to login first
    - The reach Items interface (to see or manage items) you have to press on All Items links