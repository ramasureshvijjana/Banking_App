from xml.dom import ValidationErr
import pandas as pd
from pandas.core.accessor import register_dataframe_accessor
from validations import Validation
import re
import random as rd



class CrtAcc:

    vld = Validation()
    
    # Taking name input & doing Name Validation
    def name_input(self):
        try:
            # Taking name input
            name = input('Please enter your full name: ')
            return self.vld.name_vldn(name)
        # Handle both (name length, name property) Exceptions.
        except ValueError as e:
            print(e)
            # Recirrsion the name_input() to take input again if the exception raise. 
            self.name_input()



    # Taking gender input & doing gender validation
    def gender_input(self):
        try:
            # Taking Gender input
            gender = input('Please enter your Gender: ')
            return self.vld.gender_vldn(gender)
        except ValueError as e:
            print(e)
            self.gender_input()



    # Taking age input & doing age Validation
    def age_input(self):
        try:
            # Taking Gender input
            age = input('Please enter your Age: ')
            return self.vld.age_vldn(age)
        except ValueError as e:
            print(e)
            self.age_input()



    def phone_num_input(self, data):
        try:
            phone = '+91' + input('Please enter your Phone number: ')
            phone = str(self.vld.ph_vldn(phone))[-10:]
            if phone not in data['Phone']:
                return phone
            else:
                raise ValidationErr(f'This {phone} number is already linked with another account. Please enter another one.')
        except ValueError as e:
            print(e)
            self.phone_num_input(data)
        except ValidationErr as e:
            print(e)
            self.phone_num_input(data)



    def mail_input(self):
        try:
            mail = input('Please enter your mail: ')
            return self.vld.mail_vldn(mail)
        except ValueError as e:
            print(e)
            self.mail_input()



    def psw_input(self):
        try:
            # Taking Gender input
            pws = input('Please set a 4 digit ATM Pin: ')
            return self.vld.psw_vldn(pws)
        except ValueError as e:
            print(e)
            self.psw_input()


    def acc_num_crt(self, data):

        acc_num = '8260297' + str(rd.randrange(10 ** 4, 10 ** 5))
        if acc_num not in data['Account_num']:
            return acc_num
        else:
            self.acc_num_crt(data)



    def adhar_num(self, data):

        try:
            adhr = input('Plese Enter your adhar number:')
            if re.match(r"^[2-9]{1}[0-9]{3}[0-9]{4}[0-9]{4}$", adhr):
                if adhr not in data['Adhar']:
                    return adhr
                else:
                    raise ValidationErr('This adhar nuber already have an account')
            else:
                raise ValueError('This is invalid adhar number. Please enter valied adhar number')

        except ValidationErr as e:
            print(e)
            self.adhar_num(data)
        except ValueError as e:
            print(e)
            self.adhar_num(data)
            

    def create_acc():

        crt_acc = CrtAcc()
        # Printing a massage
        print('\nFor creating an account we need your information. Please give your info.\n')
        data = pd.read_csv('E:/Python_projects/Bankig_App/data_base/Book1.csv')

        # User input details
        # Calling respective input functions for each detail.
        
        name = crt_acc.name_input()
        gender = crt_acc.gender_input()
        age = crt_acc.age_input()
        adhr = crt_acc.adhar_num(data)
        phone_no = crt_acc.phone_num_input(data)
        email = crt_acc.mail_input()
        acc_no = crt_acc.acc_num_crt(data)
        password = crt_acc.psw_input()
       
        print(name, gender, age, phone_no, email, acc_no, password, adhr)


            
        dct = {'Name': name, 'Gender': gender,'Age' : age, 'Adhar': adhr, 'Phone': phone_no ,'Email': email, 'Account_num': \
        acc_no,'Password' : password}

        df = pd.DataFrame(dct, index=[0])
        df.to_csv('E:/Python_projects/Bankig_App/data_base/Book1.csv', mode='a', index=False, header=False)

        print(f'Your account secussfully created\n################\n Wellcome {name}\n################\n')
        print(f'Your account number: {acc_no}\n\n NOTE: Please rember your account number, this is your login ID. \
        Don\'t share it to any one\n\n')

        
