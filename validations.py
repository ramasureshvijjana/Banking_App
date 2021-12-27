

def len_validation(min_len, max_len, val):
    if len(val) <= max_len and len(val) >= min_len:
        return True
    else:
        return False

def name_vlidation(val):
    y = val.replace(" ", "")
    if y.isalpha():
        return True
    else:
        return False
