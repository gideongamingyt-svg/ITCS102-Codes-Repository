
from getpass import getpass

u = "palcisomewing"
p = "handsomesmewing"

isLogin = False #trigger

while isLogin == False: 

    user = input("Please input username --> ")
    pword = getpass("Please input password -->") 

    if user == u and pword == p:   
        print("LOGIN SUCCESSFULLY")
        isLogin = True
    else:
        print("LOGIN DENIED")
        isLogin = False

        