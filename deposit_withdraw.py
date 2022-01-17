
from login import login_usr
import pandas as pd
import datetime
class DpstWdrw:
    


    @classmethod
    def money_check(cls):
        if login_usr.status:
            try: 
                balance = input('Please enter amount: ')

                bal_data = pd.read_csv('E:/Python_projects/Bankig_App/data_base/Balance.csv')
                crnt_bal = bal_data[bal_data['Account_num'] == login_usr.acc_num]['Total_Balance']

                return float(balance), bal_data, crnt_bal
            except ValueError as ve:
                print(f'{balance}is invalied input. Please enter valied one.')
                DpstWdrw.money_check(cls)
            


    @classmethod
    def deposit(cls):
        balance, bal_data, crnt_bal = DpstWdrw.money_check()
        if balance >= 100 and balance <= 100000:
            total_bal = balance + crnt_bal
            DpstWdrw.saving(total_bal, bal_data, balance)
        else:
            print('The entered amount should be in between 100 to 100000')
            DpstWdrw.deposit()



    @classmethod
    def withdrawal(cls):
        balance, bal_data, crnt_bal = DpstWdrw.money_check()
        if balance >= 100 and balance <= 20000 and balance < crnt_bal:
            total_bal = balance - crnt_bal
            DpstWdrw.saving(total_bal, bal_data, balance)
        else:
            print('The entered amount should be in between 100 to 20000')
            DpstWdrw.withdrawal()




    @classmethod
    def saving(cls, total_bal, bal_data, balance):
                
        x = datetime.datetime.now()
        date = x.strftime("%d/%m/%G")
        time = x.strftime("%I:%M:%S %p")
        acc_no = login_usr.acc_num
        
        stmt_dict = {'Account_num': acc_no,'Date': date, 'Time': time, 'Deposit': balance,'Withdrawal': 0,'Total_Balance': total_bal}
        stmt_df = pd.DataFrame(stmt_dict, index=[0])
        stmt_df.to_csv('E:/Python_projects/Bankig_App/data_base/Statements.csv', mode='a', index=False, header=False)


        bal_data.loc[bal_data['Account_num'] == login_usr.acc_num, 'Total_Balance'] = total_bal
        bal_data.to_csv('E:/Python_projects/Bankig_App/data_base/Balance.csv', index=False)




