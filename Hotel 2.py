import random
import datetime
import time
from datetime import date

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root", passwd="MALLUSETHno.8", database="hotel")
if mydb.is_connected()==False:
    print("Database not Connected...")
mycursor = mydb.cursor()

'''ROOM'''

#Insert Function
def room_insert():
    Room_No=int(input("Enter New room number: "))
    Room_Type=input("Enter the room type: ")
    Room_Price=int(input("Enter the price of the Room: "))
    Room_Status=input("Enter the room Status: ")
    Extra=input("Enter The Extra Value: ")
    temp=(Room_No,Room_Type,Room_Price,Room_Status,Extra)
    insert='insert into Room_info(Room_No,Room_Type,Room_Price,Room_Status,Extra) values(%s,%s,%s,%s,%s)'
    mycursor.execute(insert,temp)
    print(mycursor.rowcount,"Record Inserted")
    mydb.commit()



#DisplayByType Function
def DBT():
    New_Room_Type=input('''Enter the type of room required:
                                                          S ==> Single
                                                          D ==> Deluxe
                                                          SD ==> Super Deluxe
                                                          : 
                                                              ''')
    if New_Room_Type.upper()=='S':    
        display="select * from Room_info where Room_Type = 'Single' and Room_Status='V'"
    elif New_Room_Type.upper()=='D':    
        display="select * from Room_info where Room_Type = 'Deluxe' and Room_Status='V'"
    elif New_Room_Type.upper()=='SD':    
        display="select * from Room_info where Room_Type = 'SuperDeluxe' and Room_Status='V'"
    mycursor.execute(display)
    Room_Data=mycursor.fetchall()
    for row in Room_Data:
        print(row)
    mydb.commit()


#Modify Function
def room_modify():
    Room_status=input("Update the Room status to:")
    Room_no=int(input("The Room's Status to be changed:"))
    Change="update Room_info set Room_Status= '%s' where Room_No= %s"%(Room_status,Room_no)
    mycursor.execute(Change)
    Modified_Row="select * from Room_info where Room_No = '%s' "%(Room_no,)
    mycursor.execute(Modified_Row)
    Room_Data=mycursor.fetchall()
    for row in Room_Data:
        print(row)
    mydb.commit()



#Delete Function
def room_delete():
    Room_no=int(input("Enter the Room Number who's record is to be deleted:"))
    delete="delete from Room_info where Room_No=%s"%(Room_no)
    mycursor.execute(delete)
    mydb.commit()



#DisplayNoWise Function
def DNW():
    mycursor.execute('select * from Room_info order by Room_No')
    Diplayed_by_Number=mycursor.fetchall()
    for row in Diplayed_by_Number:
        print(row)



#DisplayVacant Function
def DV():
    mycursor.execute("select * from Room_info where Room_Status='V'")
    Diplayed_Vacant=mycursor.fetchall()
    for row in Diplayed_Vacant:
        print(row)



#DisplayBooked Function
def DB():
    mycursor.execute("select * from Room_info where Room_Status='B'")
    Diplayed_Vacant=mycursor.fetchall()
    for row in Diplayed_Vacant:
        print(row)




'''Serial Number'''

#Function for serial number

#Booking_Serial_Number 1
#Extra 
#Food_id 2
#Food_Billing_SNo 3
#Billbook_SNo 4

