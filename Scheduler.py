import Database   #Database connects you you the database
from Database import db    #db allows queries like db.database.query(query)
import tkinter
from tkinter import ttk,OptionMenu,StringVar,Frame,Canvas,PhotoImage, Spinbox
import webbrowser
import datetime
import time
import re

root = tkinter.Tk()
tablesearch=[]

frame_string=("700x580")
root.geometry(frame_string)
root.title("Pirate Scheduler")

background_color="grey10"
labelbgcolor="gray70"
root.configure(bg = background_color)

icon="C:/Users/calca/Desktop/VENVS/Scheduler/Scheduler/Scripts/icon.ico"
root.iconbitmap(icon)


logo=PhotoImage("C:/Users/calca/Desktop/VENVS/Scheduler/Scheduler/Scripts/Logo.png")
#####################################################################################################   DATE MODULE to generate the next 30 days
factor=30
tday= datetime.date.today()
daylist=[]

for i in range(0,factor):
    print(tday)
    tdelta=datetime.timedelta(days=i)
    dayi=tday+tdelta
    dayi=str(dayi)
    daylist.append(dayi)
print(daylist)
##################################################################################################  USE DAYLIST TO GET THE NEXT 30 DAYS

labelwidths=15
entrywidth=30
number=80
padyinput=1

time1=[]
date1=[]
time2=[]
date2=[]
time_selections=[]

label_color_num_list=[]

label1= tkinter.Label(width=labelwidths,bg=labelbgcolor,fg='black',text="Callers_Name")


label2= tkinter.Label(width=labelwidths,bg= labelbgcolor,fg='black',text="Important_Notes")

label3= tkinter.Label(width=labelwidths,bg= labelbgcolor,fg='black',text="Notes_to_be_stored->")

label4= tkinter.Label(width=labelwidths,bg= labelbgcolor,fg='black',text="Set_call_back_time")

label5= tkinter.Label(width=labelwidths,bg= labelbgcolor,fg='black',text="Good callback times")


label6= tkinter.Label(width=labelwidths,bg= labelbgcolor,fg='black',text="Send_to_DB")

#Entries
entry1=tkinter.Entry(width=entrywidth, bg=labelbgcolor)
entry2=tkinter.Text(root, bg="grey80", fg="black", height=7, width=65)
entry3=tkinter.Text(root, bg="grey80", fg="black", height=7, width=65)

frame=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
frame4=Frame(root)

frame.config(bg=background_color)
frame2.config(bg=background_color)
frame3.config(bg=background_color)
frame4.config(bg=background_color)

def optionMenuSelected(value):
    time1.clear()
    print("selected",value, " @ timemenu1")
    time1.append(value)

def DateMenuSelected(value):
    date1.clear()
    print("selected",value, " @ datemenu1")                #  Hey! I know this is kind of ugly! I just really like having the menu selections near the menu creation 
    date1.append(value)                                    #  point in tkinter.

def optionMenuSelected2(value):
    time2.clear()
    print("selected",value, " @ timemenu2")
    time2.append(value)


def DateMenuSelected2(value):
    date2.clear()
    print("selected",value, " @ datemenu2")
    date2.append(value)
     
option = StringVar(frame,"Set Callback time")
option2=StringVar(frame2,"Set Callback date")
option3 = StringVar(frame3,"Set Callback time")
option4=StringVar(frame4,"Set Callback date")

callback_list=[]
options=['ASAP','ANY','8:00 AM','8:15 AM','8:30 AM','8:45 AM','9:00 AM','9:15 AM','9:30 AM','9:45 AM','10:00 AM','10:15 AM','10:30 AM','10:45 AM','11:00 AM','11:15 AM','11:30 AM','11:45 AM','Noon','12:15 PM','12:30 PM','12:45 PM','1:00 PM','1:15 PM','1:30 PM','1:45 PM','2:00 PM','2:15 PM','2:30 PM','2:45 PM','3:00 PM','3:15 PM','3:30 PM','3:45 PM','4:00 PM','4:15 PM','4:30 PM','4:45 PM','5:00 PM','5:15 PM','5:30 PM','5:45 PM','6:00 PM','6:15 PM','6:30 PM','6:45 PM','7:00 PM','7:15 PM','7:30 PM','7:45 PM','8:00 PM']
#entries
timemenu1 = OptionMenu(frame,option, *options, command=optionMenuSelected)
timemenu1.config(bg=labelbgcolor)
datemenu= OptionMenu(frame,option2, *daylist,command=DateMenuSelected )
datemenu.config(bg=labelbgcolor)
timemenu2 = OptionMenu(frame,option3, *options, command=optionMenuSelected2)
timemenu2.config(bg=labelbgcolor)
datemenu2= OptionMenu(frame,option4, *daylist,command=DateMenuSelected2 )
datemenu2.config(bg=labelbgcolor)

