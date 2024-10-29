from datetime import datetime
import re

def login(user_name,passowrd):
    print(user_name,passowrd,"login success")
    print("Menu")
    options = "1.ippl\n2.wpl\n3.quit"
    opt = int(input(options))
    if  opt == 1:
        print("IPL Menu:")
        options = "1.SRH\n2.RCB\n3.DD"

user_menu = int(input("user_menu_1_or_2:"))
if user_menu == 1:
    user_name = input("username:")
    passowrd = input("password:")
    login(user_name,passowrd)
elif user_menu == 2:
    user_name = input("name:")
    mobile_no = int(input("mobile no:"))
    email = input("email:")
    #date_of_birth = input("Enter date_of_birth:")
    #date_object = datetime.strptime(date_of_birth,"DD-MM-YYYY")
    passowrd = input("password:")
    retype_password = input("retype_password:")
    if passowrd == retype_password:
        user_name = input("username:")
        passowrd = input("password:")
        login(user_name,passowrd)
    