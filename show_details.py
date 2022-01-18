from login import login_usr
class ShowDetails:

    @classmethod
    def show_details(cls):

        if login_usr.status:
            print(f'\n\n YOUR DETAILS ARE:\n \
            Name: {str(login_usr.name)[5:]}\n \
            Age:  {int(login_usr.age)}\n \
            Account Number: {int(login_usr.acc_num)}\n \
            Pone: {int(login_usr.ph_num)}\n \
            Email: {str(login_usr.email)[5:]}\n \
            Gender: {str(login_usr.gender)[5:]}\n\n')
        else:
            print('\n Please login before do the balance enquire.\n')
            login_usr.usr_login()
            ShowDetails.show_details()