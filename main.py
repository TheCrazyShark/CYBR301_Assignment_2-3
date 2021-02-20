from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode
from Crypto.Cipher import AES

def getusername_paswd():
    username = input('Please enter username: <Enter your email address>')
    password = input("Password rules are:"
                   "\n 1. at least 8 characters, "
                   "\n 2. has at least one alphabet,"
                   "\n 3. has at least one digit, "
                   "\n 4. has at a character in {#,$,%,*}"
                   "\n Enter your password:")
    pass_upper, pass_num, pass_special, pass_length, user_email, valid_both = False

    # Tests to see if username is an email
    if "@" in username:
        user_email = True

    # tests each character in password if one is uppercase or numeric
    for i in password:
        if i == i.isupper():
            pass_upper = True
            continue
        if i == i.isnumeric():
            pass_num = True
            continue
        if pass_upper is True and pass_num is True:  # Breaks out of for loop if both credentials have been found
            break

    # tests if a special character is in password
    if "#" in password or "@" in password or "%" in password or "*" in password:
        pass_special = True

    # tests password length
    if len(password) > 7:
        pass_length = True

    if pass_upper and pass_num and pass_special and pass_length and user_email:
        return username, password
    else:
        return None, None


def secure_store(username, password):
    output_file = "credential.dat"
    fd = open(output_file, 'ra')

    # Encrypt w/ AES algorithm
    # encrypted_password=''
    # Output user/pass to credential.dat

    # If user/pass output to file correctly, display them
    print('Username: ' + username)
    print('Password: ' + password)
    print("username and password saved in " + output_file)


def main():
    valid_username, valid_password = getusername_paswd()
    if valid_username and valid_password:
        secure_store(valid_username, valid_password)


main()