def Sr_No(num):
    sql=''
    update=''
    New=0
    if num==1:
        sql='select Booking_Serial_Number from Sr_No'
        #update="update Sr_No set Booking_Serial_Number= %s "%(New,)
    elif num==2:
        sql='select Food_id from Sr_No'
        #update="update Sr_No set Food_id= %s "%(New,)
    elif num==3:
        sql='select Food_Billing_SNo from Sr_No'
        #update="update Sr_No set Food_Billing_SNo= %s "%(New,)
    elif num==4:
        sql='select Billbook_SNo from Sr_No'
        #update="update Sr_No set Billbook_SNo= %s "%(New,)
    else:
        print("ERROR ,Number not valid")
    for x in range(0,1):
        mycursor.execute(sql)
        l=mycursor.fetchall()
        #print(l)
        l1=l
        #print(l1)
        New=l1[0][0]+1
        #print(New)
        if num==1:
            #sql='select Booking_Serial_Number from Sr_No'
            update="update Sr_No set Booking_Serial_Number= %s "%(New,)
        elif num==2:
            #sql='select Food_id from Sr_No'
            update="update Sr_No set Food_id= %s "%(New,)
        elif num==3:
            #sql='select Food_Billing_SNo from Sr_No'
            update="update Sr_No set Food_Billing_SNo= %s "%(New,)
        elif num==4:
            #sql='select Billbook_SNo from Sr_No'
            update="update Sr_No set Billbook_SNo= %s "%(New,)
        else:
            print("ERROR ,Number not valid")
        #update="update Sr_No set Value= %s "%(New,)
        mycursor.execute(update)
        mydb.commit()
        print(mycursor.rowcount,"Record Changed")
        x+=1
        return New

#Booking_Serial_Number 1
#Extra 
#Food_id 2
#Food_Billing_SNo 3
#Billbook_SNo 4

'''Food'''

#Food Function For Food Table

def food_insert():
    F_id =Sr_No(2)
    print("Food id:",F_id)
    F_Name=input("Enter the food name: ")
    F_Type=input("Enter the Food Type B/L/D: ")
    Pices=int(input("Enter the number of pices with the entered Food item: "))
    Price=int(input("Enter the price of the Food: "))
    Status=input("Enter whether the food itme is available or not A/NA: ")
    Values=(F_id,F_Name,F_Type,Pices,Price,Status)
    print(Values)
    insert="insert into Food(Fid,F_Name,F_Type,Pices,Price,Status) values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(insert,Values)
    print(mycursor.rowcount,"Record Inserted")
    mydb.commit()


#Modify Function For Food Table

def food_modify():
    find=input("Enter the food id whom you would update details:")
    print(find)
    change=input("Enter the details you want to change:\n fname \n ftype \n price \n")
    if change=='fname':
        modify=input("update the food item you want to:")
        s="update food set F_Name=%s where fid=%s"
        x=(modify,find)
   
    elif change=='ftype':
        modify=input("update the food type you want to:")
        s="update food set F_Type=%s where fid=%s"
        x=(modify,find)

    elif change=='price':
        modify=input("update the price of food item you want :")
        s="update food set Price=%s where fid=%s"
        x=(modify,find)
    else:
        print("NO OTHER VALUE OF FOOD TABLE CAN BE UPDATED")
    mycursor.execute(s,x)
    print(mycursor.rowcount,"record updated")
    mydb.commit()

#Display Function For Food Table by type

def food_display_type(ftype):
    #ftype=input("Enter the food type required:")
    display="select*from food where F_Type='%s'"%(ftype,)
    mycursor.execute(display)
    data=mycursor.fetchall()
    count=mycursor.rowcount
    print("TOTAL NUMBER OF ROWS RETRIEVED:",count)
    print(data)
    mydb.commit()

#Display Function For Food Table by type

def food_display():
    display="select*from food"
    mycursor.execute(display)
    data=mycursor.fetchall()
    count=mycursor.rowcount
    print("TOTAL NUMBER OF ROWS RETRIEVED:",count)
    for row in data:
        print(row)
    mydb.commit()

#Delete Function For Food Table

def food_delete():
    fname=input("Enter the food item you want to delete:")
    delete="delete from food where fname='%s' "%(fname,)
    mycursor.execute(delete)
    print(mycursor.rowcount," record deleted")
    mydb.commit()

'''Billing'''

#Food Bill Insert

def FBI():
    SNo=Sr_No(1)
    print("Serial Number",SNo)
    RegNo=int(input("Enter the registration number: "))
    print("Registration Number: ",RegNo)
    Date=date.today()
    print("Today's date:", Date)
    Fid=int(input("Enter the required Food id:"))
    Values=(SNo,RegNo,Date,Fid)
    Insert="insert into billing(SNo,RegNo,Date,Fid) values(%s,%s,%s,%s)"
    mycursor.execute(Insert,Values)
    mydb.commit()


