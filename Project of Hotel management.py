# THIS IS A PROGRAM OF HOTEL MANAGEMENT SYSTEM

# IMPORT ALL EXTERNAL LIBRARIES
import mysql.connector as mysqlt
import datetime
from datetime import date
import random
import PIL.Image
from PIL import Image
import tkinter.ttk as ttk
from tkinter import *
from plyer import notification
from tkinter import messagebox
from tabulate import tabulate
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from time import sleep
import webbrowser
import calendar
import time
import csv

# CALLING OWN CREATING LIBRARY
import _Menu_card_
import _Room_info_
import _Hotel_policies_

# CONNECT PYTHON WITH MYSQL SERVER TO ENTER GIVEN INFORMATION
mydb = mysqlt.connect(
    host="localhost",
    user="root",
    password="ujjwal2003",
    database="hotel_management"
)
cursor = mydb.cursor()

##if mydb.is_connected():
##    print("CONNECTION ESTABILISED")
##else:
##    print("CONNECTION ERROR !!")

# GLOBAL LIST DECLARATION
name_of_children = []  # FOR NAME OF CHILDREN
number_of_customer_adult = []  # FOR NUMBER OF ADULTS
number_of_customer_children = []  # FOR NUMBER OF CHILDREN
number_of_customer = []  # FOR NUMBER OF CUSTOMER
name_of_the_customer = []  # FOR NAME OF CUSTOMERS
age_of_the_customer = []  # FOR AGE OF CUSTOMERS
gender_of_the_customer = []  # FOR GENDER OF CUSTOMERS
aadhaar_of_the_customer = []  # FOR AADHAAR CARD OF CUSTOMERS
mobile_of_the_customer = []  # FOR MOBILE NUMBER OF CUSTOMERS
address_of_customer = []  # FOR ADDRESS OF CUSTOMERS
number_of_customer = []  # FOR NUMBER OF CUSTOMER
checkin_date = []  # FOR CHECK-IN DATE OF CUSTOMERS
checkin_month = []  # FOR CHECK-IN MONTH OF CUSTOMERS
year_in = []  # FOR CHECK-IN YEAR OF CUSTOMERS
checkout_date = []  # FOR CHECK-OUT DATE OF CUSTOMERS
checkout_month = []  # FOR CHECK-OUT MONTH OF CUSTOMERS
out_year = []  # FOR CHECK-OUT YEAR OF CUSTOMERS
for_owner_room_number = []  # FOR NUMBER OF ROOM
bill_numbering = [] # FOR BILL NUMBER RANDOMLY GENERATED NUMBER

# FOR CHECKING-INFO AND FOR DELETED DATA
name_info = []  # FOR LAST NAME
age_info = []  # FOR LAST AGE
gender_info = []  # FOR LAST GENDER
aadhaar_info = []  # FOR LAST AADHAAR NUMBER
room_type = []  # FOR ROOM TYPE
total_price = []  # FOR TOTAL PRICE

# THIS IS ONLY FOR TABLE GENERATOR AND FOR INVOICE WHICH CLEAR AFTER EVERY RE-RUN
name_of_customer = []  # FOR TABLE NAME OF CUSTOMERS
age_of_customer = []  # FOR TABLE AGE OF CUSTOMERS
gender_of_customer = []  # FOR TABLE GENDER OF CUSTOMERS
aadhaar_of_customer = []  # FOR TABLE AADHAAR CARD OF CUSTOMERS
mobile_of_customer = []  # FOR TABLE MOBILE NUMBER OF CUSTOMERS
room_of_type = []  # FOR BILL INVOICE TYPE OF ROOM
room_of_number = []  # FOR BILL INVOICE ROOM NUMBER
room_of_price = []  # FOR BILL INVOICE PRICE OF ROOM
day_of_checkin = []  # FOR BILL INVOICE CHECK-IN DATE
month_of_checkin = []  # FOR BILL INVOICE CHECK-IN MONTH
year_of_checkin = []  # FOR BILL INVOICE CHECK-IN YEAR
day_of_checkout = []  # FOR BILL INVOICE CHECK-OUT DATE
month_of_checkout = []  # FOR BILL INVOICE CHECK-OUT MONTH
year_of_checkout = []  # FOR BILL INVOICE CHECK-OUT YEAR

booking_loop = 0  # STARTING VALUE ASSIGNING TO BE ZERO

def startup():
    # FOR TABLE AND INVOICE CLEAR ALL PREVIOUS DATA
    name_of_customer.clear()
    age_of_customer.clear()
    gender_of_customer.clear()
    aadhaar_of_customer.clear()
    mobile_of_customer.clear()
    room_of_type.clear()
    room_of_number.clear()
    room_of_price.clear()
    day_of_checkin.clear()
    month_of_checkin.clear()
    year_of_checkin.clear()
    day_of_checkout.clear()
    month_of_checkout.clear()
    year_of_checkout.clear()

    # STARTUP MENU RUN FROM HERE
    for i in range(100):
        print("")
        print("LOADING.....")
        sleep(3)
        print("\n" * 4)
        print("\t\t\t", "=" * 20, " RE-RUN MENU ", "=" * 23)
        print("\n")
        xyz1 = str(input("YOU WANT TO RUN THE PROGRAM AGAIN [Y/N]="))
        xyz = xyz1.upper()
        if xyz == "Y" or xyz == "YES":
            print("\n" * 4)
            print("\t\t", "=" * 26, " RESTART MENU ", "=" * 30)
            print("\n" * 1)
            main_menu()
        elif xyz == "N" or xyz == "NO":
            print("")
            win_exit_str = str(input("ARE YOU SURE YOU EXIT THE PROGRAM !! [Y/N] = "))
            win_exit = win_exit_str.upper()
            if win_exit == "Y" or win_exit == "YES":
                # PATH LINK
                my_image = PIL.Image.open(r"E:\Python\Cs_Project\python_thankyou.png")
                my_image.show()
                exit()
            elif win_exit == "N" or win_exit == "NO":
                startup()
            else:
                startup()
        else:
            print("WRONG CHOICE")


print("")

