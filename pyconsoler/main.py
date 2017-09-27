import time


# Dictionaries

morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--"
}

user = {
    "name": "user",
    "Access Level": 1,
    "exp": 0,
    "IS ADMIN": False,
    "Position": "Temp",
    "Security Ans": " ",
    "pword": "",
    "Num attemps": 0,
}

local_username_database = [
    "Admin",
    "Overseer"
]

global_username_database = []

# functions


def levelup(spam):
    need = spam["Access Level"] * 10
    while spam["exp"] >= need:
        spam["Access Level"] += 1
        print("User Access Level Increased!")
        spam["exp"] -= need
        need = spam["Access Level"] * 10
    return spam


def stats(spam):
    print("")
    print("")
    print("Name: " + spam["name"])
    print("Access Level: {}".format(spam["Access Level"]))
    print("Position: " + spam["Position"])
    print("")
    print("")


print("")
time.sleep(1)
print("")
print("=======================================")
time.sleep(1)
print("       System Access Restricted        ")
time.sleep(1)
print("=======================================")
print("")
time.sleep(1)
print("")

print("")

newUser = True

user["name"] = input("User Name: ")
time.sleep(1)
for i in username_database:
    if i == user["name"]:
        print("Great")
        newUser = False
        break
    else:
        newUser = True

if newUser:
    print("")
    print("========NEW USER DETECTED!========")
    print("")
    time.sleep(1)
    username_database.append(user["name"])

operating = True
while operating: # Start of the main loop

    stats(user)
    usrInp = input("What is your command? " + user.["Position"] + ">")
    time.sleep(1)
    if usrInp == 'q' or usrInp == "quit":    
        operating = False    
    else if usrInp == 'h' or usrInp == "help":    
        time.sleep(1)
        print("Command Helper v1")
        print("q or quit to exit. Please make sure all work is finalized!")
        print("mail to access mail.")
        print("Please email IT if you are experiencing any bugs. IT@here.com")    
    else if userInp == "mail"
        print(" ")    
    else:
        print("Invalid Command!")
    

