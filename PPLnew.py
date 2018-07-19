#asks for name and password, if both are correct then the user will be asked if they want the contents 
#of a text file to be printed, if not, it exits the programme. If user enters an invalid name or password
#they will be asked if they want to try again and if they do, the programme will loop to the beginning.

def main():

    print("\nWelcome.\n")
    name = input("Please enter your name: ").capitalize()
    password = input("Please enter your password: ")

    if name == "Smith" and password == "Peanuts":
        print("Welcome, Smith!")
        content = input("The contents of Test.txt will be printed. Would you like to go ahead?: ")
        if content.startswith("y"):
            print("-" * 30)
            f=open("Test.txt", "r")
            if f.mode == "r":
                contents = f.read()
                print(contents)
        else:
            exit()
    else:
        startagain = input("That is an invalid name/password. Would you like to try again?: ")
        if startagain.startswith("y"):
            main()
        else:
            exit()

main()