def booking():
    # OPENING CSV FILE
    file_check = open("type_database.csv", "w")
    create_writer = csv.writer(file_check)  # MAKE A WRITER TO ADD ROWS

    # CALL THE FUNCTION OF CHECK - IN OR CHECK - OUT
    # check_in_or_out()     # THIS IS ONLY FOR EMERGENCY CASE

    # PASSING THE VARIABLE IN BETWEEN THE FUNCTION
    choose_month_upper, number_of_days, customer_check_in, month, year, check_out_date, _mon_out_, _yr_out = check_in_or_out()

    # MAKE A WRITEROW
    create_writer.writerow(["Check-in Date", "Check-in Month", "Check-in Year"])
    create_rec = [customer_check_in, month, year]
    create_writer.writerow(create_rec)
    # MAKE A WRITEROW
    create_writer.writerow(["Check-out Date", "Check-out Month", "Check-out Year"])
    create_rec = [check_out_date, _mon_out_, _yr_out]
    create_writer.writerow(create_rec)
    # MAKE A WRITEROW
    create_writer.writerow(["Number of days"])
    create_rec = [number_of_days]
    create_writer.writerow(create_rec)

    # NUMBER OF ADULT AND NUMBER OF CHILDREN
    print("")
    print("\t\t", "=" * 26, "NUMBER OF ADULTS", "=" * 30)
    print("")
    str_customer_adult = str(input("HOW MANY ADULTS ARE ?? "))
    try:
        customer_adult = int(str_customer_adult)
        print("")
        if customer_adult != 0:
            number_of_customer_adult.append(customer_adult)  # append function
            print("OKAY!! ", customer_adult, " ADULTS ")
            print("")
            sleep(3)
            print("\t\t", "=" * 26, "NUMBER OF CHILDREN", "=" * 30)
            print("")
            str_customer_children = str(input("HOW MANY CHILDREN ARE ?? "))
            try:
                customer_children = int(str_customer_children)
                number_of_customer_children.append(customer_children)  # append function
                if customer_children == 0 or customer_children != 0:
                    print("")
                    print("OKAY !!", customer_children, " CHILDREN")
                    print("")
                    sleep(3)
                    if customer_children > 0:
                        for children in range(customer_children):  # THIS LOOP WILL TERMINATE WITH CHILDREN NUMBER
                            print("\t\t\t  ", "-" * 15, "INFORMATION OF CHILD", children + 1, "-" * 15)
                            print("")
                            children_name_lower = input("ENTER NAME OF THE CHILD [OPTIONAL] = ")
                            children_name = children_name_lower.upper()
                            children_name_append = name_of_children.append(children_name)  # append function
                            str_children_age = str(input("ENTER THE AGE OF CHILD = "))
                            print("")
                            print("LOADING.....")
                            sleep(3)
                            try:
                                children_age = int(str_children_age)
                                if children_age <= 9:
                                    print("")
                                    print("YOUR CHILD", children_name, "CHILDREN NO.", children + 1, "ENTRY IS FREE")
                                    print("")
                                    print("NO NEED TO PAY EXTRA AMOUNT TO BOOK THE ROOM")

                                    customer_number = customer_adult
                                    number_of_customer.append(customer_number)  # NUMBER OF CUSTOMER ADDED IN THE LIST
                                    # append function
                                    print("")
                                elif 10 <= children_age <= 17:
                                    print("")
                                    print("YOUR CHILD", children_name, "CHILDREN NO.", children + 1,
                                          "ENTRY IS NOT FREE")
                                    print("")
                                    print("YOU NEED TO PAY EXTRA AMOUNT TO BOOK THE ROOM FOR YOUR CHILD")

                                    customer_number = customer_adult + customer_children
                                    number_of_customer.append(customer_number)  # NUMBER OF CUSTOMER ADDED IN THE LIST
                                    # append function
                                    print("")
                                elif children_age >= 18:
                                    print("")
                                    print("THE PERSON AGE OF", children_age, "IS NOT A CHILD")
                                    print("")
                                    print("PLEASE RE-RUN THE PROGRAM\n\nAND ENTER THE CORRECT INFORMATION")
                                    startup()
                                else:
                                    print("")
                                    print("INVALID AGE ENTERED")
                                    print("\nPLEASE RE-RUN THE PROGRAM\n\nAND ENTER THE CORRECT INFORMATION")
                                    startup()
                            except:
                                print("")
                                print("AGE ONLY IN NUMERICAL FORM BUT YOU ENTER IN STRING")
                                print("\nPLEASE RE-RUN THE PROGRAM")
                                messagebox.showerror("Error", "Age only in Numerical")
                                startup()
                    else:
                        print("NUMBER OF TOTAL CUSTOMERS ARE = ", customer_adult)
                else:
                    print("")
                    print("SORRY YOU ENTERED WRONG INFORMATION")
                    print("\nPLEASE RE-RUN THE PROGRAM")
                    startup()
            except:
                print("")
                print("NUMBER OF CHILDERNS ONLY IN NUMBERS")
                print("\nRE-RUN THE PROGRAM")
                messagebox.showerror("Error", "Number of Children Only in Numericals")
                startup()
        elif customer_adult == 0:
            print("")
            print("LOADING.....")
            sleep(3)
            print("")
            print("NUMBER OF ADULT = ", customer_adult)
            print("\nNO ADULT WITH YOU")
            print("\nYOU NOT BOOKED THE ROOM\n\nBECAUSE NO UNDER AGE PERSON BOOK THE ROOM IN OUR HOTEL")
            messagebox.showwarning("Warning", "No person Under 18 Booked Room in our Hotel SORRY !!")
            exit()
        else:
            print("")
            print("INVALID SYNTAX")
            startup()
    except:
        print("")
        print("NUMBER OF ADULTS ONLY IN NUMBERS")
        print("\nRE-RUN THE PROGRAM")
        messagebox.showerror("Error", "Number of Adults Only in Numericals")
        startup()

    # ADULT CUSTOMER INFORMATION
    print("")
    try:
        count = 0
        for num_adult_customer in range(customer_adult):
            count = count + 1
            print("")
            print("\t        ", "=" * 23, " DETAIL OF ADULT CUSTOMER ", count, "=" * 23)
            print("")

            customer_name = str(input("ENTER NAME OF THE CUSTOMERS = "))  # NAME OF THE CUSTOMER
            customer_name_UPPER = customer_name.upper()
            name_of_customer.append(customer_name_UPPER)  # NAME OF CUSTOMER ADDED IN THE LIST
            name_of_the_customer.append(customer_name_UPPER)  # NAME OF CUSTOMER ADDED IN THE LIST
            # append function
            customer_age_str = str(input("ENTER YOUR AGE = "))
            try:
                customer_age = int(customer_age_str)
                if 18 <= customer_age <= 100:
                    age_of_customer.append(customer_age)  # AGE OF CUSTOMER ADDED IN THE LIST
                    age_of_the_customer.append(customer_age)  # AGE OF CUSTOMER ADDED IN THE LIST
                    # append function
                elif customer_age < 18:
                    print("")
                    print("THIS PERSON IS NOT ADULT")
                    print("\nBEACAUSE HIS/HER AGE IS UNDER 18")
                    print("\nINVALID ENTRY")
                    print("\nPLEASE RE-RUN THE PROGRAM")
                    startup()
                else:
                    print("")
                    print("WRONG AGE ENTERED ONLY CUSTOMER UPTO 100 YEARS")
                    print("\nIF ANY OF THE CUSTOMER IS ABOVE 100 YEARS PLEASE GO TO OUR ONLINE WEBSITE")
                    print("\nIF YOU ENTERED WRONGLY SO ENTER DETAILS AGAIN OF AGE")
                    print("")
                    customer_age_str = str(input("ENTER YOUR AGE = "))
                    try:
                        customer_age = int(customer_age_str)
                        if 18 <= customer_age <= 80:
                            print("NOW YOU ENTERED CORRECT AGE INFORMATION")
                            age_of_customer.append(customer_age)  # AGE OF CUSTOMER ADDED IN THE LIST
                            age_of_the_customer.append(customer_age)  # AGE OF CUSTOMER ADDED IN THE LIST
                            # append function
                        else:
                            if customer_age < 18:
                                print("YOU ENTER WRONG INFORMATION UNDER 18 AGE PERSON IS COUNTED AS CHILD NOT ADULT")
                                print("")
                                print("PLEASE RE-RUN THE PROGRAM")
                                startup()
                            else:
                                print("YOU AGAIN ENTER WRONG AGE")
                                print("\nRE-RUN THE PROGRAM")
                                startup()
                    except:
                        print("INVALID SYNTAX")
                        print("\nRE-RUN THE PROGRAM")
                        messagebox.showerror("Error", "Age only in Numericals")
                        startup()

                customer_gender = str(
                    input("ENTER THE GENDER OF CUSTOMER [MALE/FEMALE/OTHER]= "))  # GENDER OF THE CUSTOMER
                customer_gender_UPPER = customer_gender.upper()
                if customer_gender_UPPER == "MALE" or "M":
                    gender_of_customer.append(customer_gender_UPPER)  # GENDER OF CUSTOMER ADDED IN THE LIST
                    gender_of_the_customer.append(customer_gender_UPPER)  # GENDER OF CUSTOMER ADDED IN THE LIST
                    # append function
                elif customer_gender_UPPER == "FEMALE" or "F":
                    gender_of_customer.append(customer_gender_UPPER)  # GENDER OF CUSTOMER ADDED IN THE LIST
                    gender_of_the_customer.append(customer_gender_UPPER)  # GENDER OF CUSTOMER ADDED IN THE LIST
                    # append function
                elif customer_gender_UPPER == "OTHER" or "O":
                    gender_of_customer.append(customer_gender_UPPER)  # GENDER OF CUSTOMER ADDED IN THE LIST
                    gender_of_the_customer.append(customer_gender_UPPER)  # GENDER OF CUSTOMER ADDED IN THE LIST
                    # append function
                else:
                    print("")
                    print("WRONG GENDER ENTERED\n")
                    print("ONLY THREE GENDER EXISTS IN OUR WEBSITE\n")
                    print("RE-RUN THE PROGRAM")
                    startup()
                print("")

                # TO UPLOAD IDENTITY CARD DETAILS
                print("FOR UNIQUE IDENTIFICATION ! \nTO UPLOAD AADHAAR CARD DETAILS ")
                print("")
                # AADHAAR CARD DETAILS
                str_customer_aadhaar_details = str(
                    input("ENTER THE AADHAAR CARD NUMBER [12 DIGIT] = "))  # length of number is 12
                aadhaar_length = len(str_customer_aadhaar_details)
                print("")
                print("LOADING......")
                sleep(3)
                print("")
                try:
                    customer_aadhaar_details = int(str_customer_aadhaar_details)
                    if aadhaar_length == 12:
                        aadhaar_of_customer.append(
                            customer_aadhaar_details)  # AADHAAR IDENTIFICATION OF CUSTOMER ADDED IN THE LIST
                        aadhaar_of_the_customer.append(
                            customer_aadhaar_details)  # AADHAAR IDENTIFICATION OF CUSTOMER ADDED IN THE LIST
                        # append function
                        print("YOUR AADHAAR NUMBER RECORDED")

                        # MAKE A WRITEROWS
                        create_writer.writerow(["Name", "Age", "Gender", "Aadhaar"])
                        create_rec = [customer_name_UPPER, customer_age, customer_gender_UPPER,
                                      customer_aadhaar_details]
                        create_writer.writerow(create_rec)

                        # INSERT DATA INTO MYSQL SERVER
                        columns_create_3 = "INSERT INTO adult_looping(NAME,AGE,GENDER,AADHAAR) VALUES(%s,%s,%s,%s)"
                        _input_3 = (customer_name_UPPER, customer_age, customer_gender_UPPER, customer_aadhaar_details)
                        cursor.execute(columns_create_3, _input_3)
                        mydb.commit()

                    elif 1 <= aadhaar_length <= 11 or 13 <= aadhaar_length <= 20:
                        print("YOUR AADHAAR NUMBER IS WRONG")
                        print("\nPLEASE RE-ENTERED THE DETAILS OF AADHAAR CARD")
                        print("\nTHE LENGTH OF AADHAAR NUMBER IS 12\n")
                        str_customer_aadhaar_details = str(
                            input("ENTER THE AADHAAR CARD NUMBER = "))  # length of number is 12
                        aadhaar_length = len(str_customer_aadhaar_details)
                        print("")
                        print("LOADING......")
                        sleep(3)
                        print("")
                        try:
                            customer_aadhaar_details = int(str_customer_aadhaar_details)
                            if aadhaar_length == 12:
                                aadhaar_of_customer.append(
                                    customer_aadhaar_details)  # AADHAAR IDENTIFICATION OF CUSTOMER ADDED IN THE LIST
                                aadhaar_of_the_customer.append(
                                    customer_aadhaar_details)  # AADHAAR IDENTIFICATION OF CUSTOMER ADDED IN THE LIST
                                # append function
                                print("YOUR AADHAAR NUMBER RECORDED")

                                # MAKE A WRITEROWS
                                create_writer.writerow(["Name", "Age", "Gender", "Aadhaar"])
                                create_rec = [customer_name_UPPER, customer_age, customer_gender_UPPER,
                                              customer_aadhaar_details]
                                create_writer.writerow(create_rec)

                                # INSERT DATA INTO MYSQL SERVER
                                columns_create_3 = "INSERT INTO adult_looping(NAME,AGE,GENDER,AADHAAR) VALUES(%s,%s,%s,%s)"
                                _input_3 = (
                                customer_name_UPPER, customer_age, customer_gender_UPPER, customer_aadhaar_details)
                                cursor.execute(columns_create_3, _input_3)
                                mydb.commit()

                            else:
                                print("\nWRONG AADHAAR NUMBER SECOND TIME \n\nPLEASE RE-RUN THE PROGRAM")
                                startup()
                        except:
                            print("\nRE-RUN THE PROGRAM \n\nAADHAAR NUMBER ONLY IN NUMERICAL FORM")
                            messagebox.showerror("Error", "Aadhaar Number only in Numericals not in Alphabets")
                            startup()
                    else:
                        print("\THE AADHAAR NUMBER IS ONLY OF 12 NUMBERS")
                        print("\nPLEASE RE-RUN THE PROGRAM")
                        startup()
                except:
                    print("\nRE-RUN THE PROGRAM \n\nAADHAAR NUMBER ONLY IN NUMERICAL FORM")
                    messagebox.showerror("Error", "Aadhaar Number only in Numericals not in Alphabets")
                    startup()

            except:
                print("")
                print("\nYOU ENTERED THE WRONG AGE [IT IS ONLY IN NUMERICALS FORM]")
                print("\nRE-RUN THE PROGRAM")
                messagebox.showerror("Error", "Age only in Numericals")
                startup()

        # FOR INFO DETAILS
        name_info.append(customer_name_UPPER)
        age_info.append(customer_age)
        gender_info.append(customer_gender_UPPER)
        aadhaar_info.append(customer_aadhaar_details)

        print("")
        print("\t\t", "=" * 30, " OTHER DETAILS ", "=" * 30)

        print("")
        customer_address = str(input("ENTER YOUR PERMANENT ADDRESS = "))  # ADDRESS OF THE CUSTOMER
        customer_address_UPPER = customer_address.upper()
        address_of_customer.append(customer_address_UPPER)
        # append function
        print("")

        str_customer_mobile_number = str(input("ENTER YOUR MOBILE NUMBER [10 DIGIT] = "))  # MOBILE NUMBER OF CUSTOMER
        customer_mobile_length = len(str_customer_mobile_number)
        try:
            customer_mobile_number = int(str_customer_mobile_number)
            if customer_mobile_length == 10:
                print("")
                print("LOADING.....")
                sleep(3)
                print("")
                mobile_of_customer.append(customer_mobile_number)  # MOBILE NUMBER ADDED IN THE LIST
                mobile_of_the_customer.append(customer_mobile_number)  # MOBILE NUMBER ADDED IN THE LIST
                # append function
                print("YOU ENTERED THE CORRECT MOBILE NUMBER")
                # MAKE A WRITEROWS
                create_writer.writerow(["Address", "Mobile Number"])
                create_rec = [customer_address_UPPER, customer_mobile_number]
                create_writer.writerow(create_rec)

            elif 2 <= customer_mobile_length <= 9 or 11 <= customer_mobile_length <= 16:
                print("\nYOU ENTERED THE WRONG MOBILE NUMBER\n")
                print("PLEASE RE - ENTERED YOUR MOBILE NUMBER\n")
                str_customer_mobile_number = str(
                    input("ENTER YOUR MOBILE NUMBER [10 DIGIT] = "))  # MOBILE NUMBER OF CUSTOMER 2 time
                customer_mobile_length = len(str_customer_mobile_number)
                print("")
                print("LOADING.....")
                sleep(3)
                print("")
                try:
                    customer_mobile_number = int(str_customer_mobile_number)
                    if customer_mobile_length == 10:
                        print("\nNOW YOU ENTERED THE CORRECT MOBILE NUMBER")
                        mobile_of_customer.append(customer_mobile_number)  # MOBILE NUMBER ADDED IN THE LIST
                        mobile_of_the_customer.append(customer_mobile_number)  # MOBILE NUMBER ADDED IN THE LIST
                        # append function

                        # MAKE A WRITEROWS
                        create_writer.writerow(["Address", "Mobile Number"])
                        create_rec = [customer_address_UPPER, customer_mobile_number]
                        create_writer.writerow(create_rec)

                    else:
                        print("\nYOU ENTERED WRONG MOBILE NUMBER SECOND TIME")
                        print("\nNOW YOU RE-RUN THE PROGRAM")
                        startup()
                except:
                    print("\nMOBILE NUMBER ONLY IN NUMERICAL FORM")
                    print("\nPLEASE RE-RUN THE PROGRAM")
                    messagebox.showerror("Error", "Mobile Number only in Numericals")
                    startup()
            else:
                print("\nYOU ENTERED WRONG FORMAT OF MOBILE NUMBER")
                print("\nPLEASE RE-RUN THE PROGRAM")
                startup()
        except:
            print("\nMOBILE NUMBER ONLY IN NUMERICAL FORM")
            print("\nPLEASE RE-RUN THE PROGRAM")
            messagebox.showerror("Error", "Mobile Number only in Numericals")
            startup()

        print("")
        print("PLEASE WAIT WE GENERATE A TABLE.....")
        sleep(8)
        print("")
        # CREATING A TABLE
        # WHEN NUMBER OF CUSTOMER IS 1
        if customer_adult == 1:
            print("NUMBER OF ADULT CUSTOMER", customer_adult)
            list1 = ["1"]
            list2 = [name_of_customer[0]]
            list3 = [age_of_customer[0]]
            list4 = [gender_of_customer[0]]
            list5 = [aadhaar_of_customer[0]]
            list6 = [mobile_of_customer[0]]
            table = PrettyTable(
                ["Number of customer", "Name of the customer", "Age", "Gender", "Identification", "Mobile number"])
            for customer_table in range(0, customer_adult):
                table.add_row(
                    [list1[customer_table], list2[customer_table], list3[customer_table], list4[customer_table],
                     list5[customer_table], list6[customer_table]])
            print(table)
        # WHEN NUMBER OF CUSTOMER IS 2
        elif customer_adult == 2:
            print("NUMBER OF ADULT CUSTOMERS", customer_adult)
            list1 = ["1", "2"]
            list2 = [name_of_customer[0], name_of_customer[1]]
            list3 = [age_of_customer[0], age_of_customer[1]]
            list4 = [gender_of_customer[0], gender_of_customer[1]]
            list5 = [aadhaar_of_customer[0], aadhaar_of_customer[1]]
            list6 = [mobile_of_customer[0], mobile_of_customer[0]]
            table = PrettyTable(
                ["Number of customer", "Name of the customer", "Age", "Gender", "Identification", "Mobile number"])
            for customer_table in range(0, customer_adult):
                table.add_row(
                    [list1[customer_table], list2[customer_table], list3[customer_table], list4[customer_table],
                     list5[customer_table], list6[customer_table]])
            print(table)
        # WHEN NUMBER OF CUSTOMER IS 3
        elif customer_adult == 3:
            print("NUMBER OF ADULT CUSTOMERS", customer_adult)
            list1 = ["1", "2", "3"]
            list2 = [name_of_customer[0], name_of_customer[1], name_of_customer[2]]
            list3 = [age_of_customer[0], age_of_customer[1], age_of_customer[2]]
            list4 = [gender_of_customer[0], gender_of_customer[1], gender_of_customer[2]]
            list5 = [aadhaar_of_customer[0], aadhaar_of_customer[1], aadhaar_of_customer[2]]
            list6 = [mobile_of_customer[0], mobile_of_customer[0], mobile_of_customer[0]]
            table = PrettyTable(
                ["Number of customer", "Name of the customer", "Age", "Gender", "Identification", "Mobile number"])
            for customer_table in range(0, customer_adult):
                table.add_row(
                    [list1[customer_table], list2[customer_table], list3[customer_table], list4[customer_table],
                     list5[customer_table], list6[customer_table]])
            print(table)
        # WHEN NUMBER OF CUSTOMER IS 4
        elif customer_adult == 4:
            print("NUMBER OF ADULT CUSTOMERS", customer_adult)
            list1 = ["1", "2", "3", "4"]
            list2 = [name_of_customer[0], name_of_customer[1], name_of_customer[2], name_of_customer[3]]
            list3 = [age_of_customer[0], age_of_customer[1], age_of_customer[2], age_of_customer[3]]
            list4 = [gender_of_customer[0], gender_of_customer[1], gender_of_customer[2], gender_of_customer[3]]
            list5 = [aadhaar_of_customer[0], aadhaar_of_customer[1], aadhaar_of_customer[2], aadhaar_of_customer[3]]
            list6 = [mobile_of_customer[0], mobile_of_customer[0], mobile_of_customer[0], mobile_of_customer[0]]
            table = PrettyTable(
                ["Number of customer", "Name of the customer", "Age", "Gender", "Identification", "Mobile number"])
            for customer_table in range(0, customer_adult):
                table.add_row(
                    [list1[customer_table], list2[customer_table], list3[customer_table], list4[customer_table],
                     list5[customer_table], list6[customer_table]])
            print(table)
        # WHEN NUMBER OF CUSTOMER IS 5
        elif customer_adult == 5:
            print("NUMBER OF ADULT CUSTOMERS", customer_adult)
            list1 = ["1", "2", "3", "4", "5"]
            list2 = [name_of_customer[0], name_of_customer[1], name_of_customer[2], name_of_customer[3],
                     name_of_customer[4]]
            list3 = [age_of_customer[0], age_of_customer[1], age_of_customer[2], age_of_customer[3], age_of_customer[4]]
            list4 = [gender_of_customer[0], gender_of_customer[1], gender_of_customer[2], gender_of_customer[3],
                     gender_of_customer[4]]
            list5 = [aadhaar_of_customer[0], aadhaar_of_customer[1], aadhaar_of_customer[2], aadhaar_of_customer[3],
                     aadhaar_of_customer[4]]
            list6 = [mobile_of_customer[0], mobile_of_customer[0], mobile_of_customer[0], mobile_of_customer[0],
                     mobile_of_customer[0]]
            table = PrettyTable(
                ["Number of customer", "Name of the customer", "Age", "Gender", "Identification", "Mobile number"])
            for customer_table in range(0, customer_adult):
                table.add_row(
                    [list1[customer_table], list2[customer_table], list3[customer_table], list4[customer_table],
                     list5[customer_table], list6[customer_table]])
            print(table)
        # WHEN NUMBER OF CUSTOMER IS 6
        elif customer_adult == 6:
            print("NUMBER OF ADULT CUSTOMERS", customer_adult)
            list1 = ["1", "2", "3", "4", "5", "6"]
            list2 = [name_of_customer[0], name_of_customer[1], name_of_customer[2], name_of_customer[3],
                     name_of_customer[4], name_of_customer[5]]
            list3 = [age_of_customer[0], age_of_customer[1], age_of_customer[2], age_of_customer[3], age_of_customer[4],
                     age_of_customer[5]]
            list4 = [gender_of_customer[0], gender_of_customer[1], gender_of_customer[2], gender_of_customer[3],
                     gender_of_customer[4], gender_of_customer[5]]
            list5 = [aadhaar_of_customer[0], aadhaar_of_customer[1], aadhaar_of_customer[2], aadhaar_of_customer[3],
                     aadhaar_of_customer[4], aadhaar_of_customer[5]]
            list6 = [mobile_of_customer[0], mobile_of_customer[0], mobile_of_customer[0], mobile_of_customer[0],
                     mobile_of_customer[0], mobile_of_customer[0]]
            table = PrettyTable(
                ["Number of customer", "Name of the customer", "Age", "Gender", "Identification", "Mobile number"])
            for customer_table in range(0, customer_adult):
                table.add_row(
                    [list1[customer_table], list2[customer_table], list3[customer_table], list4[customer_table],
                     list5[customer_table], list6[customer_table]])
            print(table)
        # WHEN NUMBER OF CUSTOMER IS ELSE
        else:
            print("NUMBER OF ADULT CUSTOMERS", customer_adult)
            list1 = ["1", "2", "3", "4", "5", "6", "7"]
            list2 = [name_of_customer[0], name_of_customer[1], name_of_customer[2], name_of_customer[3],
                     name_of_customer[4], name_of_customer[5], name_of_customer[6]]
            list3 = [age_of_customer[0], age_of_customer[1], age_of_customer[2], age_of_customer[3], age_of_customer[4],
                     age_of_customer[5], age_of_customer[6]]
            list4 = [gender_of_customer[0], gender_of_customer[1], gender_of_customer[2], gender_of_customer[3],
                     gender_of_customer[4], gender_of_customer[5], gender_of_customer[6]]
            list5 = [aadhaar_of_customer[0], aadhaar_of_customer[1], aadhaar_of_customer[2], aadhaar_of_customer[3],
                     aadhaar_of_customer[4], aadhaar_of_customer[5], aadhaar_of_customer[6]]
            list6 = [mobile_of_customer[0], mobile_of_customer[0], mobile_of_customer[0], mobile_of_customer[0],
                     mobile_of_customer[0], mobile_of_customer[0], mobile_of_customer[0]]
            table = PrettyTable(
                ["Number of customer", "Name of the customer", "Age", "Gender", "Identification", "Mobile number"])
            for customer_table in range(0, customer_adult):
                table.add_row(
                    [list1[customer_table], list2[customer_table], list3[customer_table], list4[customer_table],
                     list5[customer_table], list6[customer_table]])
            print(table)

        print("")
        print("LOADING.....")
        sleep(5)

        # PASSING THE VARIABLE IN BETWEEN THE FUNCTION
        room_rent, room, room_number = display_room()

        print("")
        print("YOU BOOK ROOM OF CATEGORY ", room)
        if customer_adult <= 3:
            number_of_room = 1
            room_rent_after = room_rent * number_of_room * number_of_days
            room_type.append(room)
            total_price.append(room_rent_after)
            room_of_type.append(room)
            room_of_number.append(number_of_room)
            room_of_price.append(room_rent_after)
        elif customer_adult > 3:
            print("")
            str_number_of_room = input("ENTER HOW MANY ROOM YOU BOOK [1/2/3 OR SO ON] = ")
            try:
                number_of_room = int(str_number_of_room)
                if number_of_room == 0:
                    print("")
                    print("SORRY WE CANCEL YOUR BOOKING BECAUSE YOU ENTER WRONG INFORMATION")
                    print("\nIF YOU BOOK THE HOTEL RE-RUN THE PROGRAM")
                    startup()
                elif number_of_room != 0:
                    if number_of_days == 0:
                        room_rent_after = room_rent * number_of_room
                    else:
                        room_rent_after = room_rent * number_of_room * number_of_days
                    room_type.append(room)
                    total_price.append(room_rent_after)
                    room_of_type.append(room)
                    room_of_number.append(number_of_room)
                    room_of_price.append(room_rent_after)
                else:
                    print("INVALID SYNTAX")
                    print("\nPLEASE RE-RUN THE PROGRAM")
                    startup()
            except:
                print("")
                print("NUMBER OF ROOM ONLY IN NUMERICAL FORM")
                print("\nPLEASE RE-RUN THE PROGRAM")
                messagebox.showerror("Error", "Number Of Rooms only in Numericals")
                print("")
                str_number_of_room = input("ENTER HOW MANY ROOM YOU BOOK [1/2/3 OR SO ON] = ")
                try:
                    number_of_room = int(str_number_of_room)
                    if number_of_room == 0:
                        print("")
                        print("SORRY WE CANCEL YOUR BOOKING BECAUSE YOU ENTER WRONG INFORMATION")
                        print("\nIF YOU BOOK THE HOTEL RE-RUN THE PROGRAM")
                        startup()
                    elif number_of_room != 0:
                        if number_of_days == 0:
                            room_rent_after = room_rent * number_of_room
                        else:
                            room_rent_after = room_rent * number_of_room * number_of_days
                        room_type.append(room)
                        total_price.append(room_rent_after)
                        room_of_type.append(room)
                        room_of_number.append(number_of_room)
                        room_of_price.append(room_rent_after)
                    else:
                        print("INVALID SYNTAX")
                        print("\nPLEASE RE-RUN THE PROGRAM")
                        startup()
                except:
                    print("")
                    print("NUMBER OF ROOM ONLY IN NUMERICAL FORM")
                    print("\nPLEASE RE-RUN THE PROGRAM")
                    messagebox.showerror("Error", "Number Of Rooms only in Numericals")
                    startup()
        else:
            print("WRONG INFORMATION !!!")
        print("")
        sleep(4)
        print("YOUR ROOM RENT IS ", room_rent_after)
        print("")
        print("LOADING.....")
        sleep(4)
        print("")
        # FOR PAYMENT
        payment_method = input("FOR PAYMENT\nPRESS 1 : FOR SCAN QR CODE\nPRESS 2 : FOR NEFT\nPRESS 3 : FOR CASH\n\nCHOOSE YOUR OPTION = ")

        if payment_method == "1":
            print("")
            print("YOU PAY BY SCAN QR CODE")
            print("")
            # PATH LINK
            my_image = PIL.Image.open(r"E:\Python\Cs_Project\UPI qr code.png")
            my_image.show()
        elif payment_method == "2":
            print("")
            print("YOU PAY BY NEFT")
            print("\nDETAILS FOR NEFT GIVEN BELOW :")
            print("\nNAME OF A/C HOLDER = TAJ HOTEL\nBANK NAME = STATE BANK OF INDIA\nACCOUNT NUMBER = 98471002980\nIFSC CODE = SBIN0020852\nBRANCH = NEW DELHI")
            print("")
        elif payment_method == "3":
            print("")
            print("YOU PAY BY CASH")
            print("")
        else:
            print("")
            print("INVALID OPTION SELECTED")
            print("\nPLEASE RE-ENTER THE INFORMATION")
            print("")
            # FOR PAYMENT
            payment_method = input("FOR PAYMENT\nPRESS 1 : FOR SCAN QR CODE\nPRESS 2 : FOR NEFT\nPRESS 3 : FOR CASH\n\nCHOOSE YOUR OPTION = ")
            if payment_method == "1":
                print("")
                print("YOU PAY BY SCAN QR CODE")
                print("")
                # PATH LINK
                my_image = PIL.Image.open(r"E:\Python\Cs_Project\UPI qr code.png")
                my_image.show()
            elif payment_method == "2":
                print("")
                print("YOU PAY BY NEFT")
                print("\nDETAILS FOR NEFT GIVEN BELOW")
                print("\nNAME OF A/C HOLDER = TAJ HOTEL\nBANK NAME = STATE BANK OF INDIA\nACCOUNT NUMBER = 98471002980\nIFSC CODE = SBIN0020852\nBRANCH = NEW DELHI")
                print("")
            elif payment_method == "3":
                print("")
                print("YOU PAY BY CASH")
                print("")
            else:
                print("")
                print("SORRY YOU RE-ENTER THE WRONG INFORMATION")
                print("\nPLEASE RE-RUN THE PROGRAM")
                startup()

        print("LOADING.....")
        sleep(8)
        print("")
        print("DIRECTION OF HOTEL FROM CURRENT LOCATION")
        # PATH LINK
        # location for school
        # webbrowser.open("https://www.google.com/maps/dir/Sbm+Sr.Sec+School,+Block+D,+Karam+Pura,+New+Delhi,+Delhi/Taj+Palace,+New+Delhi,+2,+Sardar+Patel+Marg,+Diplomatic+Enclave,+Chanakyapuri,+New+Delhi,+Delhi+110021/@28.6299701,77.1181172,13z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x390d032fdfc10bf7:0xd998c979666530e4!2m2!1d77.1482251!2d28.664819!1m5!1m1!1s0x390d1da3d0e98c7b:0xf56c1b12e18dd9b!2m2!1d77.1709502!2d28.5951864!3e0?hl=en",new=2)
        # location for  home
        webbrowser.open("https://www.google.com/maps/dir/Blooming+Buds+Public+School,+B+Block,+New+Moti+Nagar,+Karampura+West,+Near+Education+Department+Office,+Phase+1,+Block+B+1,+New+Moti+Nagar,+Moti+Nagar,+New+Delhi,+Delhi+110015,+India/Taj+Palace,+New+Delhi,+Taj+Palace,+Sardar+Patel+Marg,+Diplomatic+Enclave,+Malcha,+New+Delhi,+Delhi/@28.6300416,77.1309956,13z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x390d03aa270562d9:0xe2dc3a221de9b12c!2m2!1d77.1424777!2d28.6643522!1m5!1m1!1s0x390d1da3d0e98c7b:0xf56c1b12e18dd9b!2m2!1d77.1709502!2d28.5951864?hl=en",new=2)
        print("")
        sleep(12)
        print("FOR MORE QUERY GO TO OUR ONLINE WEBSITE")
        print("")
        print("LOADING.....")
        sleep(8)
        # PATH LINK
        webbrowser.open("https://www.tajhotels.com/en-in/taj/taj-palace-new-delhi/", new=2)

        print("")
        sleep(20)
        print("YOUR BOOKING IS RECORDED")
        print("")
        if number_of_room == 1:
            aabb = 1122
            print("YOUR ROOM NUMBER IS ", room_number)
            for_owner_room_number.append(room_number)
        elif number_of_room == 0:
            startup()
        else:
            print("YOUR ROOM NUMBER IS ", room_number)
            for_owner_room_number.append(room_number)
            check_count = 1
            for number_check in range(number_of_room - 1):
                check_count += 1
                if room == "A":
                    room_number = random.randint(1, 20)
                    print("YOUR ROOM NUMBER IS ", room_number)
                    for_owner_room_number.append(room_number)
                elif room == "B":
                    room_number = random.randint(21, 35)
                    print("YOUR ROOM NUMBER IS ", room_number)
                    for_owner_room_number.append(room_number)
                elif room == "C":
                    room_number = random.randint(51, 70)
                    print("YOUR ROOM NUMBER IS ", room_number)
                    for_owner_room_number.append(room_number)
                elif room == "D":
                    room_number = random.randint(70, 100)
                    print("YOUR ROOM NUMBER IS ", room_number)
                    for_owner_room_number.append(room_number)
                elif room == "S":
                    room_number = random.randint(36, 50)
                    print("YOUR ROOM NUMBER IS ", room_number)
                    for_owner_room_number.append(room_number)
                else:
                    print("SORRY !!")

        # Generated a bill number at random
        bill_number_generated = random.randint(5000, 15000)
        bill_numbering.append(bill_number_generated)

        # MAKE A WRITEROWS
        create_writer.writerow(["Room type", "Number of rooms", "Room number", "Total price"])
        create_rec = [room, number_of_room, room_number, room_rent_after]
        create_writer.writerow(create_rec)
        file_check.close()  # THIS STATEMENT CLOSE THE FILE

        # INSERT DATA INTO MYSQL SERVER
        columns_create_1 = "INSERT INTO Booking_info(BILL_NO,NAME,AGE,GENDER,AADHAAR,ADDRESS,MOBILE,NUMBER_ROOMS,ROOM_RENT,ROOM_TYPE,ROOM_NUMBER) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        _input_1 = (
        bill_number_generated, customer_name_UPPER, customer_age, customer_gender_UPPER, customer_aadhaar_details,
        customer_address_UPPER, customer_mobile_number, number_of_room, room_rent_after, room, room_number)
        cursor.execute(columns_create_1, _input_1)
        mydb.commit()

        # INSERT DATA OF DATES INTO MYSQL SERVER
        columns_create_2 = "INSERT INTO Booked_dates(BILL_NO,CHECK_IN_DATE,CHECK_IN_MONTH,CHECK_IN_YEAR,CHECK_OUT_DATE,CHECK_OUT_MONTH,CHECK_OUT_YEAR) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        _input_2 = (bill_number_generated, customer_check_in, month, year, check_out_date, _mon_out_, _yr_out)
        cursor.execute(columns_create_2, _input_2)
        mydb.commit()

        print("")
        print("INVOICE GENERATED.....")
        sleep(3)
        print("\t\t", "-" * 70)
        sleep(1)
        print("\t\t\t\t\t\t\t\t\tBILL AREA")
        sleep(1)
        print("\t\t", "-" * 70)
        sleep(1)
        print("\t\t\t\t\t\t\t\tHOTEL MANAGEMENT SYSTEM")
        sleep(1)
        print("\t\t\t\t\t\t\t\t\tHOTEL TAJ")
        sleep(1)
        a = " +91 11-2611-0202"
        print("\t\t\t\t\t\t\t Phone Number.", a)
        print("")
        sleep(1)
        print("Bill no. :", bill_number_generated)
        sleep(1)
        print("Customer Name :", name_of_customer[0])
        sleep(1)
        print("Phone Number. :", mobile_of_customer[0])
        print("")
        sleep(1)

        # COMPARE ALL THE VARIABLE TO MAKE ONE VARIABLE FOR CHECK-IN AND CHECK-OUT
        checkin_invoice = day_of_checkin[0], month_of_checkin[0], year_of_checkin[0]
        checkout_invoice = day_of_checkout[0], month_of_checkout[0], year_of_checkout[0]

        if choose_month_upper == "Y" or choose_month_upper == "YES":
            list1 = [name_of_customer[0], " ", " ", " ", " ", " ", " "]
            list2 = [room_of_type[0], "", " ", " ", " ", " ", " "]
            list3 = [room_of_number[0], " ", " ", " ", " ", " ", " "]
            list4 = [checkin_invoice, " ", " ", " ", " ", " ", " "]
            list5 = [checkout_invoice, " ", " ", " ", " ", " ", " "]
            list6 = [number_of_days, " ", " ", " ", " ", " ", " "]
            list7 = [room_of_price[0], " ", " ", " ", " ", " ", " "]
            table = PrettyTable(
                ["Name", "Room Type", "Number of Rooms", "Check-In", "Check-Out", "Number of Days", "Price"])
            for customer_table in range(0, 6):
                table.add_row(
                    [list1[customer_table], list2[customer_table], list3[customer_table], list4[customer_table],
                     list5[customer_table], list6[customer_table], list7[customer_table]])
            print(table)
            print("\t" * 10, "TOTAL PRICE :", room_of_price[0])
        elif choose_month_upper == "N" or choose_month_upper == "NO":
            list1 = [name_of_customer[0], " ", " ", " ", " ", " ", " "]
            list2 = [room_of_type[0], "", " ", " ", " ", " ", " "]
            list3 = [room_of_number[0], " ", " ", " ", " ", " ", " "]
            list4 = [checkin_invoice, " ", " ", " ", " ", " ", " "]
            list5 = [checkout_invoice, " ", " ", " ", " ", " ", " "]
            list6 = [number_of_days, " ", " ", " ", " ", " ", " "]
            #list7 = [room_of_price[0]," "," "," "," "," "," "]
            table = PrettyTable(["Name", "Room Type", "Number of Rooms", "Check-In", "Check-Out", "Number of Days"])
            for customer_table in range(0, 5):
                table.add_row(
                    [list1[customer_table], list2[customer_table], list3[customer_table], list4[customer_table],
                     list5[customer_table], list6[customer_table], ])
            print(table)
            print("\t" * 7, "TOTAL PRICE :", room_of_price[0])
        else:
            aabb = 11222
        print("\t" * 8, "THANK YOU !!\n", "\t" * 8, "VISITING AGAIN")

        sleep(2)
        # PATH LINK
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\python_thankyou.png")
        my_image.show()

        startup()

    except:
        print("")
        print("WRONG CHOICE")
        messagebox.showerror("Showerror", "Error")
        startup()

