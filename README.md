# E-Commerce-Nile-Website
Django Simple Multi-Vendor E-Commerce-Nile Website

# ABSTRACT

## if you like this project then ADD a STAR ⭐️ to this project 👆

The Multi-Vendor E-commerce Website Project using Python Django Framework and MySQL is a comprehensive web-based application designed to provide a platform for online marketplaces. 

The system features an intuitive user interface that allows vendors to easily create and manage their own online stores, add products, set prices, and fulfill orders. The system also provides customers with a seamless shopping experience, add items to their cart, and make purchases.

The project includes both a vendor panel and an admin panel. The vendor panel allows vendors to manage their store information, products, orders. On the other hand, the admin panel provides access to advanced features such as managing vendors, monitoring sales.

The use of Python Django Framework and MySQL makes the system highly scalable, efficient, and secure. The framework's built-in features such as authentication, security, and testing, coupled with the power of MySQL's database management system, make the system a robust and reliable choice for any e-commerce business.

In summary, the Multi-Vendor E-commerce Website Project using Python Django Framework and MySQL is a powerful and efficient platform for setting up and managing an online marketplace with multiple vendors. The system's intuitive user interface, comprehensive functionality, and advanced features make it an ideal choice for businesses that want to launch and grow their own online marketplace. 
 
# Features of this Project

### A. Admin Users Can

1.Manage Category (Add, Update, Filter and Delete) 

2.Manage Products (Add, Update, Filter and Delete)

3.Manage Users (Update, Filter and Delete)

4.Manage Orders (View and Process)

### B. Vendors Can

1.Add Products

2.Update Profile

3.Get Orders and Manage Them

### C. Users Can Can

1.Add to Cart

2.Pay with Debit/Credit Card and Order

3.While Checkout, User should give the address to deliver

# How to Install and Run this project?
### Pre-Requisites:
Install Git Version Control [ https://git-scm.com/ ]

Install Python Latest Version [ https://www.python.org/downloads/ ]

Install Pip (Package Manager) [ https://pip.pypa.io/en/stable/installing/ ]

Install XAMPP Server[ https://www.apachefriends.org/download.html ]

Alternative to Pip is Homebrew

### Installation
1. Create a Folder where you want to save the project

2. Create a Virtual Environment and Activate

Install Virtual Environment First

    $  pip install virtualenv
   
Create Virtual Environment

3.Clone this project

    $  git clone https://github.com/Surendhar182/E-Commerce-Nile-Website.git
    
Then, Enter the project

4.Install Requirements from 'requirements.txt'

    $  pip install -r requirements.txt
 
5.Install mysqlclient in CM
 
    $  pip install mysqlclient
  
6.migrate the Database in CM
   
    $  python manage.py migrate  

7.Now Run Server

    $  python manage.py runserver
