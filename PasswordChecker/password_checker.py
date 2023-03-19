# check password strength
def check_password_strength():
    max_length = 8
    has_upperCase = False
    has_lowerCase = False
    has_digit = False
    password = input('Enter password: ')
    if len(password) < max_length:
        print('Password length must be 8 characters long!')
    elif len(password) == max_length:
        print('Nice Password length')
    else:
        print('Password is too long!')

    for char in password:
        if char.isupper():
            has_upperCase = True
        elif char.islower():
            has_lowerCase = True
        elif char.isdigit():
            has_digit = True

    if not has_upperCase:
        print('Password requires a capital letter')
        return False
    if not has_lowerCase:
        print('Password requires a lower letter')
        return False
    if not has_digit:
        print('Password requires a number')
        return False
    else:
        print('Password is strong')
        return True


check_password_strength()
