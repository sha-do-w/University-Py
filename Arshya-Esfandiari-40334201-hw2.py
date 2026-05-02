# name     : Arshya Esfandiari
# uni ID   : 40334201
# homework : 2
# problem  : write a program to take a number and check if it is PRIME or COMPOSITE.
# ---------------------------------------------------------------------------------------

print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
print("⬜        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜   ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
print("⬜   ⬜⬜   ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
print("⬜   ⬜⬜   ⬜⬜   ⬜   ⬜⬜⬜   ⬜⬜             ⬜⬜⬜        ⬜⬜")
print("⬜        ⬜⬜      ⬜⬜⬜⬜   ⬜⬜   ⬜⬜   ⬜⬜   ⬜⬜   ⬜⬜⬜⬜   ⬜")
print("⬜   ⬜⬜⬜⬜⬜⬜⬜     ⬜⬜⬜⬜⬜   ⬜⬜   ⬜⬜   ⬜⬜   ⬜⬜         ⬜⬜")
print("⬜   ⬜⬜⬜⬜⬜⬜⬜   ⬜⬜⬜⬜⬜⬜⬜   ⬜⬜   ⬜⬜   ⬜⬜   ⬜⬜   ⬜⬜⬜⬜⬜⬜⬜⬜")
print("⬜   ⬜⬜⬜⬜⬜⬜⬜   ⬜⬜⬜⬜⬜⬜⬜   ⬜⬜   ⬜⬜   ⬜⬜   ⬜⬜⬜       ⬜⬜⬜")
print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
AppExit = False
while AppExit == False :
    print("Please enter your integer :")

    while True :
        try :
            UserInput = input()
            TheNumber = int(UserInput)
            break
        except ValueError :
            print("What is math , Einstein ?!")

    if TheNumber == 2:
        print("Your number is PRIME!")
    else:
        IsPrime = True
        i = 3
        Limit = int(TheNumber**(1/2)+1)
        if TheNumber%2 !=0 :
            while i < Limit :
                if TheNumber%i == 0:
                    IsPrime = False
                    break
                else:
                    i+=2
        else:
            IsPrime = False
            i=2
        if IsPrime==True:
            print("Your number is PRIME!")
        else:
            print("Your number is COMPOSITE!")
            print(f"The first divisor is {i}.")
            print("Do you want to find all divisors ?")
            print("y = yes\t\tn = no")
            while True :
                UserChoice = input()
                if UserChoice == 'y' :
                    TheDivisors = {i, int(TheNumber/i)}
                    while i < Limit :
                        if TheNumber%i == 0 :
                            TheDivisors.update([i, int(TheNumber/i)])
                        i+=1
                    print(f"All of the divisors are :\n{sorted(TheDivisors)}")
                    break
                elif UserChoice == 'n' :
                    break
                else :
                    print("Wrong option or format!")
            

    print("What now ?")
    print("r = restart\t\te = exit")
    while True :
        UserChoice = input()
        if UserChoice == 'r' :
            break
        elif UserChoice == 'e' :
            AppExit = True
            break
        else :
            print("Wrong option or format!")

# print("Your number is PRIME!" if IsPrime==True else "Your number is COMPOSITE!")

