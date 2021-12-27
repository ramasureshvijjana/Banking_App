import re
import pandas as pd
import creat_acc as ca

class Login:

    def __init__(self):
        pass

    @classmethod
    def login_id(cls):
        acc_num = input("Please enter your account number: ")
        if re.match('^\d{12}$', acc_num):
            return int(acc_num)
        else:
            print('This account number is invalied, Please enter valied one')
            Login.login_id()


    def usr_login(self):
        acc_num = Login.login_id()
        pswd = ca.psw_input()
        data = pd.read_csv('E:\Python_projects\Bankig_App\data_base\Book1.csv')
        

        try:
            
            # If email not exist it will rise TypeError, Then it will go to first except.
            usr_data = data[data['Account_num'] == acc_num]
            # print(bool(int(usr_data['Password']) == pswd))
            if int(usr_data['Password']) == pswd:
                self.name = usr_data['Name']
                self.gender = usr_data['Gender']
                self.age = usr_data['Age']
                self.ph_num = usr_data['Phone']
                self.email = usr_data['Email']
                self.acc_num = usr_data['Account_num']

                return True, self
                
            else:
                raise ValueError(f'Your email or password are not valied, please try again ')

        # If email not fount this exception will call and handle.
        except TypeError as tp:
            print('Account number not exist, Please enter eisted account')
            self.usr_login()        
        except Exception as e:
            print(e)
            self.usr_login()

usr_obj = Login()


