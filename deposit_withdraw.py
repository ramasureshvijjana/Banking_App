
from login import login_usr
import pandas as pd
import datetime
class DpstWdrw:
    
    @classmethod
    def deposit(cls):
        if login_usr.status:
            try: 
                balance = input('Please enter amount: ')
                balance = float(balance)

                if balance >= 100 and balance <= 100000:
                    bal_data = pd.read_csv('E:/Python_projects/Bankig_App/data_base/Balance.csv')
                    crnt_bal = bal_data[bal_data['Account_num'] == login_usr.acc_num]['Total_Balance']
                    
                    x = datetime.datetime.now()
                    date = x.strftime("%d/%m/%G")
                    time = x.strftime("%I:%M:%S %p")
                    acc_no = login_usr.acc_num
                    
                    total_bal = balance + crnt_bal
                   
                    stmt_dict = {'Account_num': acc_no,'Date': date, 'Time': time, 'Deposit': balance,'Withdrawal': 0,'Total_Balance': total_bal}
                    stmt_df = pd.DataFrame(stmt_dict, index=[0])
                    stmt_df.to_csv('E:/Python_projects/Bankig_App/data_base/Statements.csv', mode='a', index=False, header=False)


                    bal_data.loc[bal_data['Account_num'] == login_usr.acc_num, 'Total_Balance'] = total_bal
                    bal_data.to_csv('E:/Python_projects/Bankig_App/data_base/Balance.csv')
                    
                else:
                    raise Exception(f'The entered amount should be in between 100 to 100000')
            except Exception as e:
                print(e)
                DpstWdrw.deposit()
            except ValueError as ve:
                print(f'{balance}is invalied input. Please enter valied one.')
                DpstWdrw.deposit()



