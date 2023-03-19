# create a simple password generator for a signup space
# consisting of uppercase, lowercase, symbol and numbers.

import random
import string


def generate_password():
    user_firstname = str(input('Enter your firstname: '))
    user_lastname = str(input('Enter your lastname: '))

    def ascii_generator(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        for i in range(0, 2):
            n = random.randint(1, 30)

        print('{}${}_{}{}{}'.format(user_firstname,
              result_str, n, user_lastname, result_str))
    ascii_generator(1)


generate_password()
