import time
import pyotp
import pandas as pd
from cryptography.fernet import Fernet
 
 
df_otp = pd.read_csv('keys.csv')
df_pass = pd.read_csv('secrets.csv')

def get_fernetkey():
    f = open("fkey.txt", "r")
    x = f.read()
    #print(x)
    return str(x)

def generate_fernetkey():
    key = Fernet.generate_key()
    #x = Fernet(key)
    #print(type(key))
    f = open("fkey.txt", "w")
    f.write(key.decode())

def generate_otp(key):
    x = pyotp.TOTP(str(key))
    return x.now()

def add_account(website, key, name):
    f = open("keys.csv", "a")
    x = f"{website},{key},{name}\n"
    f.write(x)
    f.close()

def display_otp(i):
    x = df_otp['Key'][i]
    name = df_otp['Name'][i]
    remaining_time = 30 - time.time()%30
    return name,generate_otp(x),remaining_time

def add_password(website, user, password):
    x = get_fernetkey()
    fernet = Fernet(x.encode())
    #print(fernet)
    password = password.encode()
    token = fernet.encrypt(password)
    token = token.decode()
    f = open("secrets.csv", "a")
    x = f"{website},{user},{token}\n"
    f.write(x)
    f.close()

def display_passwords(i):
    x = get_fernetkey()
    fernet = Fernet(x.encode())
    #print(fernet)
    website = df_pass['Website'][i]
    user = df_pass['User'][i]
    password = df_pass['Password'][i]
    password = fernet.decrypt(password)
    return website,user,password.decode()


def main():
    print("1 - OTP")
    print("2 - Password Manager")
    print("3 - Exit")
    x = int(input(">>"))

    if x == 1:
        otp()
    if x == 2: 
        passmanager()

def otp():
    print("1 - Add OTP")
    print("2 - Display OTP")
    print("3 - Exit")
    x = int(input(">> "))

    if x == 1:
        print("Enter email/website")
        website = str(input(">> "))
        print("Enter secret key (no spaces)")
        key = str(input(">> "))
        print("Enter name")
        name = str(input(">> "))
        add_account(website,key,name)
        otp()

    if x == 2:
        for i in range(len(df_otp.index)):
            print(display_otp(i))
        otp()

def passmanager():
    print("1 - Show accounts")
    print("2 - Add account")
    print("3 - Exit")
    print("9 - Generate Fernet Key")
    x = int(input(">> "))

    if x == 1:
        for i in range(len(df_pass.index)):
            print(display_passwords(i))
        passmanager()
    if x == 2:
        print("WIP")
    if x == 3:
        main()

main()