import user_option as uo


if __name__ == '__main__':
    print('######################\n\n WELLCOME TO VJ BANK\n\n######################')

    while(True):

        usr_opn = uo.select_option()
        if usr_opn == 0:
            print('\n================================\nTHANK YOU. HOPE YOU VISIT AGAIN.\n================================\n')
            break
        uo.usr_opn_controll(usr_opn)