'''Customer'''

#Insert Function for Customer

def customer_insert():
    while True:
        regno=int((random.random())*1000000)
        print("Your Registration number is: ",regno)
        fname=input("Enter your first name : ")
        lname=input("Enter your last name : ")
        nationality=input("Enter your nationality : ")
        city=input("Enter your city name : ")
        address=input("Enter your complete address : ")
        idno=int(input("Enter your Id Number : "))
        idname=input("Enter your Id Name : ")
        gender=input("Enter your gender : ")
        mobileno=int(input("Enter your phone number : "))
        email=input("Enter your email address : ")
        checkin_date=datetime.datetime(int(input("Enter check in year : ")),int(input("Enter check in month : ")),int(input("Enter check in day : ")))
        checkout_date=datetime.datetime(int(input("Enter check out year : ")),int(input("Enter check out month : ")),int(input("Enter check out day : ")))
        insert='insert into customer (regno,idno,idname,mobileno,email,fname,lname,gender,nationality,city,address,checkin_date,checkout_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val=(regno,idno,idname,mobileno,email,fname,lname,gender,nationality,city,address,checkin_date,checkout_date)
        print(val)
        mycursor.execute(insert,val)
        mydb.commit()
        ch=input("Do you want to enter more customer details Y/N?  ")
        if ch.upper()=='N':
            break

def customer_display(regno):
    #cust=input("Enter regno to fetch their data : ")
    table="select * from customer where regno = %s"%(regno,)
    mycursor.execute(table)
    data=mycursor.fetchall()
    for row in data:
            print("regno: ", row[0])
            print("idno: ", row[1])
            print("idname: ", row[2])
            print("mobileno: ", row[3])
            print("email: ", row[4])
            print("fname: ", row[5])
            print("lname: ", row[6])
            print("gender: ", row[7])
            print("nationality: ", row[8])
            print("city: ", row[9])
            print("address: ", row[10])
            print("checkin_date: ", row[11])
            print("checkout_date: ", row[12])
            print("\n")
    mydb.commit()


def customer_modify():
    search=input("Enter customer's regno to update details : ")
    customer_display(search)
    change=input("Enter the detail you want to change : \n fn : fname \n ln : lname \n ci : checkin_date \n co : checkout_date \n mb : mobileno \n :")
    if change=='fn':
        new=input("Enter the updated detail : ")
        code="update customer set fname=%s where regno=%s"
        var=(new,search)
    elif change=='ln':
        new=input("Enter the updated detail : ")
        code="update customer set lname=%s where regno=%s"
        var=(new,search)
    elif change=='ci':
        new=datetime.datetime(int(input("Enter check in year : ")),int(input("Enter check in month : ")),int(input("Enter check in day : ")))
        code="update customer set checkin_date=%s where regno=%s"
        var=(new,search)
    elif change=='co':
        new=datetime.datetime(int(input("Enter check out year : ")),int(input("Enter check out month : ")),int(input("Enter check out day : ")))
        code="update customer set checkout_date=%s where regno=%s"
        var=(new,search)
    elif change=='mb':
        new=input("Enter the updated detail : ")
        code="update customer set mobileno=%s where regno=%s"
        var=(new,search)
    else :
        print("NO OTHER VALUE CAN BE CHANGED")
    mycursor.execute(code,var)
    x=mycursor.rowcount
    if x==1:
        print("The data was Modified")
    else:
        print("----Error----")
    mydb.commit()

#display function for customer

def customer_display_all():
    code="select * from customer"
    mycursor.execute(code)
    data=mycursor.fetchall()
    for x in data:
        print(x)
    mydb.commit()

#delete function for customer

def customer_delete():
    key=int(input("Enter the regno of customer to clear their data : "))
    code="delete from customer where regno= %s"%(key,)
    mycursor.execute(code)
    mydb.commit()


#Food Billing Generation

'''
Customer Table-Name,Mobile Number

'''