def check_in_or_out():
    global customer_check_in, check_out_date, month, month_out

    # FOR CHECK - IN DATE
    print("")
    print("\t\t", "=" * 30, " CHECK - IN ", "=" * 32)
    print("")

    # FOR CURENT TIME
    time.time
    present_time = time.asctime()
    str_month = str(input("ENTER THE MONTH OF BOOKING [IN NUMBERS] = "))
    try:
        month = int(str_month)
        if 1 <= month <= 12:
            print("")
            UPPER_checkin_year = "Y"
            if UPPER_checkin_year == "Y" or UPPER_checkin_year == "YES":
                year_check = str(input("ENTER THE YEAR [2021/2022/2023] = "))
                print("")
                if year_check == "2021":
                    year = 2021
                    current_time = datetime.datetime.now()
                    month_present = current_time.month
                    if month < month_present:  # THIS IS A CURRENT MONTH
                        print("")
                        print("SORRY YOU ENTER WRONG INFORMATION")
                        print("\nYOUR MONTH WHICH YOU ENTER ABOVE IS PREVIOUS BUT WE BOOKED THE ROOM FOR ADVANCE")
                        print("\nPLEASE RE-RUN THE PROGRAM")
                        startup()
                    else:
                        aabb = 10
                elif year_check == "2022":
                    year = 2022
                elif year_check == "2023":
                    year = 2023
                else:
                    print("INVALID YEAR ENTERED !!")
                    print("\nRE-RUN THE PROGRAM")
                    startup()
                print("LOADING.....")
                sleep(3)
                print("")
                year_for_append = int(year_check)
                calendar.setfirstweekday(calendar.SUNDAY)
                yr = calendar.month(year, month)
                print("THIS IS THE CALENDAR OF MONTH ", month)
                print("")
                print(yr)
                # MONTH HAVING 31 DAYS
                if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    print("")
                    str_customer_check_in = str(input("ENTER THE DATE OF BOOKING = "))
                    print("")
                    print("LOADING.....")
                    sleep(3)
                    try:
                        customer_check_in = int(str_customer_check_in)

                        # THIS IS FOR PRESENT YEAR
                        current_time = datetime.datetime.now()
                        year_present = current_time.year
                        if year == year_present:
                            # THIS IS FOR PRESENT MONTH
                            month_present = current_time.month
                            if month == month_present:
                                # THIS IS FOR TODAY'S DATE
                                date_today = current_time.day
                                if date_today > customer_check_in:
                                    print("")
                                    print("INVALID DATE ENTERED")
                                    print("THIS DATE IS NOT POSSIBLE IN FUTURE")
                                    print("PLEASE RE-RUN THE PROGRAM")
                                    startup()
                                else:
                                    aabb = 10
                            else:
                                aabb = 12
                        else:
                            aabb = 15

                        if 1 <= customer_check_in <= 31:
                            print("")
                            print("OKAY YOUR CHECK-IN DATE HAS BEEN RECORDED")
                            if customer_check_in == 0:
                                print("")
                                print("SORRY RIGHT NOW WE HAVE NO ROOM FOR BOOKING IN THIS DATE\nFOR MORE INFORMATION GO TO OUR ONLINE WEBSITE")
                                # PATH LINK
                                webbrowser.open("https://www.tajhotels.com/en-in/taj/taj-palace-new-delhi/", new=2)
                                startup()
                            else:
                                print("")
                                print("YOUR CHECK-IN DATE IS =", customer_check_in, "/", month, "/", year)
                                print("")

                                checkin_month.append(month)
                                checkin_date.append(customer_check_in)
                                # append function

                                try:
                                    year_in.append(year)

                                except:
                                    print("")
                                    print("IT SHOW ERROR")

                        elif customer_check_in >= 32:
                            print("")
                            print("THE MAXIMUM DAYS IN MONTH WHICH YOU ENTER IS ONLY 31 \nBUT YOU ENTER MORE THAN 31 DAYS")
                            print("\nRE-RUN THE PROGRAM")
                            startup()
                        else:
                            print("INVALID SYNTAX")
                            startup()
                    except:
                        print("")
                        print("THE DATE ONLY IN NUMBER")
                        print("\nRE-RUN THE PROGRAM")
                        messagebox.showerror("Error", "Date Only in Numbers")
                        startup()
                # MONTH HAVING 30 DAYS
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    print("")
                    str_customer_check_in = str(input("ENTER THE DATE OF BOOKING = "))
                    print("")
                    print("LOADING.....")
                    sleep(3)
                    print("")
                    try:
                        customer_check_in = int(str_customer_check_in)

                        # THIS IS FOR PRESENT YEAR
                        current_time = datetime.datetime.now()
                        year_present = current_time.year
                        if year == year_present:
                            # THIS IS FOR PRESENT MONTH
                            month_present = current_time.month
                            if month == month_present:
                                # THIS IS FOR TODAY'S DATE
                                date_today = current_time.day
                                if date_today > customer_check_in:
                                    print("")
                                    print("INVALID DATE ENTERED")
                                    print("THIS DATE IS NOT POSSIBLE IN FUTURE")
                                    print("PLEASE RE-RUN THE PROGRAM")
                                    startup()
                                else:
                                    aabb = 10
                            else:
                                aabb = 12
                        else:
                            aabb = 15

                        if 1 <= customer_check_in <= 30:
                            print("OKAY YOUR CHECK-IN DATE HAS BEEN RECORDED")
                            if customer_check_in == 0:
                                print("")
                                print("SORRY RIGHT NOW WE HAVE NO ROOM FOR BOOKING IN THIS DATE\nFOR MORE INFORMATION GO TO OUR ONLINE WEBSITE")
                                startup()
                            else:
                                print("")
                                print("YOUR CHECK-IN DATE IS =", customer_check_in, "/", month, "/", year)
                                print("")

                                checkin_month.append(month)
                                # checkin_year.append(year)
                                checkin_date.append(customer_check_in)
                                # append function

                                try:
                                    year_in.append(year)

                                except:
                                    print("")
                                    print("IT SHOW ERROR")

                        elif customer_check_in >= 31:
                            print("")
                            print(
                                "THE MAXIMUM DAYS IN MONTH WHICH YOU ENTER IS ONLY 30\nBUT YOU ENTER MORE THAN 30 DAYS")
                            print("\nRE-RUN THE PROGRAM")
                            startup()
                        else:
                            print("INVALID SYNTAX")
                            startup()
                    except:
                        print("")
                        print("THE DATE ONLY IN NUMBER")
                        print("\nRE-RUN THE PROGRAM")
                        messagebox.showerror("Error", "Date Only in Numbers")
                        startup()
                # MONTH HAVING 28 DAYS
                elif month == 2:
                    print("")
                    str_customer_check_in = str(input("ENTER THE DATE OF BOOKING = "))
                    print("")
                    print("LOADING.....")
                    sleep(3)
                    print("")
                    try:
                        customer_check_in = int(str_customer_check_in)

                        # THIS IS FOR PRESENT YEAR
                        current_time = datetime.datetime.now()
                        year_present = current_time.year
                        if year == year_present:
                            # THIS IS FOR PRESENT MONTH
                            month_present = current_time.month
                            if month == month_present:
                                # THIS IS FOR TODAY'S DATE
                                date_today = current_time.day
                                if date_today > customer_check_in:
                                    print("")
                                    print("INVALID DATE ENTERED")
                                    print("THIS DATE IS NOT POSSIBLE IN FUTURE")
                                    print("PLEASE RE-RUN THE PROGRAM")
                                    startup()
                                else:
                                    aabb = 10
                            else:
                                aabb = 12
                        else:
                            aabb = 15

                        if 1 <= customer_check_in <= 30:
                            print("")
                            print("OKAY YOUR CHECK-IN DATE HAS BEEN RECORDED")
                            if customer_check_in == 0:
                                print("")
                                print("SORRY RIGHT NOW WE HAVE NO ROOM FOR BOOKING IN THIS DATE\nFOR MORE INFORMATION GO TO OUR ONLINE WEBSITE")
                                startup()
                            else:
                                print("")
                                print("YOUR CHECK-IN DATE IS =", customer_check_in, "/", month, "/", year)
                                print("")

                                checkin_month.append(month)
                                # checkin_year.append(year)
                                checkin_date.append(customer_check_in)
                                # append function

                                try:
                                    year_in.append(year)

                                except:
                                    print("")
                                    print("IT SHOW ERROR")

                        elif customer_check_in >= 31:
                            print("")
                            print("THE MAXIMUM DAYS IN MONTH FEBURARY IS ONLY 28 \nBUT YOU ENTER MORE THAN 28 DAYS")
                            print("\nRE-RUN THE PROGRAM")
                            startup()
                        else:
                            print("")
                            print("INVALID SYNTAX")
                            startup()
                    except:
                        print("")
                        print("THE DATE ONLY IN NUMBER")
                        print("\nRE-RUN THE PROGRAM")
                        messagebox.showerror("Error", "Date Only in Numbers")
                        startup()
                else:
                    print("")
                    print("INVALID MONTH ENTER")
                    print("\nRE-RUN THE PROGRAM")
                    startup()

            elif UPPER_checkin_year == "N" and "NO":
                print("")
                print("\nTHIS IS AN HIGHLY ADVANCE BOOKING")
                print("\nSORRY WE CAN'T BOOK HOTEL ROOM FOR ADVANCE THREE YEAR BEFORE")
                print("\nPLEASE RE - RUN THE PROGRAM")
            else:
                print("\nINVALID CHOICE")
                startup()
        elif month >= 13:
            print("")
            print("LOADING.....")
            sleep(3)
            messagebox.showerror("Error", "There are Only 12 Month in a Year")
            print("\nTHERE ARE ONLY 12 MONTHS IN ONE YEAR")
            print("\nPLEASE RE - RUN THE PROGRAM")
            startup()
        else:
            print("\nINVALID SYNTAX")
            startup()
    except:
        print("\nENTER MONTH ONLY IN NUMBERS \nBUT YOU ENTER IN ALPHABETS\nPLEASE RE - RUN THE PROGRAM")
        messagebox.showerror("Error", "Month Only in Numbers")

        startup()

    # FOR CHECK - OUT DATE

    print("")
    print("\t\t", "=" * 30, " CHECK - OUT ", "=" * 32)
    print("")

    print("ARE YOU CHECK-OUT IN MONTH", month, " [Y/N]")
    print("")
    choose_month = input("ENTER YOUR CHOICE [Y/N] = ")
    choose_month_upper = choose_month.upper()
    if choose_month_upper == "Y" or choose_month_upper == "YES":  # same month of check-in as well as check-out
        try:
            print("")
            checkout_year_Y = "Y"
            if checkout_year_Y == "Y":
                print("LOADING.....")
                sleep(3)
                print("")
                calendar.setfirstweekday(calendar.SUNDAY)
                yr = calendar.month(year, month)
                print("THIS IS THE CALENDAR OF MONTH ", month)
                print("")
                print(yr)
                print("")
                str_check_out_date = input("ENTER THE CHECK_OUT DATE = ")
                try:
                    check_out_date = int(str_check_out_date)
                    print("")
                    print("LOADING.....")
                    sleep(3)
                    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                        if 1 <= check_out_date <= 31:
                            if check_out_date < customer_check_in:
                                print("")
                                print("YOU ENTERED WRONG DATE ")
                                print("")
                                print("YOUR CHECK-IN DATE IS ", customer_check_in)
                                print("")
                                print("AND YOUR CHECK-OUT DATE IS ", check_out_date)
                                print("")
                                print("YOUR CHECK-OUT DATE IS LESS THAN CHECK-IN DATE WHICH IS NOT POSSIBLE")
                                print("\n", check_out_date, "<", customer_check_in)
                                print("")
                                print("IN STARTING YOU ENTERED YOU CHECK-IN AND CHECK-OUT IN SAME MONTH")
                                print("")
                                print("PLEASE RE-RUN THE PROGRAM")
                                startup()
                            else:
                                print("")
                                print("YOUR CHECK-OUT DATE WILL BE RECORDED")
                                print("")
                                number_of_days = check_out_date - customer_check_in
                                print("YOU STAY IN HOTEL FOR", number_of_days, "DAYS")
                                print("")
                                print("OKAY!! PLEASE FILL SOME OTHER DETAILS TO BOOK THE ROOM")
                                print("")
                                sleep(4)
                                print("YOUR CHECK - IN DATE IS ", customer_check_in, "/", month, "/", year)
                                print("")
                                print("YOUR CHECK - OUT DATE IS ", check_out_date, "/", month, "/", year)

                                checkout_date.append(check_out_date)
                                checkout_month.append(month)
                                # append function

                                try:
                                    out_year.append(year)
                                    month_out = month
                                    year_out = year

                                except:
                                    print("")
                                    print("IT SHOW ERROR")
                        else:
                            print("")
                            print("YOUR MONTH OF BOOKING IS ", month)
                            print("\nIN THIS MONTH THERE ARE ONLY 31 DAYS BUT YOU ENTER MORE THAN THAT")
                            print("\nPLEASE RE-RUN THE PROGRAM")
                            startup()
                    elif month == 4 or month == 6 or month == 9 or month == 11:
                        if 1 <= check_out_date <= 30:
                            if check_out_date < customer_check_in:
                                print("")
                                print("YOU ENTERED WRONG DATE")
                                print("")
                                print("YOUR CHECK-IN DATE IS ", customer_check_in)
                                print("")
                                print("AND YOUR CHECK-OUT DATE IS ", check_out_date)
                                print("")
                                print("YOUR CHECK-OUT DATE IS LESS THAN CHECK-IN DATE WHICH IS NOT POSSIBLE")
                                print("\n", check_out_date, "<", customer_check_in)
                                print("")
                                print("IN STARTING YOU ENTERED YOU CHECK-IN AND CHECK-OUT IN SAME MONTH")
                                print("")
                                print("PLEASE RE-RUN THE PROGRAM")
                                startup()
                            else:
                                print("")
                                print("YOUR CHECK-OUT DATE WILL BE RECORDED")
                                print("")
                                number_of_days = check_out_date - customer_check_in
                                print("YOU STAY IN HOTEL FOR", number_of_days, "DAYS")
                                print("")
                                print("OKAY!! PLEASE FILL SOME OTHER DETAILS TO BOOK THE ROOM")
                                print("")
                                sleep(4)
                                print("YOUR CHECK - IN DATE IS ", customer_check_in, "/", month, "/", year)
                                print("")
                                print("YOUR CHECK - OUT DATE IS ", check_out_date, "/", month, "/", year)

                                checkout_date.append(check_out_date)
                                checkout_month.append(month)
                                # append function

                                try:
                                    out_year.append(year)
                                    month_out = month
                                    year_out = year

                                except:
                                    print("")
                                    print("IT SHOW ERROR")
                        else:
                            print("")
                            print("YOUR MONTH OF BOOKING IS ", month)
                            print("\nIN THIS MONTH THERE ARE ONLY 30 DAYS BUT YOU ENTER MORE THAN THAT")
                            print("\nPLEASE RE-RUN THE PROGRAM")
                            startup()
                    elif month == 2:
                        if 1 <= check_out_date <= 28:
                            if check_out_date < customer_check_in:
                                print("")
                                print("YOU ENTERED WRONG DATE")
                                print("")
                                print("YOUR CHECK-IN DATE IS ", customer_check_in)
                                print("")
                                print("AND YOUR CHECK-OUT IS ", check_out_date)
                                print("")
                                print("YOUR CHECK-OUT DATE IS LESS THAN CHECK-IN DATE WHICH IS NOT POSSIBLE")
                                print("\n", check_out_date, "<", customer_check_in)
                                print("")
                                print("IN STARTING YOU ENTERED YOU CHECK-IN AND CHECK-OUT IN SAME MONTH")
                                print("")
                                print("PLEASE RE-RUN THE PROGRAM")
                                startup()
                            else:
                                print("")
                                print("YOUR CHECK-OUT DATE WILL BE RECORDED")
                                print("")
                                number_of_days = check_out_date - customer_check_in
                                print("YOU STAY IN HOTEL FOR", number_of_days, "DAYS")
                                print("")
                                print("OKAY!! PLEASE FILL SOME OTHER DETAILS TO BOOK THE ROOM")
                                print("")
                                sleep(4)
                                print("YOUR CHECK - IN DATE IS ", customer_check_in, "/", month, "/", year)
                                print("")
                                print("YOUR CHECK - OUT DATE IS ", check_out_date, "/", month, "/", year)

                                checkout_date.append(check_out_date)
                                checkout_month.append(month)
                                # append function

                                try:
                                    out_year.append(year)
                                    month_out = month
                                    year_out = year

                                except:
                                    print("")
                                    print("IT SHOW ERROR")

                        else:
                            print("")
                            print("YOUR MONTH OF BOOKING IS ", month)
                            print("\nIN THIS MONTH THERE ARE ONLY 28 DAYS BUT YOU ENTER MORE THAN THAT")
                            print("\nPLEASE RE-RUN THE PROGRAM")
                            startup()
                    else:
                        print("INVALID YEAR ENTERED")
                        print("\nPLEASE RE-RUN THE PROGRAM")
                        startup()
                except:
                    print("INVALID CHECK-OUT DATE ENTERED ")
                    print("\nDATE ONLY IN NUMBERS")
                    print("\nPLEASE RE-RUN THE PROGRAM")
                    messagebox.showerror("Error", "Date Only in Numbers")
                    startup()
            else:
                print("WRONG CHOICE")
                print("\nPLEASE RE-RUN THE PROGRAM")
                startup()
        except:
            print("")
            print("INVALID CHOICE")
            print("\nPLEASE RE - RUN THE PROGRAM")
            messagebox.showerror("Error", "Invalid Choice")
            startup()

    elif choose_month_upper == "N" or choose_month_upper == "NO":  # different month of check-in and check-out
        print("")
        str_month = str(input("ENTER THE MONTH FOR CHECK-OUT [IN NUMBERS] = "))
        try:
            month_out = int(str_month)

            year_present = current_time.year  # PRESENT YEAR
            month_present = current_time.month  # PRESENT MONTH
            date_today = current_time.day  # TODAY DATE

            print("")

            if 1 <= month_out <= 12:
                checkout_year = str(input("ENTER THE YEAR FOR CHECK - OUT [2021/2022/2023] = "))
                if checkout_year == "2021":
                    year_out = 2021
                    checkout_year_yes = "Y"
                    current_time = datetime.datetime.now()
                    month_present = current_time.month
                    if month_out < month_present:  # THIS IS A CURRENT MONTH
                        print("")
                        print("SORRY YOU ENTER WRONG INFORMATION")
                        print("\nYOUR MONTH WHICH YOU ENTER ABOVE IS PREVIOUS BUT WE BOOKED THE ROOM FOR ADVANCE")
                        print("\nPLEASE RE-RUN THE PROGRAM")
                        startup()
                    else:
                        aabb = 10
                elif checkout_year == "2022":
                    year_out = 2022
                    checkout_year_yes = "Y"
                elif checkout_year == "2023":
                    year_out = 2023
                    checkout_year_yes = "Y"
                else:
                    print("")
                    print("INVALID SYNTAX")
                    print("\nPLEASE RE-RUN THE PROGRAM")
                    startup()
                if month_out == month:
                    if year_out == year:
                        print("")
                        print(
                            "SORRY IN ABOVE STATEMENT YOU ENTER YOU CHECK-OUT THE HOTEL ROOM IN ANOTHER MONTH OF CHECK-IN")
                        print("\nBUT HERE YOU ENTER THE SAME MONTH AND SAME YEAR")
                        print("\nPLEASE RE-RUN TE PROGRAM")
                        startup()
                    else:
                        aabb = 0
                else:
                    aabb = 1

                if checkout_year_yes == "Y":
                    print("")
                    if year_out >= year:  # CHECK-OUT YEAR >= CHECK-IN YEAR
                        print("LOADING.....")
                        sleep(3)
                        print("")
                        calendar.setfirstweekday(calendar.SUNDAY)
                        yr = calendar.month(year_out, month_out)
                        print("THIS IS THE CALENDAR OF MONTH ", month_out)
                        print("")
                        print(yr)
                        print("")
                        str_check_out_date = input("ENTER THE CHECK-OUT DATE = ")
                        try:
                            check_out_date = int(str_check_out_date)
                            print("")
                            print("LOADING.....")
                            sleep(3)
                            print("")

                            # DAY CALCULATOR
                            firstdate = date(year, month, customer_check_in)
                            seconddate = date(year_out, month_out, check_out_date)
                            number_of_days = seconddate - firstdate

                            # MONTH OF 31 DAYS
                            if month_out == 1 or month_out == 3 or month_out == 5 or month_out == 7 or month_out == 8 or month_out == 10 or month_out == 12:
                                if 1 <= check_out_date <= 31:
                                    print("")
                                    print("YOUR CHECK-OUT DATE WILL BE RECORDED")
                                    print("")
                                    print("YOU STAY IN HOTEL FOR", number_of_days, "DAYS")
                                    print("")
                                    print("OKAY!! PLEASE FILL SOME OTHER DETAILS TO BOOK THE ROOM")
                                    print("")
                                    sleep(4)
                                    print("YOUR CHECK - IN DATE IS ", customer_check_in, "/", month, "/", year)
                                    print("")
                                    print("YOUR CHECK - OUT DATE IS ", check_out_date, "/", month_out, "/", year_out)

                                    checkout_date.append(check_out_date)
                                    checkout_month.append(month_out)
                                    # append function
                                    try:
                                        out_year.append(year_out)
                                    except:
                                        print("")
                                        print("IT SHOWS A ERROR")

                                else:
                                    print("")
                                    print("YOUR MONTH OF BOOKING IS ", month)
                                    print("\nIN THIS MONTH THERE ARE ONLY 31 DAYS BUT YOU ENTER MORE THAN THAT")
                                    print("\nPLEASE RE-RUN THE PROGRAM")
                                    startup()
                            # MONTH OF 30 DAYS
                            elif month_out == 4 or month_out == 6 or month_out == 9 or month_out == 11:
                                if 1 <= check_out_date <= 30:
                                    print("")
                                    print("YOUR CHECK-OUT DATE WILL BE RECORDED")
                                    print("")
                                    print("YOU STAY IN HOTEL FOR", number_of_days, "DAYS")
                                    print("")
                                    print("OKAY!! PLEASE FILL SOME OTHER DETAILS TO BOOK THE ROOM")
                                    print("")
                                    sleep(4)
                                    print("YOUR CHECK - IN DATE IS ", customer_check_in, "/", month, "/", year)
                                    print("")
                                    print("YOUR CHECK - OUT DATE IS ", check_out_date, "/", month_out, "/", year_out)

                                    checkout_date.append(check_out_date)
                                    checkout_month.append(month_out)
                                    # append function
                                    try:
                                        out_year.append(year_out)
                                    except:
                                        print("")
                                        print("IT SHOWS A ERROR")

                                else:
                                    print("")
                                    print("YOUR MONTH OF BOOKING IS ", month)
                                    print("\nIN THIS MONTH THERE ARE ONLY 30 DAYS BUT YOU ENTER MORE THAN THAT")
                                    print("\nPLEASE RE-RUN THE PROGRAM")
                                    startup()
                            # MONTH OF 28 DAYS
                            elif month_out == 2:
                                if 1 <= check_out_date <= 28:
                                    print("")
                                    print("YOUR CHECK-OUT DATE WILL BE RECORDED")
                                    print("")
                                    print("YOU STAY IN HOTEL FOR", number_of_days, "DAYS")
                                    print("")
                                    print("OKAY!! PLEASE FILL SOME OTHER DETAILS TO BOOK THE ROOM")
                                    print("")
                                    sleep(4)
                                    print("YOUR CHECK - IN DATE IS ", customer_check_in, "/", month, "/", year)
                                    print("")
                                    print("YOUR CHECK - OUT DATE IS ", check_out_date, "/", month_out, "/", year_out)

                                    checkout_date.append(check_out_date)
                                    checkout_month.append(month_out)
                                    # append function
                                    try:
                                        out_year.append(year_out)
                                    except:
                                        print("")
                                        print("IT SHOWS A ERROR")

                                else:
                                    print("")
                                    print("YOUR MONTH OF BOOKING IS ", month)
                                    print("\nIN THIS MONTH THERE ARE ONLY 28 DAYS BUT YOU ENTER MORE THAN THAT")
                                    print("\nPLEASE RE-RUN THE PROGRAM")
                                    startup()
                            else:
                                print("")
                                print("INVALID SYNTAX")
                                print("\nPLEASE RE-RUN THE PROGRAM")
                                startup()
                        except:
                            print("")
                            print("INVALID DATE ENTERED ")
                            print("\nDATE ONLY IN NUMBERS")
                            print("\nPLEASE RE-RUN THE PROGRAM")
                            messagebox.showerror("Error", "Date Only in Numbers")
                            startup()
                    else:
                        print("")
                        print("THIS CONDITION IS NOT POSSIBLE")
                        print("\nINVALID SYNTAX")
                        print("\nPLEASE RE-RUN THE PROGRAM")
                        startup()
                else:
                    print("")
                    print("INVALD SYNTAX")
                    print("\nPLEASE RE-RUN THE PROGRAM")
                    startup()
            else:
                print("")
                print("YEAR ONLY HAVE 12 MONTHS BUT YOU ENTER MORE THAN THAT")
                print("\nPLEASE RE-RUN THE PROGRAM")
                startup()
        except:
            print("")
            print("MONTH ONLY IN NUMERICAL FORM")
            print("\nPLEASE RE-RUN THE PROGRAM")
            messagebox.showerror("Error", "Month Only in Numbers")
            startup()
    else:
        print("")
        print("INVALID SYNTAX")
        print("\nPLEASE RE-RUN THE PROGRAM")
        startup()

    # FOR BILL INVOICE MAKE ONE LIST
    day_of_checkin.append(customer_check_in)  # APPEND IN LIST CHECK-IN DATE
    month_of_checkin.append(month)  # APPEND IN LIST CHECK-IN MONTH
    year_of_checkin.append(year)  # APPEND IN LIST CHECK-IN YEAR
    day_of_checkout.append(check_out_date)  # APPEND IN LIST CHECK-OUT DATE
    month_of_checkout.append(month_out)  # APPEND IN LIST CHECK-OUT MONTH
    year_of_checkout.append(year_out)  # APPEND IN LIST CHECK-OUT YEAR

    _mon_out_ = month_out
    _yr_out = year_out

    return choose_month_upper, number_of_days, customer_check_in, month, year, check_out_date, _mon_out_, _yr_out


