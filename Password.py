Master_pwd = input("What is your master password? ")



def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " " + pwd + "\n")



while True:
    mode = input("Would you like to add a new password or view existing ones (view, add) or press Q to quit? ").lower()
    if mode == "q":
        break
    
    elif mode == "view":
        view()

    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
    
    