def FB_Generation():
    T_bill=0
    RegNo=int(input("Enter the Registration Number:"))
    if verify(RegNo)!=1:
            raise Exception("ENTERED REGNO NOT VALID")
    Date=date.today()
    Fetch="select billing.Fid,F_Name,Pices,Price from billing,food where billing.Fid=food.Fid and RegNo=%s"%(RegNo,)
    print("Today's date:",Date)
    mycursor.execute(Fetch)
    Bill=mycursor.fetchall()
    print("Fid\t Food Name\t Pcs. \t Price\t Total Price\t")
    for i in Bill:
        print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[2]*i[3])
        print()
        T_bill=T_bill+i[2]*i[3]
    gst=0.05*int(T_bill)
    tot=gst+int(T_bill)
    print('-'*47)
    print("Total Price: \t\t\t\t",T_bill)
    print('-'*47)
    print("Added GST(5%) Charged =\t\t\t ",gst)
    print('-'*47)
    print("Final Bill =\t\t\t\t ",tot)
    print('-'*47)
    mydb.commit()



#Food_bill

def food_bill(regno):
        T_bill=0
        #RegNo=int(input("Enter the Registration Number to calculate food bill : "))
        Fetch="select billing.Fid,F_Name,Pices,Price from billing,food where billing.Fid=food.Fid and RegNo=%s"%(regno,)
        mycursor.execute(Fetch)
        Bill=mycursor.fetchall()
        for i in Bill:
            T_bill=T_bill+i[2]*i[3]
        if int(T_bill)==None:
            return 0
        else:
            return int(T_bill)


#Fecth Room Price

def fetch_roomprice():
        Room_No=int(input("Enter the room number:"))
        rprice=0
        code="select Room_Price from room_info where Room_No= %s"%(Room_No,)
        mycursor.execute(code)
        fetch=mycursor.fetchall()
        rprice=0.12*(fetch[0][0])+fetch[0][0]
        return rprice

#Booking

" CALCULATE STAY PERIOD " 
def days_count(regno):
    a="select datediff(checkout_date,checkin_date) from customer where regno=%s"%(regno,)
    mycursor.execute(a)
    fetch=mycursor.fetchall()
    mydb.commit()
    a=fetch[0]
    days=a[0] 
    return days

" TOTAL CHARGES CALCULATION "
def tot_charges(regno,Room_No):
    def FB_Generation():
        T_bill=0
        try :
            #RegNo=int(input("Enter the Registration Number to calculate food bill : "))
            Fetch="select billing.Fid,F_Name,Pices,Price from billing,food where billing.Fid=food.Fid and RegNo=%s"%(regno,)
            mycursor.execute(Fetch)
            Bill=mycursor.fetchall()
            for i in Bill:
                T_bill=T_bill+i[2]*i[3]
            return int(T_bill)
        except :
            print("ERROR! ENTER CORRECT REGISTRATION NUMBER")
        

    def fetch_roomprice():
        rprice=0
        try :
            #roomno=int(input("Enter Room Number To Check Price : "))
            code="select Room_Price from room_info where Room_No= %s"%(Room_No,)
            mycursor.execute(code)
            fetch=mycursor.fetchall()
            rprice=0.12*(fetch[0][0])+fetch[0][0]
            return rprice
        except :
            print("ERROR! ENTER VALID ROOM NUMBER")
    
    total= FB_Generation()+fetch_roomprice()
    return total




    
" CALCULATE AMOUNT DUE AND PAY STATUS "

def pay_status_due(Booking_amt,regno,Room_No):
    #amt=int(input("Enter the amount paid : "))
    amt=Booking_amt
    tot=tot_charges(regno,Room_No)
    if amt==tot:
        status="Fully Paid"
        due=0
        refund_money=0
        return status,due,refund_money
    elif amt<tot and amt>0:
        status="Partially Paid"
        due=tot-amt
        refund_money=0
        return status ,due,refund_money
    elif amt==0:
        status="None Paid"
        due=tot
        refund_money=0
        return status,due,refund_money
    elif amt>tot:
        status="Fully Paid*"
        refund_money=amt-tot
        due=0
        return status,due,refund_money


