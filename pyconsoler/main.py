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


class User:
    def __init__(self, name, AccessLevel, exp, ISADMIN, Position, SecAns, pword):
        self.name = name
        self.AccessLevel = AccessLevel
        self.exp = exp
        self.ISADMIN = ISADMIN
        self.Position = Position
        self.SecAns = SecAns
        self.pword = pword
        self.numattempts = 0

# End of dictionaries

local_username_database = [
    "Admin",
]

global_username_database = []

# functions


def levelup(spam):
    need = spam.AccessLevel * 10
    while spam.exp >= need:
        spam.AccessLevel += 1
        print("User Access Level Increased!")
        spam.exp -= need
        need = spam.AccessLevel * 10
    return spam


def stats(spam):
    print("")
    print("")
    print("Name: " + spam.name)
    print("Access Level: {}".format(spam.AccessLevel))
    print("Position: " + spam.Position)
    print("")
    print("")
    
    
def printWord(word):
  for letter in word:
    print(morse[letter.upper()])
    
# End of functions

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

user = User("", 1, 0, False, "Temp", "", " ")
time.sleep(1)
for i in local_username_database:
    if i == user.name:
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
    local_username_database.append(user.name)

operating = True
while operating:  # Start of the main loop

    stats(user)
    usrInp = input("What is your command? " + user.Position + ">")
    time.sleep(1)
    if usrInp == 'q' or usrInp == "quit":    
        operating = False    
    elif usrInp == 'h' or usrInp == "help":
        time.sleep(1)
        print("Command Helper v1")
        print("q or quit to exit. Please make sure all work is finalized!")
        print("mail to access mail.")
        print("Please email IT if you are experiencing any bugs. IT@here.com")    
    elif usrInp == "mail":
        print(" ")    
    else:
        print("Invalid Command!")
