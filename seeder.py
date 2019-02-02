from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Company, Computers, User

engine = create_engine('sqlite:///ComputerCompanieswithusers.db?'
                       'check_same_thread=false')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


'# Create a user : these data mentioned to real data of my email'
app_user = User(name="Faimah Al-Ibrahim",
                email="fatimah.abdulaziem.alibrahim@gmail.com",
                picture='https://lh4.googleusercontent.com/-hbKMNuV5Yd0/'
                        'AAAAAAAAAAI/AAAAAAAAAAA/wSm7wWWkl4g/photo.jpg')
session.add(app_user)
session.commit()


'# Add First Categoy (HP company) with its items'
appCategory1 = Company(name="Hewlett-Packard (HP)", user_id=1)
session.add(appCategory1)
session.commit()

'# Add First Item Computer to HP'
appc1Item1 = Computers(name="HP 14-bp101nx",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Core i5-8250U
Operating System: Windows 10 - 64 bit
RAM: 8 GB
Capacity: 1 TB
Processor Speed : 1.6 GHz
Connectivity Technology: WiFi/Bluetooth
Touch Display : No
Display Size: 14 inch
Color : white
Release Year : 2017
Price: 3780 SR in Jarir Bookstore"""),
                       computer_type="Laptop", company_id=1, user_id=1)
session.add(appc1Item1)
session.commit()

'# Add Second Item Computer to HP'
appc1Item2 = Computers(name="HP ENVY 13-ad105nx",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Core i5-8250U
Operating System: Windows 10 - 64 bit
RAM: 8 GB
Capacity: 256 GB PCIe NVMe M.2 SSD
Processor Speed : 1.8 GHz
Connectivity Technology    : WiFi/Bluetooth
Touch Display : No
Display Size: 13.3 inch
Color : Natural Silver
Release Year : 2017
Price: 3999 SR in Jarir Bookstore"""),
                       computer_type="Laptop", company_id=1, user_id=1)
session.add(appc1Item2)
session.commit()

'# Add third Item Computer to HP'
appc1Item3 = Computers(name="HP Pavilion 24-r013nx Desktop All-in-One",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Core i7-7700T
Operating System: Windows 10 - 64 bit
RAM: 16 GB
Capacity: 2 TB HDD
Processor Speed : 2.9 GHz
Connectivity Technology	: WiFi/Bluetooth
Touch Display : Yes
Display Size: 23.8 inch
Color : Blizzard White
Ports : HDMI/USB 2.0/USB 3.1/USB-C/RJ-45
Release Year : 2017
Price: 4719 SR in Jarir Bookstore """),
                       computer_type="Desktop Computer",
                       company_id=1, user_id=1)
session.add(appc1Item3)
session.commit()

'# Add fourth Item Computer to HP'
appc1Item4 = Computers(name="HP ENVY x2 12-g003nx",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Core i5-7Y54
Operating System: Windows 10
RAM: 8 GB
Capacity: 256 GB PCIe NVMe M.2 SSD
Processor Speed: 1.2 GHz
Connectivity Technology: WiFi/Bluetooth
Touch Display: Yes
Display Size: 12.3 inch
Color: Natural Silver
Renewed Grade: Renewed Grade B
Price: 5699 SR in Jarir Bookstore"""),
                       computer_type="2 in 1 Laptop", company_id=1, user_id=1)
session.add(appc1Item4)
session.commit()

