import time
import pyotp
import csv
import pandas as pd
 
df = pd.read_csv('keys.csv')

def generate_otp(key):
    x = pyotp.TOTP(str(key))
    return x.now()

def add_account(website, key, name):
    f = open("keys.csv", "a")
    x = f"{website},{key},{name}\n"
    f.write(x)
    f.close()

def display_otp(i):
    x = df['Key'][i]
    name = df['Name'][i]
    remaining_time = 30 - time.time()%30
    return name,generate_otp(x),remaining_time

def main():
    print("1 - OTP")
    print("2 - Password Manager")
    print("3 - Exit")
    x = int(input(">>"))

    if x == 1:
        otp()
    if x == 2: 
        print("WIP")

def otp():
    print("1 - Add OTP")
    print("2 - Display OTP")
    print("3 - Exit")
    x = int(input(">>"))

    if x == 1:
        print("WIP")
    if x == 2:
        for i in range(len(df.index)):
            print(display_otp(i))
        otp()

main()