############ PUT THESE IN ANOTHER FILE WHEN DONE  ###########################################   Hahaha just seeing this! Not gonna happen!
def send_it():                                                                              #
    print("send it")                                                                        #
    custname=entry1.get()
    notes=entry3.get(1.0,'end')

    try:
        timea=time1[0]
        datea=date1[0]
        print("call",custname, "on" ,datea,"at ", timea)
        formatted_timea=datea," ",timea
    except:
        print("Missing a value in either time or date in set 1.")

    try:
        timeb=time2[0]
        dateb=date2[0]
        print("call",custname, "on" ,dateb,"at ", timeb)
    except:
        print("Missing a value in either time or date for selection set 2.")
    

    try:
        formatted_timea=datetime.datetime.strptime(timea, "%I:%M %p").strftime("%H:%M")
        time_1_selection=datea+" "+formatted_timea
        time_selections.append(time_1_selection)
    except:
        print("No time in first section")

    try:
        formatted_timeb=datetime.datetime.strptime(timeb, "%I:%M %p").strftime("%H:%M")
        time_2_selection=dateb+" "+formatted_timeb
        time_selections.append(time_2_selection)
    except:
        print("No time in second section")

    now=datetime.datetime.now()

    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

    formatted_date=str(formatted_date)

    #print(formatted_date)
    time_selections_len=len(time_selections)
    print(time_selections_len," times were selected for callback")

    if time_selections_len == 0:
        query="INSERT INTO `schedules`.`customer_calls` (Customer_Name,Notes,Time_Of_Call) VALUES ('{}','{}','{}');".format(custname,notes,formatted_date)
        response=db.query(query)
        db.database.commit()
        clear_all()
    elif time_selections_len == 1:
        query="INSERT INTO `schedules`.`customer_calls` (Customer_Name,Notes,Time_Of_Call,Callback_time) VALUES ('{}','{}','{}','{}');".format(custname,notes,formatted_date,time_1_selection)
        writetofile(query)
        response=db.query(query)
        db.database.commit()
        clear_all()  
    elif time_selections_len == 2:
        query="INSERT INTO `schedules`.`customer_calls` (Customer_Name,Notes,Time_Of_Call,Callback_time,Callback_time_2) VALUES ('{}','{}','{}','{}','{}');".format(custname,notes,formatted_date,time_1_selection,time_2_selection)
        response=db.query(query)
        db.database.commit()
        clear_all()
    else:
        print("Error, try again")
    time_selections.clear()    


def clear_all():
    print("clear button was pressed")
    entry1.delete(0,'end')
    entry2.delete(0.1,'end')
    entry3.delete(0.1,'end')
    time1.clear()
    time2.clear()
    date1.clear()
    date2.clear()
    option.set("Set Callback Time")
    option2.set("Set Callback Date")
    option3.set("Set Callback Time")
    option4.set("Set Callback Date")
  

#####################################################################################
entry4label=tkinter.Label(text='hello')

entry6=tkinter.Entry(width=entrywidth, bg=labelbgcolor)

#buttons
sendbutton=tkinter.Button(frame2,width=15, bg=labelbgcolor, text='Press to send it!',command=send_it)
clearbutton=tkinter.Button(frame2,width=15, bg=labelbgcolor, text='Press to clear all!',command=clear_all)

Tableinfo=[]