'# Add fifth Item Computer to HP'
appc1Item5 = Computers(name="HP ENVY 27-b207nx Desktop All-in-One",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Core i7-8700T
Operating System: Windows 10 - 64 bit
RAM: 16 GB
Capacity: 512 GB PCIe NVMe M.2 SSD/1 TB
Processor Speed : 2.4 GHz
Connectivity Technology	: WiFi/Bluetooth
Touch Display : Yes
Display Size: 27 inch
Color : Ash Silver Sparkle
Ports : HDMI/USB 3.0/USB-C/RJ-45
Release Year : 2018
Price: 8749 SR in Jarir Bookstore """),
                       computer_type="Desktop Computer",
                       company_id=1, user_id=1)
session.add(appc1Item5)
session.commit()

'# Add Second Categoy (Apple company) with its items'
appCategory2 = Company(name="Apple", user_id=1)
session.add(appCategory2)
session.commit()

'# Add 1st Item Computer to Apple'
appc2Item1 = Computers(name="Apple iPad Pro 4G",
                       description=("""This Device has set of specifications:\n
Display Size: 12.9 inch
Color : Gold
Operating System: iOS 10 - 64 bit
Capacity: 256 GB (NAND Flash)
Camera Resolution: Rear: 12 MP/Front: 7 MP
SIM Type: Nano SIM
Number Of Sim Supported: 1 SIM
Calling Function: None
Release Year : (iPad Pro) 2nd Generation - 2017
Price: 3619 SR in Jarir Bookstore """),
                       computer_type="Tablet", company_id=2, user_id=1)
session.add(appc2Item1)
session.commit()

'# Add 2ed Item Computer to Apple'
appc2Item2 = Computers(name="Apple iMac Pro Desktop All-in-One",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Xeon W
Operating System: macOS High Sierra
RAM: 32 GB
Capacity: 1 TB SSD
Processor Speed : 3.2 GHz
Connectivity Technology	: WiFi/Bluetooth
Touch Display : No
Display Size: 27 inch
Color : Space Gray
Release Year : 2017
Price: 18999 SR in Jarir Bookstore """),
                       computer_type="Desktop Computer",
                       company_id=2, user_id=1)
session.add(appc2Item2)
session.commit()

'# Add 3rd Item Computer to Apple'
appc2Item3 = Computers(name="Apple MacBook Pro (Retina)",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Core i7 Quad Core
Operating System: macOS Sierra
RAM: 16 GB
Capacity: 256 GB SSD
Processor Speed : 2.2 GHz
Connectivity Technology	: WiFi/Bluetooth
Touch Display : No
Display Size: 15.4 inch
Color : Silver
Ports : HDMI/USB 3.0/Thunderbolt
Release Year : 2015
Price: 6999 SR in Jarir Bookstore """),
                       computer_type="Laptop", company_id=2, user_id=1)
session.add(appc2Item3)
session.commit()

'# Add third Categoy (Dell company) with its items'
appCategory3 = Company(name="Dell", user_id=1)
session.add(appCategory3)
session.commit()

'# Add 1st Item Computer to Dell'
appc3Item1 = Computers(name="Dell Inspiron 13 7000",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Core i7-8550U
Operating System: Windows 10
RAM: 16 GB
Capacity: 512 GB SSD
Processor Speed : 1.8 GHz
Connectivity Technology	: WiFi/Bluetooth
Touch Display : Yes
Display Size: 13.3 inch
Color : Grey
Ports : HDMI/USB 2.0/USB 3.0
Price: 5749 SR in Jarir Bookstore """),
                       computer_type="2 in 1 Laptop", company_id=3, user_id=1)
session.add(appc3Item1)
session.commit()

'# Add 2ed Item Computer to Dell'
appc3Item2 = Computers(name="Dell XPS 13",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Core i7-7500U
Operating System: Windows 10
RAM: 16 GB
Capacity: 1 TB SSD
Processor Speed: 2.7 GHz
Connectivity Technology: WiFi/Bluetooth
Touch Display : Yes
Display Size: 13.3 inch
Color : Silver
Ports : USB 3.0/Thunderbolt
Release Year : 2016
Renewed Grade : Renewed Grade B
Price: 7599 SR in Jarir Bookstore """),
                       computer_type="Laptop", company_id=3, user_id=1)
session.add(appc3Item2)
session.commit()

'# Add 3rd Item Computer to Dell'
appc3Item3 = Computers(name="Dell Inspiron 20 Desktop All-in-One",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Core i3-7100U
Operating System: Windows 10
RAM: 4 GB
Capacity: 1 TB HDD
Processor Speed : 2.4 GHz
Connectivity Technology: WiFi/Bluetooth
Touch Display : Yes
Display Size: 19.5 inch
Color : Black
Ports : HDMI/USB 2.0/USB 3.0/RJ-45
Release Year : 2016
Price: 2729 SR in Jarir Bookstore"""),
                       computer_type="Desktop Computer",
                       company_id=3, user_id=1)
session.add(appc3Item3)
session.commit()

'# Add fourth Categoy (Samsung company) with its items'
appCategory4 = Company(name="Samsung", user_id=1)
session.add(appCategory4)
session.commit()