def display_room():
    # DISPLAY IMAGE OF THE ROOM
    print("")
    print("\t\t\t    ", "=" * 20, "DISPLAY ROOM", "=" * 20)
    # PATH LINK
    my_image = PIL.Image.open(r"E:\Python\Cs_Project\collage_room_1.jpeg")
    my_image.show()
    my_image = PIL.Image.open(r"E:\Python\Cs_Project\collage_room_2.jpeg")
    my_image.show()
    my_image = PIL.Image.open(r"E:\Python\Cs_Project\collage_room_3.jpeg")
    my_image.show()

    print("")
    print("CHOOSE THE ROOM :\n\nPRESS A = TO BOOK A CATEGORY ROOM\nPRESS B = TO BOOK B CATEGORY ROOM\nPRESS C = TO BOOK C CATEGORY ROOM\nPRESS D = TO BOOK D CATEGORY ROOM\nPRESS S = TO BOOK SPECIAL DELUXE CATEGORY ROOM")
    print("")
    print("PRICE LIST OF ROOMS :\n\nROOMS A : 4000\nROOMS B : 3000\nROOMS C : 2500\nROOMS D : 1500\nROOMS S : 7000")
    print("\nALL ROOMS ARE AIR CONDITIONER\nBOOK ACCORDING YOUR CHOICE\n")
    roomX = str(input("ENTER THE CATEGORY OF THE ROOM = "))
    room = roomX.upper()

    # THIS IS FOR A CATEGORY OF ROOM
    if room == "A":
        # PATH LINK
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\roomA_1.jpeg")
        my_image.show()
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\roomA_2.jpeg")
        my_image.show()
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\roomA_3.jpeg")
        my_image.show()
        room_rent = 4000  # ROOM RENT FOR ONE DAY
        room_number = random.randint(1, 20)

    # THIS IS FOR B CATEGORY OF ROOM
    elif room == "B":
        # PATH LINK
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\roomB_1.png")
        my_image.show()
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\roomB_2.png")
        my_image.show()
        room_rent = 3000  # ROOM RENT FOR ONE DAY
        room_number = random.randint(21, 35)

    # THIS IS FOR C CATEGORY OF ROOM
    elif room == "C":
        # PATH LINK
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\roomC_1.jpeg")
        my_image.show()
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\roomC_2.jpeg")
        my_image.show()
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\roomC_3.jpeg")
        my_image.show()
        room_rent = 2500  # ROOM RENT FOR ONE DAY
        room_number = random.randint(51, 70)

    # THIS IS FOR D CATEGORY OF ROOM
    elif room == "D":
        # PATH LINK
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\roomD.png")
        my_image.show()
        room_rent = 1500  # ROOM RENT FOR ONE DAY
        room_number = random.randint(70, 100)

    # THIS IS FOR SPECIAL CATEGORY OF ROOM [DELUXE]
    elif room == "S":
        # PATH LINK
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\special_room_deluxe_1.jpeg")
        my_image.show()
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\special_room_deluxe_2.jpeg")
        my_image.show()
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\special_room_deluxe_3.jpeg")
        my_image.show()
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\special_room_deluxe_4.jpeg")
        my_image.show()
        my_image = PIL.Image.open(r"E:\Python\Cs_Project\special_room_deluxe_5.jpeg")
        my_image.show()
        room_rent = 7000  # ROOM RENT FOR ONE DAY
        room_number = random.randint(36, 50)

    # ELSE PART FOR USER TO RE-RUN THE PROGRAM
    else:
        print("\nINVALID SYNTAX")
        print("\nPLEASE RE-RUN THE PROGRAM")
        startup()

    return room_rent, room, room_number

