from os import system


users = {
    "brohithkr":{
        "name":"Rohith",
        "password":"Rohith@123"
    }
}

def is_valid_password(passw):
    if len(passw)<8:
        print("Length of password must be greater than or equal to 8")
        return False
    if passw.lower()==passw:
        print("Password must contain lowercase letters too.")
        return False
    if passw.upper()==passw:
        print("Password must contain lowercase letters too.")
        return
    containsNumeric = False
    containsSpecial = False
    for i in passw:
        if ord('0') <= ord(i) <= ord('9'):
            containsNumeric==True
    if not containsNumeric:
        print("Password must contains lowercase letters too.")
        return False

def is_unique_user(uname):
    if uname in users:
        return False
    else:
        return True

def is_user(uname,password):
    if uname not in users:
        print("Not  valid user!")
        return False
    elif users[uname]['password']!=password:
        print("Wrong password!")
        return False
    else:
        return True

def display_menu():
    print("Welcome to KMIT\n")
    print("1. Login\n2. Register\n3. Exit\n")
    print("Select one of following options:",end=" ")
    option = input()
    return int(option)



def login():
    username = input("Give a username:")
    password = input("Give a password:")
    if is_user(username,password):
        print(f"Welcome {users[username]['name']}. You have successfully logged in.\n\n")
        return True
    else:
        print(f"Login not successful. Please try again.\n\n")
        return False

def register():
    username = input("Please select a valid username: ")
    name = input("Please give your name: ")
    password = input("Please give a valid password: ")
    if is_unique_user(username):
        users[username]={
            "name":name,
            "password":password
        }
        return True
    else:
        return False


    


if __name__=="__main__":
    while(True):
        system("clear")
        option = display_menu()
        system("clear")
        if option==1:
            if login():
                break
        elif option==2:
            if register():
                continue
        elif option==3:
            print("Exiting")
            break
        else:
            print("Not a valid option.")
            system("clear")
        


