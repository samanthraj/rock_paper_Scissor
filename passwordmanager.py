import hashlib
password_file = open("password.txt","a+")

def setting_master():
    while True:
        password = input("enter your password:  ")
        hashed = hashlib.sha256(password.encode()).hexdigest()
        master_file = open("master.txt", "a")
        master_file.write(hashed)
        break
    master_file.close()

def read_file():
    username = input("enter username:  ")
    password_file.seek(0)
    for line in password_file.readlines():
        (user,pas) = line.split("|")
        if user == username:
           print(pas)
        else:
           print("")
def write_file():
    username = input("enter username:  ")
    password = input("enter password:  ")
    password_file.write(username+"|"+password+"\n")

print("Welcome to Password manager")
while True:
    mode = input("do you want to set masterpassword or view passwords or write passwords, options are master,write,read or q for quit   ")
    if mode == "master":
        setting_master()
        continue
    elif mode == "write":
        write_file()
        continue
    elif mode == "read":
        read_file()
        continue
    elif mode == "q":
        break


password_file.close()




