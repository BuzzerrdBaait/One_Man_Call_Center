import mysql
from mysql.connector.errors import Error
import time                         
import datetime
import random
import webbrowser
from boringstuff import dbname, host, user, password

import mysql.connector
from mysql.connector import errorcode


random_number = random.randint(1, 10)   #This is here for testing.

#                                   #Here is the instance of SQLDatabase
                                    #It is what connects us and validates
                                    #our credentials that get entered below.
class SQLDatabase:
    def __init__(self, dbname, host, user, password):       #creates and defines
        self.dbname = dbname                                #user info and admins
        self.host = host                                    #it to the db.
        self.user = user                                    
        self.password = password                            #Python classes are
                                                            #wonderful because
    def connect(self):                                      #we don't have to
        try:                                                #make repetetive code
            self.database = mysql.connector.connect(        #over and over again!
                host=self.host,                          
                user=self.user,
                passwd=self.password,
                database=self.dbname
            )
            print("Connected to database successfully!")
        except Error as e:
            print("Failed to connect to the database: {}".format(e))


    def query(self, query):
        cursor = self.database.cursor()
        try:
            cursor.execute(query)
            records = cursor.fetchall()
            
            return records
        except Error as e:
            print("Failed to query data: {}".format(e))

 
    def disconnect(self):
        if self.database.is_connected():
            self.database.close()
            print("MySQL connection is closed")



currenttable=[]                     # Instance to be used later
currenttable2=[]                    # his is an another instance that will be used later

                                    #Here is how you make a database call.
db = SQLDatabase(dbname, host, user, password)
db.connect()                    #We connect to the database before calling other functions so we can interate over the database.

colnames=[]
currentcolnames=[]
tableslist=[]
searchlist=[]
parentname=[]

data_to_be_inserted=[]






def writetofile(query):
    """
    Be sure to update your file path below.
    """
      #insert a file path here.
    with open("C://Users//User//Desktop//Data.txt", "a") as f:    #Its just nice to have
        f.write(query)                                         #a write to file.
        f.write('\n')                                          #incase I need to add
        f.close()                                              #functions it helps see
                                                               #the sql query.
def show_columns(item,query):
    response=db.query(query)
    newlist=[]                                # I has to create a newlist because db.query(query) 
    for item in response:                     # returns a set. It doesn't explicitly tell you it
        newlist.append(item)                  # but it does if you dive deep into the code. I started 
    for columnsname in newlist:               # sweating trying to figure out what was wrong! hahaha!
        colnames.append((columnsname[0]))     # So I have to take the set and append it to a list
                                              # Then print an item out of the list.
    return item,colnames, print(item,colnames)

def show_db():
    print("Here is a list of the tables in this database:\n                                            ----------------------------------\n")
    query=("SHOW TABLES;")            #Helpful for the programmer
    response=db.query(query)          # shows the tables available.
    numtables=(len(response))         #Eventually I want to incorporate this into the GUI
    tableslist=[]                     #<---Instance of tableslist. Its just easier to define in here to not mess anything up outside the statement.

    for item in response:              #Uses the list to iterate over our list.
        tableslist.append(item[0])     #We have to clean off the )'
        print(item[0])         
    
    search=input("choose a table to open")
    
    searchlist.append(search) #I wanted this to be scalable to allow multiple tables. It is possible but for this instance its purpose is to select one and only one table.

    for item in tableslist:
        if item == search:
            query=("SHOW COLUMNS FROM {}.{};").format(dbname,item)
            print(query)
            show_columns(item,query)
            break
        else:
            continue

    return 
#show_db()
#print(searchlist,colnames)
#table=searchlist[0]             

integertype=['int', 'INT','Int', 'integer']                  #These are here
strtype=['str','string', 'Str', 'STR', 'VARCHAR', 'varchar'] #to determine what kind of string types 
datetype=['Date','date', 'dates','time']                     #MySQLMachine is taking in BUT mostly
                                                             #they stay here incase I have to go back
                                                             #into the cmd line to troubleshoot.



def customquery(query):
    rsp= db.query(query)
    print(query)
    print(rsp)



