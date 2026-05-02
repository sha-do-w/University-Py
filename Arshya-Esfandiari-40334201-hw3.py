# name     : Arshya Esfandiari
# uni ID   : 40334201
# homework : 3
# problem  : write a program to calculate the Fibonacci series base on the number of members that user wants.
# ---------------------------------------------------------------------------------------

# The Title
print("########## Fibonacci Sequence ##########")

ChangeMode = True # For choosing the model of Fibonacci sequence
ExitApp = False # The condition for closing console app

while not ExitApp :
    print("\n****** Start ******")

    # Choose The Mode
    if ChangeMode == True :
        print("\nWhat Model do you want to work with ?")
        print("0 = 0 , 1 , 1 , 2 , 3 , ...")
        print("1 = 1 , 1 , 2 , 3 , 5 , ...")
        ChangeMode = False # Disables Model Change unless the user wants
        while True :
            UserInput = input("> ")
            if UserInput == "0" : # Starts with ````0
                TheModel = 0
                break
            elif UserInput == "1" : # Starts with 1
                TheModel = 1
                break
            else : # Error
                print("ERROR! Invalid Format or Number!")
    
    print("\nType a number to get the Fibonacci sequence up to that number :")

    # Taking number from user
    while True :
        UserInput = input("> ")
        if UserInput.isdigit(): # if the input is just a positive number
            if (TheModel == 1 and UserInput == "0") :
                print("ERROR! The model is 1 but your number is 0!")
            else :
                TheNumber = int(UserInput)
                break
        else :
            print("ERROR! Invalid Number or Format!") # if its negative or zero number or even not a number
    
    # Setting the first two terms of Fibonacci sequence based on the model
    if TheModel == 0 :
        FiboSeq = [0,1]
    else :
        FiboSeq = [1,1] 

    # Calculate the Fibonacci sequence terms
    while len(FiboSeq) >= 2 :
        SumOfTwo = FiboSeq[-2] + FiboSeq[-1]
        if SumOfTwo > TheNumber :
            break
        FiboSeq.append(SumOfTwo)
    
    # Display the result ( The sequence )
    print(f"\nThe Fibonacci sequence before the number {TheNumber} is :")
    for i in range(len(FiboSeq)) :
        if FiboSeq[i] <= TheNumber :
            print(f"{FiboSeq[i]}", end = "")
            if i != len(FiboSeq)-1 and FiboSeq[i+1] <= TheNumber : # For last term of sequence
                print(" , ", end = "")

    # Options after finishing task
    print("\n\n****** The End ******\n")
    print("Please choose an option.")
    print("c = CHANGE MODE AND RESTART\nr = JUST RESTART\ne = EXIT")
    while True :
        UserInput = input("> ")
        if UserInput == "c" :   # Restart and let user change the model
            ChangeMode = True
            break
        if UserInput == "r" :   # Restart
            break
        elif UserInput == "e" : # Exit
            ExitApp = True
            break
        else :                  # Error
            print("ERROR! Invalid Format or Letter!")
