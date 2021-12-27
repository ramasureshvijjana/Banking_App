import pandas as pd
from pandas.core.accessor import register_dataframe_accessor
import validations as vld
import re
import random as rd
import phonenumbers as pn


# Taking name input & doing Name Validation
def name_input():
    try:
        # Taking name input
        name = input('Pleasr enter your full name: ')
        # Checking lenth of name [3 <= len(name) <= 100 ]
        if vld.len_validation(3, 100, name):
            # Checking name properties
            if vld.name_vlidation(name):
                # Change 1st char of every word as capital Ex: [rama ----> Rama]
                name = name.title()
                return name

            else:
                raise ValueError('\nThe name should not have numbers and special characters.\nPlease enter a valid Name.\n')
                
        else:
            raise ValueError('\nThe name length should be between 3 to 100.\nPlease enter a valid Name.')
    # Handle both (name length, name property) Exceptions.
    except ValueError as e:
        print(e)
        # Recirrsion the name_input() to take input again if the exception raise. 
        name_input()



# Taking name input & doing Name Validation
def gender_input():
    try:
        # Taking Gender input
        gender = input('Pleasr enter your Gender: ')
        # Checking is user input in ['M', 'F', 'O']
        if gender.upper() in ['M', 'F', 'O']:
            return gender.upper()
        else:
            raise ValueError('\nThe gender should be "M" or "F" or "O".\nPlease enter a valid Gender.\n')
    except ValueError as e:
        print(e)
        gender_input()



# Taking age input & doing age Validation
def age_input():
    try:
        # Taking Gender input
        age = input('Pleasr enter your Age: ')
        if age.isdigit():
            age = int(age)
            if age >= 18 and age <= 100:
                return age
            else:
                raise ValueError(f"{age} is not aligible age. Sorry You can't create Bank account")
        else:
            raise ValueError(f"{age} is invalid input. Please enter valid one.")
    except ValueError as e:
        print(e)
        age_input()


def phone_num_input():
    try:
        phone = input('Pleasr enter your Phone number along with country code: ')
        phone = pn.parse(phone)
        # below line checks is the phone number is valid and is that possible number
        if pn.is_valid_number(phone) and pn.is_possible_number(phone): # another way: (Not recomended) --> re.match(r'^[0-9]{10}$', phone)
            return phone
        else:
            raise ValueError(f"{phone} is invalid input. Please enter valid one.")
    except ValueError as e:
        print(e)
        phone_num_input()



def address_input():
    try:
        address = input('Pleasr enter your address: ')
        add_len = len(address)
        if add_len > 5 and add_len < 200:
            return address
        else:
            raise ValueError(f"Your address length should be greater than 5 and less than 200. Please enter a valid one.")
    except ValueError as e:
        print(e)
        phone_num_input()


def mail_input():
    try:
        mail = input('Pleasr enter your mail: ')
        if re.match(r'^[a-z0-9]+@[a-z]{2,8}.com$', mail):
            return mail
        else:
            raise ValueError('ERROR: This is invalid mail. Please enter valid email.')
    except ValueError as e:
        print(e)
        mail_input()



def psw_input():
    try:
        # Taking Gender input
        pws = input('Please set a 4 digit ATM Pin: ')
        if pws.isdigit():
            pws_len = len(pws)
            if pws_len == 4:
                return int(pws)
            else:
                raise ValueError(f"{pws} Should have 4 digits.")
        else:
            raise ValueError(f"{pws} is invalid input. Please enter valid one.")
    except ValueError as e:
        print(e)
        psw_input()


def create_acc():
    # Printing a massage
    print('\nFor creating an account we need your information. Please give your info.\n')

    # User input details
    # Calling respective input functions for each detail.
    name = name_input()
    gender = gender_input()
    age = age_input()
    phone_no = phone_num_input()
    email = mail_input()
    acc_no = rd.randrange(10 ** 11, 10 ** 12)
    password = psw_input()

    data = pd.read_csv('E:/Python_projects/Bankig_App/data_base/Book1.csv')
    print(name, gender, age, phone_no, email, acc_no, password)


    if acc_no not in data['Account_num']:
        
        dct = {'Name': name, 'Gender': gender,'Age' : age, 'Phone': phone_no ,'Email': email, 'Account_num': \
        acc_no,'Password' : password}

        df = pd.DataFrame(dct, index=[0])
        df.to_csv('E:/Python_projects/Bankig_App/data_base/Book1.csv', mode='a', index=False, header=False)

        print(f'Your account secussfully created\n################\n Wellcome {name}\n################\n')
        print(f'Your account number: {acc_no}\n\n NOTE: Please rember your account number, this is your login ID. \
        Don\'t share it to any one\n\n')
        
