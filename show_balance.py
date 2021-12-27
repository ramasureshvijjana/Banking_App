import creat_acc as ca
import login
class ShowBal:

    def __init__(self):
        pass

    def show_bal():
        lgn_status, usr_details = login.usr_obj.usr_login()
        if lgn_status:
            print(f'Your bal is: {usr_details.ph_num}')