def update_room_status(status,Room_No):
    code="update Room_info set Room_Status=%s where Room_No=%s"
    val=(status,Room_No)
    mycursor.execute(code,val)
    mydb.commit()
    a=mycursor.rowcount
    return a


def verify(regno):
    x=0
    code='select regno from customer'
    mycursor.execute(code)
    data=mycursor.fetchall()
    for item in data:
        #print(item[0])
        if regno==int(item[0]):
            x=1
    return x


def booking():
    try:
        no=Sr_No(1) #Serial Number
        regno=int(input("Enter your registration number : "))
        if verify(regno)!=1:
            raise Exception("ENTERED REGNO NOT VALID")
        customer_display(regno)
        time.sleep(1.5)
        input("Press Enter to continue...")
        DBT() #Display Room By Type
        time.sleep(1.5)
        Room_No=int(input("Designate Room Number to customer : "))
        input("Press Enter to continue...")
        c_in="select checkin_date from customer where regno=%s"%(regno,)
        mycursor.execute(c_in)
        cid=mycursor.fetchall()
        checkin_date=cid[0][0]
        print(checkin_date)
        c_out="select checkout_date from customer where regno=%s"%(regno,)
        mycursor.execute(c_out)
        cod=mycursor.fetchall()
        checkout_date=cod[0][0]
        print(checkout_date)
        NoOfDays=days_count(regno) #Calculate Duration
        print(NoOfDays)
        Total_Charges=tot_charges(regno,Room_No) #total charges
        print(Total_Charges)
        Booking_amt=int(input("Enter the amount paid : ")) #booking amt
        temp=pay_status_due(Booking_amt,regno,Room_No)
        pay_status=''
        if Booking_amt==Total_Charges:
            pay_status='Paid'
        elif Booking_amt>0 and Booking_amt<Total_Charges:
            pay_status='Partially Paid'
        elif Booking_amt==0:
            pay_status='None'
        elif Booking_amt<0:
            print(":-:-:-:-INVALID-:-:-:-:")
        amt_due=temp[1]  #Amt due to be paid
        amt_due=int(amt_due)
        Total_Charges=int(Total_Charges)
        refund_money=temp[2]
        Food_bill_status=food_bill(regno)
        if Food_bill_status==0:
            Food_bill_status="No food bill"
        print(Food_bill_status)
        input("Press Enter To Submit")
        checkin_date=datetime.datetime(int(input("Enter check in year : ")),int(input("Enter check in month : ")),int(input("Enter check in day : ")))
        checkout_date=datetime.datetime(int(input("Enter check out year : ")),int(input("Enter check out month : ")),int(input("Enter check out day : ")))
        regno=str(regno)
        mycursor.execute("insert into booking(Sr_No,regno,Room_No,checkin_date,checkout_date,NoOfDays,Total_Charges,Booking_amt,pay_status,Food_bill_status,amt_due,refund_money) values(%s,'%s',%s,'%s','%s',%s,%s,%s,'%s','%s',%s,%s)"%(no,regno,Room_No,checkin_date,checkout_date,NoOfDays,Total_Charges,Booking_amt,pay_status,Food_bill_status,amt_due,refund_money))
        updated_room_status=update_room_status('B',Room_No)
        if updated_room_status==1:
            print("ROOM ",Room_No,"SUCCESFULLY BOOKED FOR" ,regno)
            pay_status=temp[0]
            Food_bill_status=food_bill(regno)
            mycursor.execute("update booking set Food_bill_status='%s' and pay_status='%s' where regno=85287;"%(Food_bill_status,pay_status))
        else :
            print("ERROR IN BOOKING ROOM")
        mydb.commit()
    except:
        print(":-:-:-:-:-:ENTERED INFORMATION/REGNO IS INCORRECT PLEASE TRY AGAIN:-:-:-:-:-:" )
        mydb.rollback()
#booking()

#Checkout function

