import re

def check_password_strength(pswd):
    length_pwd = len(pswd)
    uppercase = re.findall('[A-Z]',pswd)
    lowercase = re.findall('[a-z]',pswd)
    number= re.findall('[0-9]',pswd)
    specialchar= re.findall('[^a-zA-z0-9]',pswd)

    if length_pwd<7:
        print("Atleast min 8 char required!!")
    elif len(uppercase)==0:
        print("Must 1 contain uppercase!!")
    elif len(lowercase)==0:
        print("Must 1 contain lowercase!!")
    elif len(number)==0 :
        print("Must 1 contain number!!")
    elif len(specialchar)==0:
        print("Must 1 contain special char!!")
    else:
        print("Password is strong.")

pwd= input("Enter your password to check its strength: ")
check_password_strength(pwd)