def name_image_display():
    # FOR WAITING ROOM
    def waiting_room():
        root = Tk()
        root.title("Background image")
        root.geometry("1024x683")

        framehome = Frame(root, bg="red")
        framehome.pack(fill=BOTH, expand=True)

        imagehome = PhotoImage(file="waiting area.png")
        label1 = ttk.Label(framehome, image=imagehome)
        label1.pack(fill=BOTH, expand=True)

        labela = Label(label1, text="WAITING ROOM", fg="black", font=("calibri", 30, "bold"))
        labela.pack()

        root.mainloop()

    # FOR HOTEL NAME DISPLAY
    def Taj():
        root = Tk()
        root.title("Background image")
        root.geometry("1280x600")

        framehome = Frame(root, bg="red")
        framehome.pack(fill=BOTH, expand=True)

        imagehome = PhotoImage(file="taj_hotel.png")
        label1 = ttk.Label(framehome, image=imagehome)
        label1.pack(fill=BOTH, expand=True)

        labela = Label(label1, text="HOTEL IMAGE DISPLAY", fg="black", font=("calibri", 30, "bold"))
        labela.pack()

        root.mainloop()

    # FOR LOBBY
    def lobby():
        root = Tk()
        root.title("Background image")
        root.geometry("1024x683")

        framehome = Frame(root, bg="red")
        framehome.pack(fill=BOTH, expand=True)

        imagehome = PhotoImage(file="lobby.png")
        label1 = ttk.Label(framehome, image=imagehome)
        label1.pack(fill=BOTH, expand=True)

        labela = Label(label1, text="LOBBY", fg="black", font=("calibri", 30, "bold"))
        labela.pack()

        root.mainloop()

    # FOR GARDEN
    def graden():
        root = Tk()
        root.title("Background image")
        root.geometry("1024x683")

        framehome = Frame(root, bg="red")
        framehome.pack(fill=BOTH, expand=True)

        imagehome = PhotoImage(file="graden.png")
        label1 = ttk.Label(framehome, image=imagehome)
        label1.pack(fill=BOTH, expand=True)

        labela = Label(label1, text="GARDEN", fg="black", font=("calibri", 30, "bold"))
        labela.pack()

        root.mainloop()

    for i in range(100):
        print("")
        print("\t\t", "=" * 26, "CHECK HOTEL IMAGES", "=" * 30)
        print("")
        print("\tPRESS 1 = WAITING ROOM\n\tPRESS 2 = FOR HOTEL NAME\n\tPRESS 3 = FOR LOBBY\n\tPRESS 4 = FOR GARDEN\n\tPRESS 5 = TO GO TO MAIN MENU\n\tPRESS 0 = FOR QUIET THE WINDOW")
        print("")
        choice = str(input("\tENTER YOUR CHOICE = "))
        if choice == "1":
            waiting_room()
            print("")
        elif choice == "2":
            Taj()
            print("")
        elif choice == "3":
            lobby()
            print("")
        elif choice == "4":
            graden()
            print("")
        elif choice == "5":
            print("")
            main_menu()
        elif choice == "0":
            quit()
        else:
            print("")
            print("INVALID CHOICE")
            print("")


