"Pirate_Scheduler"
  
  is a scheduler I made for fun! You can store and search caller's names. It then scans the database for information that is important to the customer service rep.

Pirate Scheduler logs the dates of all communications as well as allows for setting callback times and can tell if the caller is a customer or not.


I would reccomend downloading MySQL workbench (GUI for database). Here is the link for MySQL Workbench ---> https://dev.mysql.com/downloads/workbench/
                               

Inside of your database, create two tables.

Table Name: customer_calls
Columns:    Customer_Name varchar(50) 
            Time_Of_Call datetime 
            Notes varchar(250) 
            Callback_time datetime 
            Callback_time_2 datetime 
            id int AI PK
            
Table 2 Name: order_info
Columns:      Order_ID int AI PK 
              Customer_Name varchar(45) 
              Notes varchar(250) 
              Customer_Paid float 
              Date_Of_Purchase datetime 
              Item_Purchased varchar(45) 
              Item_ID int
            
Here are sql queries to save you time:

CREATE TABLE schedules.customer_calls (
    Customer_Name varchar(50),
    Time_Of_Call datetime,
    Notes varchar(250),
    Callback_time datetime,
    Callback_time_2 datetime,
    id int AUTO_INCREMENT PRIMARY KEY
);


CREATE TABLE schedules.order_info (
    Order_ID int AUTO_INCREMENT PRIMARY KEY,
    Customer_Name varchar(45),
    Notes varchar(250),
    Customer_Paid float,
    Date_Of_Purchase datetime,
    Item_Purchased varchar(45),
    Item_ID int
);


Once you have your two tables created. 

Open   boringstuff.py   this file is where your database username,password, ip address, and schema (database's name) live.
if you use the sql queries noted above. Your schema's name will be "schedules".

You fill in your User_Name, Password, Schema.

After this you should be ready to run Scheduler.py (the GUI) and start making queries.
If you have issues with connecting to your database. Make sure you are hosting your
database on your local server, and check connection config settings @ the home screen
of MySQL workbench.

(picture to come soon)



Optional but also highly recommended: Create a virtual environment and pip install requirements.txt

Useful cmd lines: *OPEN CMD LINE*,
                  cd Desktop,
                  mkdir virtualenvs,
                  cd virtualenvs,
                  python -m venv Pirate_Scheduler_venv,
                  cd Pirate_Scheduler_venv,
                  cd scripts,
                  activate.bat, <--activates virtual environment),
                  mkdir programs,
                  cd programs,
                  
                  *Git_Hub Files should then be downloaded or copied into the new folder you created*
                  Once these files live in the folder called "programs". 
                  run the program by typing:  
                  
                  python schedule.py


Update:4/27/23
