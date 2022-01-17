from user_option import UserOptions as uo
from Home_page import Home
from login import login_usr


if __name__ == '__main__':
    print('######################\n\n WELLCOME TO VJ BANK\n\n######################')
    Home.signing()
    if login_usr.status != True:
        login_usr.usr_login()



    while(True):

        usr_opn = uo.select_option()
        if usr_opn == 0:
            print('\n================================\nTHANK YOU. HOPE YOU VISIT AGAIN.\n================================\n')
            break
        uo.usr_opn_controll(usr_opn)
