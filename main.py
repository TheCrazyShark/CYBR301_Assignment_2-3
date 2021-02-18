# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def getusername_paswd():
    username = input('Please enter username: ')
    password = input('Please enter password: ')

    # tests each character in password if one is uppercase or numeric
    for i in password:
        if i == i.isupper():
            passUpper = True
        if i == i.isnumeric():
            passNum = True

    # tests if a special character is in password
    if "#" in password or "@" in password or "%" in password or "*" in password:
        passSpecial = True

    # Asks user to re-enter their password until it is valid
    while len(password) > 7 and not(passUpper) and not(passNum) and not(passSpecial):
        password = input('Please enter a valid password: ')

    return username, password


def secure_store(username, password):
    print('Username: ' + username)
    print('Password: ' + password)


def main():
    susername, spassword = getusername_paswd()
    if susername and spassword:  # Need to change this to check getusername_paswd() returns 1
        secure_store(susername, spassword)


if __name__ == "__main__":
    main()