def indian_menu_card():
    my_image = PIL.Image.open(r"E:\Python\Cs_Project\restaurant_1.jpeg")
    my_image.show()
    my_image = PIL.Image.open(r"E:\Python\Cs_Project\restaurant_2.jpeg")
    my_image.show()
    sleep(2)
    _Menu_card_.menu_card()  # CALLING OUR OWN CREATING LIBRARY
    print("")
    sleep(2)
    startup()

def hotel_brochure():
    webbrowser.open("E:\\Python\\Cs_Project\\Taj-PalaceNew-Delhi-Hotel-Presentation.pdf")
    print("LOADING.....")
    sleep(4)
    startup()

def hotel_policies():
    print("")
    print("\t\t   ", "=" * 26, "HOTEL POLICIES", "=" * 30)
    print("")
    print("")
    sleep(4)

    def Hotel_Amenities():
        _Hotel_policies_.ammenities()

    def Hotel_Policies():
        _Hotel_policies_.policies()

    def Hotel_Highlights():
        _Hotel_policies_.highlights()

    def Hotel_Awards():
        _Hotel_policies_.awards()

    policy_choice = input("THESE ARE OPTIONS :\n\nPRESS 1 : TO CHECK AMENITIES\nPRESS 2 : TO CHECK HOTEL POLICIES\nPRESS 3 : TO CHECK HOTEL HIGHLIGHTS\nPRESS 4 : TO CHECK HOTEL AWARDS\nPRESS 0 : TO EXIT\n\nENTER YOUR CHOICE = ")
    if policy_choice == "1":
        Hotel_Amenities()
    elif policy_choice == "2":
        Hotel_Policies()
    elif policy_choice == "3":
        Hotel_Highlights()
    elif policy_choice == "4":
        Hotel_Awards()
    elif policy_choice == "0":
        print("")
        win_exit_str = str(input("ARE YOU SURE YOU EXIT THE PROGRAM !! [Y/N] = "))
        win_exit = win_exit_str.upper()
        if win_exit == "Y" or win_exit == "YES":
            exit()
        elif win_exit == "N" or win_exit == "NO":
            startup()
        else:
            startup()
    else:
        print("\nINVALID ENTRY ENTERED")
        startup()
    hotel_policies()