'# Add 1st Item Computer to Samsung'
appc4Item1 = Computers(name="(Samsung) Galaxy 4G Tablet PC",
                       description=("""This Device has set of specifications:\n
Display Size: 10.5 inch
Operating System: Android v8.1(Oreo)-32bit
RAM: 4 GB RAM
Capacity: 64 GB (eMMC)
Camera Resolution: Rear: 13 MP/Front: 8 MP
SIM Type: Nano SIM
Number Of Sim Supported: 1 SIM
Calling Function: Yes
Release Year : 2018
Color : Gray
Price: 2799 SR in Jarir Bookstore"""),
                       computer_type="Tablet", company_id=4, user_id=1)
session.add(appc4Item1)
session.commit()

'# Add 2ed Item Computer to Samsung'
appc4Item2 = Computers(name="Samsung Galaxy Tab A 7.0 4G Tablet PC",
                       description=("""This Device has set of specifications:\n
Display Size: 7 inch
Operating System: Android v5.1 (Lollipop)
RAM: 1.5 GB RAM
Capacity: 8 GB (eMMC)
Processor Speed: 1.5  GHz
Camera Resolution: Rear: 5 MP/Front: 2 MP
SIM Type: Micro SIM
Number Of Sim Supported: 1 SIM
Calling Function: Yes
Release Year : 2016
Color : Black
Price: 499 SR in Jarir Bookstore"""),
                       computer_type="Tablet", company_id=4, user_id=1)
session.add(appc4Item2)
session.commit()

'# Add fifth Categoy (Lenovo company) with its items'
appCategory5 = Company(name="Lenovo", user_id=1)
session.add(appCategory5)
session.commit()

'# Add 1st Item Computer to Lenovo'
appc5Item1 = Computers(name="Lenovo YOGA Tab 3 10 (X50)",
                       description=("""This Device has set of specifications:\n
Display Size: 10.1 inch
Operating System: Android v5.1 (Lollipop)
RAM: 2 GB RAM
Capacity: 16 GB (eMMC)
Processor Speed: 1.3  GHz
Camera Resolution: Rear: 8 MP/Front: 8 MP
SIM Type: Micro SIM
Number Of Sim Supported: 1 SIM
Calling Function: Yes
Release Year : 2016
Color : Black
Price: 1049 SR in Jarir Bookstore"""),
                       computer_type="Tablet", company_id=5, user_id=1)
session.add(appc5Item1)
session.commit()

'# Add 2ed Item Computer to Lenovo'
appc5Item2 = Computers(name="Lenovo IdeaPad 720S-14",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Core i7-8550U
Operating System: Windows10
RAM: 8 GB RAM
Capacity: 512 GB (PCIe Flash)
Processor Speed: 1.8 GHz
Connectivity Technology: WiFi/Bluetooth
Touch Display : No
Display Size: 14 inch
Color : Silver
Ports : HDMI/USB 3.0/USB-C
Release Year : 2017
Price: 4129 SR in Jarir Bookstore"""),
                       computer_type="Laptop", company_id=5, user_id=1)
session.add(appc5Item2)
session.commit()

'# Add 3rd Item Computer to Lenovo'
appc5Item3 = Computers(name="Lenovo YOGA 920-13IKB",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Core i7-8550U
Operating System: Windows 10
RAM: 16 GB RAM
Capacity: 1 TB SSD
Processor Speed: 1.8 GHz
Connectivity Technology: WiFi/Bluetooth
Touch Display : Yes
Display Size: 13.9 inch
Color : Champagne Gold
Ports : USB 3.0/USB-C
Renewed Grade : Renewed Grade B
Price: 8599 SR in Jarir Bookstore"""),
                       computer_type="2 in 1 Laptop", company_id=5, user_id=1)
session.add(appc5Item3)
session.commit()

'# Add 4th Item Computer to Lenovo'
appc5Item4 = Computers(name="Lenovo IdeaCentre 520 Desktop All-in-One",
                       description=("""This Device has set of specifications:\n
Processor Type: Intel Core i7-8700T
Operating System: Windows10
RAM: 8 GB RAM
Capacity: 1 TB SSD
Processor Speed: 2.4 GHz
Connectivity Technology: WiFi/Bluetooth
Touch Display : Yes
Display Size: 23.8 inch
Color : Black
Ports : HDMI(In/Out)/USB 2.0/USB 3.1/RJ-45
Release Year : 2018
Price: 3899 SR in Jarir Bookstore"""),
                       computer_type="Desktop Computer",
                       company_id=5, user_id=1)
session.add(appc5Item4)
session.commit()

print "Categories have been added to the database"