def checkout():
        regno=int(input("Enter your registration number : "))
        #Room_No=int(input("Enter your room number : "))
        input("Press enter to continue")
        FB_Generation()
        input("Press enter to continue")
        print("Room Price with added GST is : ",fetch_roomprice())
        input("Press enter to continue")
        a="select pay_status from booking where regno=%s"%(regno,)
        mycursor.execute(a)
        pay_status=mycursor.fetchall()
        if pay_status=='Partially Paid':
            b="select amt_due from booking where regno=%s"%(regno,)
            mycursor.execute(b)
            a=mycursor.fetchall()
            due=a+food_bill(regno)
            print("REMAINING AMOUNT TO BE PAID IS : ",due)
        elif pay_status=='Fully Paid':
            b="select amt_due from booking where regno=%s"%(regno,)
            mycursor.execute(b)
            a=mycursor.fetchall()
            due=a+food_bill(regno)
            print("REMAINING AMOUNT TO BE PAID IS : ",due)


def customer():
    text_1=int(input('''Enter:
                        1. Add new customer Details
                        2. Modify details of customer
                        3. Display customer Details
                        4. Display all customers Details
                        5. Delete a customer record
                        6. Return to main menu
                        
                        >>>'''))
    if text_1==1:
        customer_insert()
        customer()
    elif text_1==2:
        customer_modify()
        customer()
    elif text_1==3:
        x=int(input("Enter the Registration Number:"))
        customer_display(x)
        customer()
    elif text_1==4:
        customer_display_all()
        customer()
    elif text_1==5:
        customer_delete()
        customer()
    elif text_1==6:
        menu()
    else:
        print("Invalid Input")
    
def booking_1():        
    text_1=int(input('''Enter:
                        1. Display rooms
                        2. Book room
                        3. Checkout room
                        4. Roomm bill
                        5. Return to main menu
                            
                        >>>'''))
    if text_1==1:
         DBT()
         booking_1()
    elif text_1==2:
        booking()
        booking_1()
    elif text_1==3:
        checkout()
        booking_1()
    elif text_1==4:
        fetch_roomprice()
        booking()
    elif text_1==5:
        menu()
    else:
        print("Invalid Input")
def room():
    text_1=int(input('''Enter:
                        1. Add room
                        2. Delete room
                        3. Update room
                        4. Update room status
                        5. Display all
                        6. Display by type
                        7. Display booked
                        8. Display vaccant
                        9. Return to main menu
                        
                        >>>'''))
    if text_1==1:
        room_insert()
        room()
    elif text_1==2:
        room_delete()
        room()
    elif text_1==3:
        room_modify()
        room()
    elif text_1==4:
        room_modify()
        room()
    elif text_1==5:
        DNW()
        room()
    elif text_1==6:
        DBT()
        room()
    elif text_1==7:
        DB()
        room()
    elif text_1==8:
        DV()
        room()
    elif text_1==9:
        menu()
    else:
        print("Invalid Input")

def food():
    text_1=int(input('''Enter:
                        1. Add a food item
                        2. Update ava/notav
                        3. Delete
                        4. Display all
                        5. Display B
                        6. Display L
                        7. Display D
                        8. Book a food
                        9. Food bill
                        10. Return to main menu
                        
                        >>>'''))
        
    if text_1==1:
        food_insert()
        food()
    elif text_1==2:
        food_modify()
        food()
    elif text_1==3:
        food_delete()
        food()
    elif text_1==4:
        food_display()
        food()
    elif text_1==5:
        food_display_type('B')
        food()
    elif text_1==6:
        food_display_type('L')
        food()
    elif text_1==7:
        food_display_type('D')
        food()
    elif text_1==8:
        FBI()  #To book a food(Food bill insertion)
        food()
    elif text_1==9:
        FB_Generation()
        food()
    elif text_1==10:
        menu()
    else:
        print("Inalid Input")

def settings():
    pass


#Menu

def menu():

    text=int(input('''Enter 
                   1. Customer...
                   2. Booking...
                   3. Room...
                   4. Food...
                   5. Settings..
                   6. Exit...
                   
                   >>>'''))
    if text==1:
        customer()
    elif text==2:
        booking_1()
    elif text==3:
        room()
    elif text==4:
        food()
    elif text==5:
        settings()
    elif text==6:
        pass
    else:
        print("The given Input is wrong")

menu()