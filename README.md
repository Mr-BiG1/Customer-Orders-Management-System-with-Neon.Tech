# Customer-Orders-Management-System-with-Neon.Tech
Customer Orders Management System with Neon.Tech Develop a simple Customer Orders Management System that connects to a Neon.Tech PostgreSQL database. This project covers the basics of connecting to Neon.Tech and implementing minimal Create and Read functionality for managing customer orders. using python 


# How to use 
Before running the main.py you have to install the required packages to run this application.

to install all the required packages run      `pip install -r requirements.txt` this will install all the packages need to run this app.
Once finished installing, run `python main.py` "make sure u are on root directory"


# Blueprint 
```
folder structure 
Customer Order Management System
|
|---app
|    |
|    ├───db # this contains all database related files/codes.
|    |    |
|    |    ├──connection.py
|    |    ├──order.py
|    |
|    ├───gui # you cab find all screen related files/code here.
|         |
|         ├──layout.py
|         ├──main_Window.py
|
|
├────.gitignore # instruction related to the git/version controlling, preventing form uploading sensitive information eg. db pass 
├────.env #contain sensitive information like password.
├────main.py # initial code 
├────requirements.txt # contains required packages 
├────README.md # contains information about the project 

```
# .env configuration 
create a file named .env and add these details form your neon tech web page 

DB_NAME=dbName
DB_USER=dbUserName
DB_PASSWORD=password
DB_HOST=ep-sparkling-dew-a4x74dcj-pooler.us-east-1.aws.neon.tech // 
DB_PORT=5432\