def owner_info():
    print("")
    print("\t\t", "-" * 26, "OWNER INFORMATION", "-" * 30)
    print("")
    print("WELCOME BOSS !!")
    print("")

    def admin_rerun():
        print("")
        sleep(5)
        print("\t\t", "-" * 26, "OWNER INFORMATION", "-" * 30)
        print("")
        print("WELCOME BOSS !!")
        print("")
        print("THESE ARE OPTIONS :\n\nPRESS 1 : TO CHECK GROWTH AND DEMOTE RATE OF HOTEL\nPRESS 2 : FOR CHECK AVAILABILITIES\nPRESS 3 : TO CHECK CUSTOMER DATA FROM DATABASE SERVER\nPRESS 4 : TO MAIN MENU\nPRESS 0 : TO QUIET")
        owner_choice = input("\nENTER YUR CHOICE = ")
        if owner_choice == "1":  # TO CHECK GROWTH AND DEMOTE RATE OF HOTEL
            print("")
            print("HOTEL GROWTH RATE AND RATE OF DECLINE IN WHICH GRAPH :\n\nPRESS 1 : FOR BAR GRAPH\nPRESS 2 : TO MAIN MENU\nPRESS 0 : TO EXIT")
            graph_selection = input("\nENTER YOU CHOICE = ")
            if graph_selection == "1":
                print("")
                print("GRAPH IN BAR-GRAPH")
                year = [2015, 2016, 2017, 2018, 2019, 2020]
                growth = [72, 88, 61, 91, 84, 36]  # out of 100 %
                plt.bar(year, growth, width=0.6, color=["green", "red"])
                plt.xlabel("YEARS")
                plt.ylabel("GROWTH RATE")
                plt.title("HOTEL GROWTH RATE AND RATE OF DECLINE")
                plt.show()
                print("")
                admin_rerun()
            elif graph_selection == "2":
                main_menu()
            elif graph_selection == "0":
                startup()
            else:
                print("")
                print("INVALID OPTION SELECTED\n")
                admin_rerun()

        elif owner_choice == "2":  # FOR CHECK AVAILABILITIES
            print("\nTO CHECK AVAILABILITY OF HOTEL\n")
            print("THESE ARE OPTIONS :\n\nPRESS 1 : FOR CHECK BOOKED ROOMS\nPRESS 2 : TO CHECK INFO OF ROOMS ITEMS\nPRESS 3 : GO TO MAIN MENU")
            _owner_availability_ = input("\nENTER YOU CHOICE : ")
            if _owner_availability_ == "1":
                print("\nTHESE ROOM NUMBER ARE BOOKED IN OUR HOTEL -", for_owner_room_number)
                length_of_room_book = len(for_owner_room_number)
                print("\nTOTAL NUMBER OF ROOM BOOKED - ", length_of_room_book)
                print("\nNUMBER OF VACANT ROOMS - ", 100 - length_of_room_book)
                print("\nTOTAL 100 ROOMS")
            elif _owner_availability_ == "2":
                print("\nALL ROOMS ITEMS IN OUR HOTEL ARE NEW DUE TO LATEST RENOVATION")
                _Room_info_.room_info()  # CALLING OUR OWN CREATING LIBRARY
            elif _owner_availability_ == "3":
                main_menu()
            else:
                print("\nINVALID OPTION SELECTED\n")
            admin_rerun()

        elif owner_choice == "3":  # TO CHECK CUSTOMER DATA FROM DATABASE SERVER
            data_choice = str(input("\nTHESE ARE OPTIONS :\nPRESS 1 : FOR CUSTOMER DATA\nPRESS 2 : FOR BOOKING DATES\nENTER YOUR CHOICE = "))
            if data_choice == "1":
                result_data = [] # For Tabulate to showing data
                print("\nTO CHECK CUSTOMER DATA FROM DATABASE SERVER\n")
                head = ["S NO.", "BILL NO.", "NAME", "AGE", "GENDER", "AADHAAR", "ADDRESS", "PHONE NO.", "NO.OF ROOMS", "PRICE",
                    "ROOM CATEGORY", "ROOM NUMBER"]
                # TO PRINT ALL RECORDS FROM THE TABLE [DATABASE]
                call_all_records = "SELECT * FROM booking_info"
                cursor.execute(call_all_records)
                result = cursor.fetchall()
                for rec in result:
                    result_data.append(rec)
                mydata = result_data
                print(tabulate(mydata, headers=head, tablefmt="psql"))

            elif data_choice == "2":

                result_data = []  # For Tabulate to showing data
                print("\nTO CHECK CUSTOMER DATA FROM DATABASE SERVER\n")
                head = ["S NO.", "BILL NO.", "NAME", "AGE", "GENDER", "AADHAAR", "ADDRESS", "PHONE NO.", "NO.OF ROOMS",
                        "PRICE",
                        "ROOM CATEGORY", "ROOM NUMBER"]
                # TO PRINT ALL RECORDS FROM THE TABLE [DATABASE]
                call_all_records = "SELECT * FROM booking_info"
                cursor.execute(call_all_records)
                result = cursor.fetchall()
                for rec in result:
                    result_data.append(rec)
                mydata = result_data
                print(tabulate(mydata, headers=head, tablefmt="psql"))

                result_data_2 = []  # For Tabulate to showing data
                print("\nTO CHECK BOOKING DATES WITH BILLING NAME FROM DATABASE SERVER\n")
                head = ["S NO.", "BILL NO.","CHECK_IN_DATE", "CHECK_IN_MONTH", "CHECK_IN_YEAR", "  CHECK_OUT_DATE", "CHECK_OUT_MONTH", "CHECK_OUT_YEAR"]
                # TO PRINT ALL RECORDS FROM THE TABLE [DATABASE]
                call_all_records = "SELECT * FROM booked_dates"
                cursor.execute(call_all_records)
                result = cursor.fetchall()
                for rec in result:
                    result_data_2.append(rec)
                mydata = result_data_2
                print("")
                print(tabulate(mydata, headers=head, tablefmt="psql"))

            else:
                print("INVALID INPUT ENTERED\n")
                sleep(1)
                admin_rerun()

            admin_rerun()

        elif owner_choice == "4":
            main_menu()

        elif owner_choice == "0":  # TO EXIT
            print("")
            win_exit_str = str(input("ARE YOU SURE YOU EXIT THE PROGRAM !! [Y/N] = "))
            win_exit = win_exit_str.upper()
            if win_exit == "Y" or win_exit == "YES":
                exit()
            elif win_exit == "N" or win_exit == "NO":
                startup()
            else:
                startup()
        else:
            print("\tINVALID OPTION ENTERED\n")
            admin_rerun()

    pass_input = input("ENTER THE PASSWORD = ")
    password_input = pass_input.upper()
    password = "TAJHOTEL2003"
    print("")
    print("LOADING.....")
    sleep(4)
    if password == password_input:
        print("")
        print("YOU ENTER THE CORRECT PASSWORD !!")
        print("")
        print("PERMISSION ACCESS !!")
        messagebox.showinfo("Information", "Welcome Boss !!")

        def notifyMe(title, message):
            notification.notify(
                title=title,
                message=message,
                app_icon=r"E:\Python\Cs_Project\admin.ico",
                timeout=10
            )
        _name_ = "1"
        if _name_ == "1":
            notifyMe("Admin", "Welcome Boss In Admin Portal")
        admin_rerun()
    else:
        print("")
        print("SORRY YOU ENTER WRONG PASSWORD YOU NOT USE ADMIN WINDOW")
        print("\nPERMISSION DENIED !!")
        print("\nPLEASE RE-RUN THE PROGRRAM")
        messagebox.showwarning("Warning", "Invalid Password Entered")
        startup()

