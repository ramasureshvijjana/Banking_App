
import phonenumbers as pn
import re

class Validation:

    @classmethod
    def len_validation(cls, min_len, max_len, val):
        if len(val) <= max_len and len(val) >= min_len:
            return True
        else:
            return False



    @classmethod
    def name_vlidation(cls, val):
        y = val.replace(" ", "")
        if y.isalpha():
            return True
        else:
            return False



    def name_vldn(self, name):

        # Checking lenth of name [3 <= len(name) <= 100 ]
        if self.len_validation(3, 100, name):
            # Checking name properties
            if self.name_vlidation(name):
                # Change 1st char of every word as capital Ex: [rama ----> Rama]
                name = name.title()
                return name

            else:
                raise ValueError('\nThe name should not have numbers and special characters.\nPlease enter a valid Name.\n')
                
        else:
            raise ValueError('\nThe name length should be between 3 to 100.\nPlease enter a valid Name.')



    def gender_vldn(self, gender):

        # Checking is user input in ['M', 'F', 'O']
        if gender.upper() in ['M', 'F', 'O']:
            return gender.upper()
        else:
            raise ValueError('\nThe gender should be "M" or "F" or "O".\nPlease enter a valid Gender.\n')



    def age_vldn(self, age):
    
        if age.isdigit():
            age = int(age)
            if age >= 18 and age <= 100:
                return age
            else:
                raise ValueError(f"{age} is not aligible age. Sorry You can't create Bank account")
        else:
            raise ValueError(f"{age} is invalid input. Please enter valid one.")



    def ph_vldn(self, phone):

        phone = pn.parse(phone)
        # below line checks is the phone number is valid and is that possible number
        if pn.is_valid_number(phone) and pn.is_possible_number(phone): # another way: (Not recomended) --> re.match(r'^[0-9]{10}$', phone)
            return phone
        else:
            raise ValueError(f"{phone} is invalid input. Please enter valid one.")



    def mail_vldn(self, mail):

        if re.match(r'^[a-z0-9]+@[a-z]{2,8}.com$', mail):
            return mail
        else:
            raise ValueError('ERROR: This is invalid mail. Please enter valid email.')



    def psw_vldn(self, pws):

        if pws.isdigit():
            if len(pws) == 4:
                return int(pws)
            else:
                raise ValueError(f"{pws} Should have 4 digits.")
        else:
            raise ValueError(f"{pws} is invalid input. Please enter valid one.")