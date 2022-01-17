import imp
from user_option import UserOptions as uo
from creat_acc import CrtAcc as ca
from login import login_usr

class Home:

    def signing():
        sign_opn = uo.signing_optn()

        if sign_opn == 1:
            ca.create_acc()
        else:         
            login_usr.usr_login()