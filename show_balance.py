import pandas as pd
from login import login_usr
class ShowBal:

    def __init__(self):
        pass
    
    @classmethod
    def show_bal(cls):
        
        if login_usr.status:
            bal_data = pd.read_csv('E:/Python_projects/Bankig_App/data_base/Balance.csv')
            ttl_bal = float(bal_data['Total_Balance'])
            print(f"\n\nYour balance is: {ttl_bal}\n\n")
        else:
            print('\n Please login before do the balance enquire.\n')
            login_usr.usr_login()
            ShowBal.show_bal()