def check_info():
    print("")
    print("\t\t", "=" * 26, "CHECKING DETAIL INFO", "=" * 30)
    print("\nTHIS IS FOR CUSTOMER INFO")
    print("\nPLEASE ENTER THOSE NUMBER WHICH YOU ENTER AT BOOKING TIME ")
    print("")
    str_check_mobi = input("ENTER YOUR MOBILE NUMBER = ")
    try:
        check_mobi = int(str_check_mobi)
        check_mobi_length = len(str_check_mobi)
        if check_mobi_length == 10:
            print("")
            if check_mobi in mobile_of_the_customer:
                print("YOUR NUMBER IS IN OUR LIST")
                print("")
                # FOR SUITABLE INDEXING
                mobile_index = mobile_of_the_customer.index(check_mobi)

                check_name = name_info[mobile_index]
                check_age = age_info[mobile_index]
                check_gender = gender_info[mobile_index]
                check_aadhaar = aadhaar_info[mobile_index]
                check_room_type = room_type[mobile_index]
                check_total_price = total_price[mobile_index]

                # FOR CHECK-IN AND CHECK-OUT
                check_in_date_info = checkin_date[mobile_index]
                check_in_month_info = checkin_month[mobile_index]
                check_in_year_info = year_in[mobile_index]
                check_out_date_info = checkout_date[mobile_index]
                check_out_month_info = checkout_month[mobile_index]
                check_out_year_info = out_year[mobile_index]

                sleep(5)
                print("NAME :", check_name)
                print("AGE :", check_age)
                print("GENDER :", check_gender)
                print("AADHAAR :", check_aadhaar)
                print("ROOM TYPE :", check_room_type)
                print("TOTAL PRICE :", check_total_price)
                print("CHECK-IN DATE :", check_in_date_info, "/", check_in_month_info, "/", check_in_year_info)
                print("CHECK-OUT DATE :", check_out_date_info, "/", check_out_month_info, "/", check_out_year_info)
                print("")
                startup()
            else:
                print("SORRY NO RECORD FOUND WITH THIS NUMBER")
                print("\nFOR RE-ENTER PLEASE RE-RUN THE PROGRAM")
                messagebox.showwarning("Warning", "No Record Found With this Number")
                startup()
        else:
            print("\nINVALID NUMBER ENTERED")
            print("\nPLEASE RE-RUN ")
            check_info()
    except:
        print("\nMOBILE NUMBER ONLY IN NUMERICAL FORM")
        print("\nPLEASE RE-RUN THE PROGRAM")
        messagebox.showerror("Error", "Mobile Number Only in Numbers")
        startup()

def cancel_booking():
    print("")
    print("\t\t", "=" * 28, "CANCEL THE BOOKING", "=" * 30)
    print("")
    print("THIS IS FOR CANCEL THE BOOKING")
    print("")
    print("PLEASE ENTER THOSE NUMBER WHICH YOU ENTER AT BOOKING TIME ")
    print("")
    str_check_mobi = input("ENTER YOUR MOBILE NUMBER = ")
    try:
        check_mobi = int(str_check_mobi)
        check_mobi_length = len(str_check_mobi)
        if check_mobi_length == 10:
            print("")
            if check_mobi in mobile_of_the_customer:
                print("YOUR NUMBER IS IN OUR LIST")
                print("")
                # FOR SUITABLE INDEXING
                mobile_index = mobile_of_the_customer.index(check_mobi)

                check_name = name_info[mobile_index]
                check_age = age_info[mobile_index]
                check_gender = gender_info[mobile_index]
                check_aadhaar = aadhaar_info[mobile_index]
                check_room_type = room_type[mobile_index]
                check_total_price = total_price[mobile_index]

                # FOR CHECK-IN AND CHECK-OUT
                check_in_date_info = checkin_date[mobile_index]
                check_in_month_info = checkin_month[mobile_index]
                check_in_year_info = year_in[mobile_index]
                check_out_date_info = checkout_date[mobile_index]
                check_out_month_info = checkout_month[mobile_index]
                check_out_year_info = out_year[mobile_index]

                # WORK TO BE CONTINUED

                print("NAME :", check_name)
                print("AGE :", check_age)
                print("GENDER :", check_gender)
                print("AADHAAR :", check_aadhaar)
                print("ROOM TYPE :", check_room_type)
                print("TOTAL PRICE :", check_total_price)
                print("CHECK-IN DATE :", check_in_date_info, "/", check_in_month_info, "/", check_in_year_info)
                print("CHECK-OUT DATE :", check_out_date_info, "/", check_out_month_info, "/", check_out_year_info)

                try:
                    # CANCEL THE BOOKING BY REMOVE ALL ITEM OF CUSTOMER

                    mobile_of_the_customer.remove(check_mobi)  # REMOVE THE MOBILE NUMBER
                    name_info.remove(check_name)  # REMOVE THE NAME
                    age_info.remove(check_age)  # REMOVE THE AGE
                    gender_info.remove(check_gender)  # REMOVE THE GENDER
                    aadhaar_info.remove(check_aadhaar)  # REMOVE THE AADHAAR
                    room_type.remove(check_room_type)  # REMOVE THE TYPE OF ROOM
                    total_price.remove(check_total_price)  # REMOVE THE TOTAL PRICE
                    checkin_date.remove(check_in_date_info)  # REMOVE THE CHECK-IN DATE
                    checkin_month.remove(check_in_month_info)  # REMOVE THE CHECK-IN MONTH
                    year_in.remove(check_in_year_info)  # REMOVE THE CHECK-IN YEAR
                    checkout_date.remove(check_out_date_info)  # REMOVE THE CHECK-OUT DATE
                    checkout_month.remove(check_out_month_info)  # REMOVE THE CHECK-OUT MONTH
                    out_year.remove(check_out_year_info)  # REMOVE THE CHECK-OUT YEAR

                    sleep(4)
                    print("")
                    print("OPERATION SUCCESSFULLY DONE !!!")
                    print("\nALL ITEM WHICH YOU ENTER IN BOOKING IS REMOVE FROM OUR LIST")
                    print("\nYOUR BOOKING IS CANCEL")
                    messagebox.showinfo("Info", "Your Item Successfully Removed")

                except:
                    print("")
                    print("THIS ITEM NOT IN OUR LIST")
                    print("\nSORRY !! ERROR OCCURRED\n")
                    messagebox.showerror("Error", "Error Occurred !!")
                    startup()
            else:
                print("SORRY NO RECORD FOUND WITH THIS NUMBER")
                print("\nFOR RE-ENTER PLEASE RE-RUN THE PROGRAM")
                messagebox.showwarning("Warning", "No Record Found With this Number")
                startup()
        else:
            print("\nINVALID NUMBER ENTERED")
            print("\nPLEASE RE-RUN")
            cancel_booking()
    except:
        print("\nMOBILE NUMBER ONLY IN NUMERICAL FORM")
        print("\nPLEASE RE-RUN THE PROGRAM")
        messagebox.showerror("Error", "Mobile Number Only in Numbers")
        startup()

def main_menu():
    # COLUMN FOR MAIN MENU
    print("\t", "-" * 90)
    print("\t\t                             HOTEL TAJ")
    print("\t", "-" * 90)
    print("\t\t                             MAIN MENU")
    print("\t", "-" * 90)
    print("")
    print("\tPRESS 1 : FOR ADMIN\n\tPRESS 2 : FOR USER\n")
    first_choice = input("\tENTER YOUR CHOICE = ")

    if first_choice == "1":  # ONLY FOR OWNER OF HOTEL
        print("\n\tYOU ARE IN ADMIN WINDOW\n")
        print("\tTHESE ARE OPTION :\n\tPRESS 1 : FOR ADMIN WINDOW\n\tPRESS 2 : GO TO MAIN MENU\n\tPRESS 0 : FOR EXIT")
        choice = input("\n\tENTER YOUR CHOICE = ")
        print("")
        if choice == "1":  # FOR ADMIN WINDOW
            owner_info()  # ONLY FOR OWNER OF HOTEL
        elif choice == "2": # MAIN MENU
            main_menu()
        elif choice == "0":  # TO EXIT
            print("")
            win_exit_str = str(input("ARE YOU SURE YOU EXIT THE PROGRAM !! [Y/N] = "))
            win_exit = win_exit_str.upper()
            if win_exit == "Y" or win_exit == "YES":
                exit()
            elif win_exit == "N" or win_exit == "NO":
                startup()
            else:
                startup()
        else:
            print("\tINVALID STATEMENT")
            print("\n\tPLEASE RE-RUN THE PROGRAM")
            startup()

    elif first_choice == "2":
        print("\n\tYOU ARE IN USER WINDOW\n")
        print("\tTHESE ARE OPTIONS :\n\n\tPRESS 1 : FOR BOOKING THE ROOM\n\tPRESS 2 : FOR CANCEL THE BOOKING\n\tPRESS 3 : FOR CHECK CUSTOMER INFO\n\tPRESS 4 : TO CHECK INDIAN MENU CARD\n\tPRESS 5 : TO CHECK HOTEL POLICIES\n\tPRESS 6 : TO SEE HOTEL BROCHURE\n\tPRESS 7 : TO SEE HOTEL ROOM INFO\n\tPRESS 8 : TO CHECK HOTEL IMAGES\n\tPRESS 0 : TO EXIT")
        choice = input("\n\tENTER YOUR CHOICE = ")
        print("")
        if choice == "1":  # FOR BOOKING THE ROOM
            global booking_loop  # MAKE A VARIABLE TO A GLOBAL SCOPE
            booking_loop += 1

            booking()
        elif choice == "2":  # FOR CANCEL THE BOOKING
            cancel_booking()
        elif choice == "3":  # FOR CHECK CUSTOMER INFO
            check_info()
        elif choice == "4":  # TO CHECK MENU CARD
            print("")
            indian_menu_card()
        elif choice == "5":  # HOTEL POLICIES
            hotel_policies()
        elif choice == "6": # FOR HOTEL BROCHURE
            hotel_brochure()
        elif choice == "7": # FOR ROOM INFO
            _Room_info_.room_info()  # CALLING OUR OWN CREATING LIBRARY
            startup()
        elif choice == "8":  # HOTEL IMAGES
            name_image_display()
        elif choice == "0":  # TO EXIT
            print("")
            win_exit_str = str(input("ARE YOU SURE YOU EXIT THE PROGRAM !! [Y/N] = "))
            win_exit = win_exit_str.upper()
            if win_exit == "Y" or win_exit == "YES":
                exit()
            elif win_exit == "N" or win_exit == "NO":
                startup()
            else:
                startup()
        else:
            print("\tINVALID STATEMENT")
            print("\n\tPLEASE RE-RUN THE PROGRAM")
            startup()
    else:
        print("\n\tINVALID SYNTAX ENTERED\n")
        print("\tPLEASE RE-RUN THE PROGRAM")
        startup()

my_image = PIL.Image.open(r"E:\Python\Cs_Project\_Taj_.png")
my_image.show()

main_menu()