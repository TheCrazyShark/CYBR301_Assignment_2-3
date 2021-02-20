from Crypto.Cipher import AES

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

    # 16 byte key used for encryption
    key = b'\xa4\'\xf4\x0c"\xf9a,\x9c\xac\x12\xc1\x83n\x7ft'
    # Allows for encryption. Uses EAX mode as it can detect unauthorized modifications
    cipher = AES.new(key, AES.MODE_EAX)

    # opens credential.dat file
    with open('credential.dat', 'a') as f:
        # encrypts the password
        encrypted_password = cipher.encrypt(password.encode('utf-8'))

        # writes username and password to file
        f.write(username + "\n")
        f.write(str(encrypted_password) + "\n")

        print("Username and password written to credentials.dat")

        # closes credential.dat file
        f.close()


def main():
    susername, spassword = getusername_paswd()
    if susername and spassword:
        secure_store(susername, spassword)


if __name__ == "__main__":
    main()