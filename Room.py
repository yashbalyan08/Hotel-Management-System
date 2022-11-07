#SQL imported for the code to run

import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
if mydb.is_connected()==False:
    print("Databse is not connected...")
else:
    mycursor = mydb.cursor()

# Room



"------Insert Function------"

def room_insert():
    Room_No = int(input("Enter New room number: "))
    Room_type = input("Enter the room type: ")
    Room_Price = int(input("Enter the room price of the Room: "))
    Room_Status = input("Emter the room status(A for available and B for booked): ")
    Extra = input("Enter the Extra Value: ")
    values_to_be_inserted = (Room_No, Room_type, Room_Price, Room_Status, Extra)
    insert = "insert into room_info(Room_No, Room_type, Room_Price, Room_Status, Extra) values(%s,%s,%s,%s,%s)"
    mycursor.execute(insert,values_to_be_inserted)
    print(mycursor.rowcount,"Record inserted")
    mydb.commit()

"------Room Status Change Function-------"

def room_status_update():
    Room_Status = input("Update the Room Status to: ")
    Room_No = int(input("Enter the Room number whose status is to be updated: "))
    Change = "update room_info set Room_Status = '%s' where Room_No ='%s'"%(Room_Status,Room_No)
    mycursor.execute(Change)
    Modified_Row_Display = "select * from room_info where Room_No = '%s'"%(Room_No,)
    mycursor.execute(Modified_Row_Display)
    Room_Data = mycursor.fetchall()
    for row in Room_Data:
        print(row)
    mydb.commit()

"------Room delete Function-------"

def room_delete():
    Room_No = int(input("Enter the room number who's reocrd is to be deleted: "))
    delete = "delete from room_info where Room_No = '%s'"%(Room_No)
    mycursor.execute(delete)
    mydb.commit()

"------Room Edit Function-------"

def room_edit():
    input = int(input('''Select from the list
                                            1. To insert new room...
                                            2. To delete a room record...
                                            3. To update room status...
                                            :  '''))
    if input == 1:
        room_insert()
    elif input == 2:
        room_delete()
    elif input == 3:
        room_status_update()
    else:
        print("----Wrong input----")

"------Room Display by type Function-------"

def DBT():
    Room_Type = input('''Enter the type of room required: 
    S ==> Single...
    D ==> Deluxe...
    SD ==> Super Deluxe...
    :
    ''')
    if Room_Type.upper()=="S":
        display = "select *& from room_info where Room_Type = 'Single' and Room_Status = 'V' "
    elif Room_Type.upper()=="D":
        display = "select *& from room_info where Room_Type = 'Deluxe' and Room_Status = 'V' "
    elif Room_Type.upper()=="SD":
        display = "select *& from room_info where Room_Type = 'Super Deluxe' and Room_Status = 'V' "
    else:
        print("-----WRONG INPUT-----")
    Room_Data = mycursor.fetchall()
    for row in Room_Data:
        print(row)
    mydb.commit()

"------Display No Wise Function -----"

def DNW():
    mycursor.execute("selet * from room_info order by Room_No")
    Display_by_number = mycursor.fetchall()
    for row in Display_by_number:
        print(row)

"------Display all the vacant rooms Function-----"

def DV():
    mycursor.execute("select * from room_info where Room_Status = 'V'")
    Display_Vacant = mycursor.fetchall()
    for row in Display_Vacant:
        print(row

"------Display all the booked rooms Function-----"

def DB():
    mycursor.execute("select * from Room_info where Room_Status='B'")
    Diplayed_Vacant=mycursor.fetchall()
    for row in Diplayed_Vacant:
        print(row)

"------Display Function------"

def Display():
    input = int(input('''Select from the list
                                            1. To display Room Display by type...
                                            2. To display room number wise...
                                            3. To display all the vacant rooms...
                                            4. To display all the booked rooms...
                                            :  '''))
    if input == 1:
        DBT()
    elif input == 2:
        DNW()
    elif input == 3:
        DV()
    elif input == 4:
        DB()
    else:
        print("----Wrong input----")
