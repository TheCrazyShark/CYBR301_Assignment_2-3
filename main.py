# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def getusername_paswd():
    username = input('Please enter username: ')
    password = input('Please enter password: ')

    pass_user, pass_upper, pass_lower, pass_num, pass_special = False, False, False, False, False

    # tests if username contains @ to make sure it is an email address
    if "@" in username:
        pass_user = True

    # tests each character in password if one is uppercase or numeric
    for i in password:
        if i.isupper():
            pass_upper = True
        if i.islower():
            pass_lower = True
        if i.isnumeric():
            pass_num = True

    # tests if a special character is in password
    if "#" in password or "@" in password or "%" in password or "*" in password:
        pass_special = True

    # calls function again until a valid username and password is entered
    if pass_user and len(password) > 7 and pass_upper and pass_lower and pass_num and pass_special:
        print("Valid username and password!")
        return username, password

    else:
        print("Please enter a valid username/password.")
        getusername_paswd()


def secure_store(username, password):
    print('Username: ' + username)
    print('Password: ' + password)


def main():

    getusername_paswd()

    """
    susername, spassword = getusername_paswd()
    if susername and spassword:  # Need to change this to check getusername_paswd() returns 1
        secure_store(susername, spassword)
    """


if __name__ == "__main__":
    main()
