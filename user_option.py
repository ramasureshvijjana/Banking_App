import creat_acc as ca
import show_balance as sb
import main



def usr_opn_controll(usr_opn):
    if usr_opn == 1:
        ca.create_acc()
    elif usr_opn == 0:
        main.exit()
    elif usr_opn == 3:
        sb.ShowBal.show_bal()

def select_option():
    print('WHAT YOU ARE LOOKING FOR \n\n \
    1. Create Account\n \
    2. Show My Details\n \
    3. Show Balance\n \
    4. Diposit\n \
    5. withdraw\n \
    6. Change Password\n \
    7. Update Phone Number & Email\n \
    8. Take Loan\n')

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
        select_option()