def insert_into_table_w_a_list(dbname, currenttable, currentcolnames,data_to_be_inserted,):

    length=len(currentcolnames)                          
    datalength=len(data_to_be_inserted)                  #These print out helpful stats
    #print("length of datalength {}".format(datalength))  #for the programmer. They are useful   
    #print("length of current colnames {}".format(length))#because they determine how big of a 
    #print(datalength//length,"is this the one??")        #table you need.
    a=currenttable[0]
    #print(a)
    #print("inserting into ", #Here is the start of the query. think of it like a snowball that gets bigger. The query stacks and gets bigger because of formatting in python, this is easy to accomplish.
    query = ("INSERT INTO `{}`.`{}` (").format(dbname,a) #INSERT INTO 'DBNAME'.'TABLE_ECT.' ()
    print(currentcolnames)
    for item in currentcolnames:
        query += "`{}`,".format(item)         #INSERT INTO 'DBNAME'.'TABLE' + "(item),(item),(item),(ect..)"

    query = query[0:-1]                       #Had to strip away the comma.
    
    query += ") VALUES ("    #INSERT INTO 'DBNAME'.'TABLE'(item) + ) VALUES (       
    querystart=query
    print(datalength//length)

    for i in range(datalength//length):    
        row=data_to_be_inserted[:length]   #We have to know when to stop inserting into
        for item in row:                   #our database. So we do the math datalength//length
             query += "'{}',".format(item) # which the answer will be equivalent to the number
        query = query[0:-1]                #of columns in the database...So your query will match up :)
        query += ");"
        #writetofile(query)                #<--If you ever need to test your queries, this is a
        #print(query)                      # very good way. You copy and paste the query into MySQL 
        db.query(query)                    # or any SQL troubleshooter to determine what needs to be fixed.
        db.database.commit()               # A very common step to forget is the .commit() method. It always has to be applied.
        query=querystart
        data_to_be_inserted=data_to_be_inserted[length:]

    return()
        
def create_table_if_not_exists(data_to_be_inserted,currenttable,currentcolnames,parentname, rowlength):

    
    
    rowlength=int(rowlength)            # HERE WE GO!! I will eventually make this not neccessary. But It is the only necessary input and the rest are instances that have already been determined. Your row length is determined by the amounts of different information you need to gather.

    colnum=len(data_to_be_inserted[:rowlength])  #Beep boop beep boop, boring math just determining how many columns to insert. 
    #print(colnum, "good i think")
    colnames=[]                            
    query="SHOW TABLES;"            # We call this query because we need to figure out how many tables are currently in the db.
    list1=db.query(query)           # This is where I want to insert Chat GPT to read one row of information and create an informative name for. Maybe I will! do that! YEAH!

    numtables=(len(list1))

    name=data_to_be_inserted[0]
     
         
    table='{}_{}'.format(name,numtables)  # Table_(i).format(i) #I do not know why but I have to have numbtables in here. If I take it out it goes crazy!
                                          # I have tried to remove it but for some reason I have to have it
                                          # If I replace the end, _{}' with anything other than numtables
                                          # SQL queries will work for the first table, but not the second
                                          # at first I realized that I was calling the same table when searching 
                                          # but when a random number was inserted it still caused the same issue.
                                          # So I'm lost until I can figure out why. I'm stumped!

    query = "CREATE TABLE IF NOT EXISTS {} (".format(table)  #easy peasy insert right here
    currentcolnames.clear()       #Hey, do not delete this. Just please don't. 
    print("rowlength = ",rowlength)
    print("colnum= ",colnum)
    
    
    for i in range(colnum):
        print(currentcolnames)                                  #<Number of columsn to be created based off of a sample of what gets put in
        columname= '{}_{}'.format(parentname[i],i+1)       #'column_{i+1}
        colnames.append(columname)               # I could probably insert gpt here to to make it fully customized. Would pre pretty sweet.
                                                 #print(currentcolnames)
        currentcolnames.append(columname)        #We have to make a list here so we can iterate over it. 
        data_type = type(data_to_be_inserted[i])  #We have to determine what datatype we are receiving so we can 
        if data_type == str:                      #save time later by not having to change all of the column types.
                leng= len(data_to_be_inserted[i]) #Eventually I want to find the range of each column and use the highest number to make that the column length. It will have to be another day though! :)
    
                data_type=("VARCHAR({})".format(250))   
        elif data_type == int:
            data_type=("INT")
        elif data_type == float:
            data_type=("FLOAT")
        elif data_type == bool:
            print("BOOLEAN")
            ####                    <------I want to add datetime but the input will always be 
            ####                           a string because MySQL needs the input to be a string :'(  Idk boss.
            ###  
        elif data_type == datetime:        #This must have been my attempt to insert datetime. If I left it here, I'm sure it works still but It would be hard to read on a chart.
            data_type == ("DATETIME")                          
        query += "{} {},".format(columname, data_type)
    query = query[:-1]
    query += ");"
    
    db.query((query))
    print("Searched and sent to db  ", name)
    #writetofile(query)    Not neccessary but a good place to test code..      
    currenttable.append(table)


    return(currentcolnames)   


def delete_alldb():
    query=("SHOW TABLES;")
    tblist=(db.query(query))

    for table in tblist:
        table=str(table)
        table=table[2:-3]
        print(table)
        query=("DROP TABLE `{}`.`{}`;").format(dbname,table)
        db.query(query)
        res=("Deleted table--{}").format(table)
        print(res)
Textwidget=""

def show_tables():
    query=("SHOW TABLES;")
    response=db.query(query)
    tablesearch=[]
    for item in response:
        for tablesname in response:
            for tablename in tablesname:
                tablesearch.append(tablename)
    return(Textwidget.update(1.0,item))


def show_columns(tablesname):
    query=("DESCRIBE {}").format(tablesname)
    db.query(query)















