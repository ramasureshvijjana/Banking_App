from creat_acc import CrtAcc as ca
import show_balance as sb
from deposit_withdraw import DpstWdrw as dw
#import main

class UserOptions:


    @classmethod
    def signing_optn(cls):
        print('1. CREATE ACCOUNT\n2. lOGIN\n')

        try:
            usr_rsp = input('SELECT YOUR OPTION:   ')
            if usr_rsp.isdigit():
                usr_rsp = int(usr_rsp)

                if usr_rsp in range(1,3):
                    return usr_rsp

                else:
                    raise ValueError(f'Your option should be 1 or 2. {usr_rsp} is not valied')

            else:
                raise ValueError(f'{usr_rsp} is invalid input. Please select valid one.')

        except ValueError as e:
            print(e)
            UserOptions.select_option()



    @classmethod
    def usr_opn_controll(cls,usr_opn):
        # if usr_opn == 0:
        #     main.exit()
        if usr_opn == 1:
            sb.ShowBal.show_bal()
        elif usr_opn == 3:
            dw.deposit()

                


    @classmethod
    def select_option(cls):
        print('WHAT YOU ARE LOOKING FOR \n\n \
        1. Show My Details\n \
        2. Show Balance\n \
        3. Diposit\n \
        4. withdrawal\n \
        5. Change Password\n \
        6. Update Phone Number & Email\n \
        7. Take Loan\n')

        try:
            usr_opn = input('PLEASE SELECT YOUR OPTION:  ')
            if usr_opn.isdigit():
                usr_opn = int(usr_opn)

                if usr_opn in range(0,9):
                    return usr_opn

                else:
                    raise ValueError(f'Your option should be in [0,1,2,3,4,5,6,7,8], {usr_opn} is not valied')

            else:
                raise ValueError(f'{usr_opn} is invalid input. Please select valid one.')

        except ValueError as e:
            print(e)
            UserOptions.select_option()