tableselection=[]
options = []

  
def writetofile(query):
    """
    be sure to update your filepath if you want to write queries to a file. This is super helpful for troubleshooting queries.
    """
      #insert a file path here.
    with open("C://Users//User1//Desktop//Data.txt", "a") as f:    #Its just nice to have
        f.write(query)                                         #a write to file.
        f.write('\n')                                         #incase I need to add
        f.close()                                              #functions it helps see
                                                               #the sql query.

#####################################################################################################Creates header photo
canvas = Canvas(root, width = 75, height = 180) 


img = PhotoImage(file = "C:/Users/calca/Desktop/VENVS/Scheduler/Scheduler/Scripts/Logo.gif")
 
canvas.create_image(100, 80,anchor="center", image = img) 
#######################################################################################################
temprow_list=[]

def row_factor(input):
    row=0
    row= row+input
    temprow_list.append(row)
    return(print(temprow_list))

row_factor(3)

rownum=temprow_list[0]
labelspacer=tkinter.Label(bg="#6F390A")

tempcolumn_list=[]

def column_factor(input):
    column=0
    column= column+input
    tempcolumn_list.append(column)
    return(print(tempcolumn_list))

column_factor(2)

columnnum=tempcolumn_list[0]

#placement of widgets starts here
canvas.grid(row=0,column=0, sticky="nsew", padx=0, pady=5, columnspan=2)
label1.grid(row=1, column=0, sticky="nsew", padx=20, pady=5)
label2.grid(row=2, column=0, sticky="nsew", padx=20, pady=25)
label3.grid(row=3, column=0, sticky="nsew", padx=20, pady=25)
label4.grid(row=4, column=0, sticky="nsew", padx=20, pady=5)

label6.grid(row=6, column=0, sticky="nsew", padx=20, pady=5)

entry1.grid(row=1, column=1, sticky="nsew", padx=5, pady=0)
entry2.grid(row=2, column=1, sticky="nsew", padx=5, pady=0)
entry3.grid(row=3, column=1, sticky="nsew", padx=5, pady=0)

frame.grid(row=4,column=1,sticky="nsew", padx=5,pady=0)
timemenu1.grid(row=4, column=1, sticky="nsew",padx=5)
datemenu.grid(row=4,column=2,sticky="nsew")
timemenu2.grid(row=5,column=1,sticky="nsew",padx=5)
datemenu2.grid(row=5,column=2,sticky="nsew")

frame2.grid(row=6, column=1,sticky="nsew",pady=5,padx=5)
sendbutton.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)
clearbutton.grid(row=6,column=2,sticky="nsew",pady=5)



##non tkinter functions below::
entry_list=[]
itemsbought=[]
templist=[]


def get_entry(event,entry):
     itemsbought.clear()
    
     entry_value = entry.get()
     entry2.delete(1.0,'end')
     entry3.delete(1.0,'end')

       
     #print(entry_value)

     query=("SELECT item_purchased, Customer_Paid,Date_Of_Purchase FROM schedules.order_info WHERE Customer_Name ='{}';").format(entry_value)
     query2=("SELECT * FROM schedules.customer_calls WHERE Customer_Name ='{}';").format(entry_value)

     try:
         print("trying num 2")
         response=db.query(query2)
         #print(response)
         if response[0][0]:
             for item in response:

                ins=("Customer name  :{}\nCalled on      : {}\nNotes          : {}\n").format(item[0],item[1],item[2])
                entry2.insert(1.0,ins)
         
     except:
         entry2.insert(1.0,"Caller has not called before.\n\n")


     try:
         response=db.query(query)
         #print(response)
         if response[0][0]:
             for item in response:
                 itemsbought.append(item[0])
                 formatthedate=str(item[2])

                 formatthedate=formatthedate[:10]

                 inser=("{} bought {} for ${} on {}           \n\n").format(entry_value,item[0],item[1],formatthedate)
                 print(inser)
                 entry2.insert(1.0,inser)
             print("worked")
     except:
         inser=("{} has no sales on record.    \n\n").format(entry_value)
         entry2.insert(1.0,inser)



entry1.bind("<Return>", lambda event, entry=entry1: get_entry(event,entry))     #<----entry button binded with entry


root.mainloop()
