'''
Author: Naresh Adhikari, Sru
This is a skeletal program that students need to implement the declared
and defined functions under @TODO annotation, according to the logic/functional requirements stated in assigment-2.pdf.

Students are not expected to midify main() function.
'''
import hashlib
def secure_hashed_passwd(username, passwd):
    import hashlib, uuid
    import os

    '''
    @TODO: Students are required to implement this function.
    using salt+paper+sha3-224 algorithm
    :param username: string repr of username
    :param passwd: a plain text password
    :return: True if given values are stored successfully in outfile var; else returns False
    '''

    s = hashlib.sha3_224()  # initializes the hash algorithm
    salt = uuid.uuid4().bytes  # Add salt
    pepper = uuid.uuid4().bytes  # add pepper
    salt_peppered_passwd = salt + pepper + bytes(passwd, 'utf-8')
    salt_peppered_passwd = bytes(salt_peppered_passwd, 'utf-8')

    print(salt_peppered_passwd)
    s.update(salt_peppered_passwd)

    return salt, pepper, s.hexdigest()  # return salt, pepper, saltpepperdigest


def verify_hashed_passwd(username, passwd):
    '''
    @TODO: Students are required to implement this function.

    Server side verifies login credentials username and password
    :param username:
    :param hpasswd:
    :return:
    '''
    infile="hlogins.dat"    #databse file with username and hashed-password.
    fd=open(infile,"r")     #open the file to read
    s = hashlib.sha3_224()  #initialize hashing algorithm
    match = False

    for line in fd:
        list = line.split(',')
        if list[0] == username:
            match = True
            salt = list[1]
            pepper = list[2]
            hashedPassword = list[3]

            tempo_hash = s.update(salt+pepper+passwd)
            print(line)

    if match:
        if tempo_hash == hashedPassword:
            return True
    else:
        print("Authentication unsuccessful!")
        return False

    #To read the file line by line, use a for loop.
    #Hint: split each line by a comma "," to get list of username, salt, pepper, and stored_hashpassword values.
    #implement other logics inside loop.
    fd.close()  #Closes file to reallocate resources

def main():
    '''Do not modify this function.'''

    import hashlib, uuid
    import os

    lusername=["shyamal@gmail.com",
                "brutforce@yahoo.com",
                "lifegivesalot@protonmail.com",
                "rainbow@sru.edu",
                "ghana@makai.com",
                "david@inst.edu",
                "buttlerbusiness@sru.edu",
                "myChurch45@state.edu"]
    lpasswd=["pass$1290Red",
            "fail$567Blue",
            "rainB0w159$",
            "lglot$$$Tatoo",
            "ghana456$$909",
            "DavI0234$09",
            "IsBulltop345",
            "xCrosTop24"]

    # open file outfile in write mode.
    outfile="hlogins.dat"
    fd = open(outfile, "w+")
    #@server: call method for each usernames, passwords.
    for i in range(0,len(lusername)):
        username=lusername[i]
        passwd=lpasswd[i]
        salt,pepper,saltpepperdigest=secure_hashed_passwd(username,passwd)
        if i in [3,7,1]:continue
        fd.write(username + "," + str(salt) + "," + str(pepper) + "," + saltpepperdigest+","+"$\n")
    fd.close()

    for j in range(0,len(lusername)):
        uname=lusername[j]
        passwd=lpasswd[j]
        result=verify_hashed_passwd(uname,passwd)
        if not result:
            print("<!> Login failed for user ",uname)
        else:
            print("Login succesful for user ",uname)

if __name__ == "__main__":
    main()