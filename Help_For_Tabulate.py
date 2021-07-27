# todo : This is for Help in tabulate table
from tabulate import tabulate
head= ["Row1","Row2","Row3"]
# assign data
mydata = [{'a', 'b', 'c'},{12, 34, 56},{'Geeks', 'for', 'geeks!'}]
# display table
print(tabulate(mydata,headers=head,tablefmt="psql"))
exit()

# todo : This is our Project Tabulate part
from tabulate import tabulate
import mysql.connector as mysqlt

mydb = mysqlt.connect(
    host="localhost",
    user="root",
    password="ujjwal2003",
    database="hotel_management"
)
cursor = mydb.cursor()
result_data = []
print("\nTO CHECK CUSTOMER DATA FROM DATABASE SERVER\n")
head=["S NO.", "NAME", "AGE", "  GENDER", "AADHAAR", "ADDRESS", "PHONE NO.", "NO.OF ROOMS", "PRICE", "ROOM CATEGORY", "ROOM NUMBER"]
# TO PRINT ALL RECORDS FROM THE TABLE [DATABASE]
call_all_records = "SELECT * FROM booking_info"
cursor.execute(call_all_records)
result = cursor.fetchall()
for rec in result:
    # print(rec)
    result_data.append(rec)

mydata = result_data

print(tabulate(mydata,headers=head,tablefmt="psql"))
# print(tabulate(mydata, headers=head, tablefmt="grid"))

# todo :  FOr more information Visit to - https://pypi.org/project/tabulate/
