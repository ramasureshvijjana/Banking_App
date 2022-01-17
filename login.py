import re
import pandas as pd
from creat_acc import CrtAcc

class Login:

    def __init__(self):
        self.status = False

    @classmethod
    def login_id(cls, data):
        acc_num = input("Please enter your account number: ")
        if re.match('^\d{12}$', acc_num):
            try:
                # If Account_num not exist it will rise TypeError, Then it will go to first except.
                usr_data = data[data['Account_num'] == int(acc_num)]
                return usr_data
            # If email not fount this exception will catch and handle.
            except TypeError as tp:
                print(f'This {acc_num} account number is not existed. Please enter existed one.')
                cls.login_id(data)
        else:
            print('This account number is invalied, Please enter valied one')
            Login.login_id(data)

    @classmethod
    def psw_check(cls, usr_data):
        cr_obj = CrtAcc()
        pswd = cr_obj.psw_input()
        if int(usr_data['Password']) == pswd:
            return pswd
        else:
            print(f"Incorrect password. Please enter valied one.")
            Login.psw_check(usr_data)


    def usr_login(self):
        print('#########\n  LOGIN  \n#########\n\nPlease enter your login credentials.')
        data = pd.read_csv('E:\Python_projects\Bankig_App\data_base\Book1.csv')
        usr_data = Login.login_id(data)
        Login.psw_check(usr_data)

        self.name = usr_data['Name']
        self.gender = usr_data['Gender']
        self.age = usr_data['Age']
        self.ph_num = usr_data['Phone']
        self.email = usr_data['Email']
        self.acc_num = usr_data['Account_num']

        self.status = True

login_usr = Login()


