
runProgram = True
name = input("What is your name?")

while runProgram:
    print(f"Welcome {name}!")
    number = int(input("Enter an integer between 1 and 100 for me to analyze."))

    # odd
    if (number % 2 != 0):
        if (number >=1 and number < 60):
            print(f"The number {number} is odd and less than 60.")

        else:
            print(f"The number {number} is odd and greater than 60.")



    # even
    elif(number % 2 == 0):
        if(number >=2 and number <= 24):
            print(f"The number {number} is even and less than 25.")

        elif(number >=26 and number <= 60):
            print(f"The number {number} is even and between 26 and 60 inclusive.")

        else:
            print(f"The number {number} is even and greater than 60.")


    #out of range
    elif(number <=0 or number > 100):
        print(f"{number} is not a valid choice. Please enter a number between 1 and 100 inclusively {name}.")

    #not number
    else:
        print(f"{number} is not a valid choice. Please enter a number between 1 and 100 inclusively {name}.")

    while runProgram:
        response = input("Would you like to analzye another number? (y / n").lower()
        if(response == "y"):
            runProgram = True
            break
        elif(response == "n"):
            runProgram = False
            print("Have a good day!")
            break
        else:
            print(f"{response} is not a valid entry. Y or N only")






