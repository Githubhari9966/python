#import regular expression
import re
#varible pwd is loaded with user creating password
pwd= input("Enter your password:\n")
#if the condition f is true
f = True
while f:
    if (len(pwd)<6 or len(pwd)>16): # it check weather given password is less than 6 char or more than 16
        break
    elif not re.search("[a-z]",pwd): # it search password for lower case letters
        break
    elif not re.search("[0-9]",pwd): #it search password for numbers
        break
    elif not re.search("[A-Z]",pwd): # it search password for the upper case letters
        break
    elif not re.search("[[$@!*]",pwd): # it search password for special characters
        break
    elif re.search("\s",pwd): # it search the password for spaces
        break
    else:
        print("Valid Password")
        f=False
        break

if f:
    print("invalid password")