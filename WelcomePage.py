def welcome():
    '''This Function Creates A Welcome Page For Our Gaming App'''
    for i in range(0, 20):
        print("*\t", end="")
    print()
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 8):
        print("\t", end="")
    print("WELCOME", end="")
    for i in range(0, 10):
        print("\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*")
    for i in range(0, 20):
        print("*\t", end="")
    print()
    input("Press any key to start:")

def mainmenu():
    print("1.Rock Paper Scissors\n2.Cows And Bulls\n3.Exit")
    ch=int(input("Enter your choice number"))
    if ch==1:
        rockpaperscissorsmenu()
    elif ch==2:
        cowsandbullsmenu()
    elif ch==3:
        print("ERROR EEROR\nOOOOOOOF")
        exit()

def rockpaperscissormenu():
    print("1.Play\n 2.Rules\n  3.Return to Main Menu")
    ch = int(input("Enter your choice number"))
    if ch == 1:
        rockpaperscissors()
    elif ch == 2:
        rockpaperscissorsrules()
    elif ch == 3:
        mainmenu()


def cowsandbulls():
    print("1.Play\n 2.Rules\n  3.Return to Main Menu")
    ch = int(input("Enter your choice number"))
    if ch == 1:
        cowsandbulls()
    elif ch == 2:
        cowsandbullsrules()
    elif ch == 3:
        mainmenu()
def rockpaperscissors():
    print("Welcome to rock paper scissors")

welcome()
print("\n"*100)
mainmenu()