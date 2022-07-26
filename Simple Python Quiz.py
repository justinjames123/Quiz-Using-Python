print(" *** Welcome To Justin's Quiz *** ")
Name = input("Enter Your Name: ")
print("Hey",Name,"Welcome To The Game")
print("Do You Wanna Play a Quiz?")
print("Press 1 For Yes \nPress 2 For No ")
intro = int(input("Enter Your Choice: "))

correct = 0
Incorrect = 0

if intro == 1:
    print("Let's Go", Name)
    print()
    Q1 = input("Q1. Who Is India's Prime minister? ")
    if Q1 == "narendar modi" or "Narendar Modi" or "Narendar modi" or "NARENDAR MODI":
        print("You are Right", Q1, "Is Our Prime minister ")
        print()
        correct += 1
    else:
        print("Sorry But", Q1, "Is Not Our Prime minister. ")
        print()
        Incorrect += 1

    Q2 = int(input("Q2. When Was The Internet Founded? "))
    if Q2 == 1960:
        print("You are Right The Internet Started at", Q2)
        print()
        correct += 1
    else:
        print("You are Wrong The Internet Didn't Start in", Q2)
        print()
        Incorrect += 1

    Q3 = input("Q3. Who is Called as The Rocket Man of India? ")
    if Q3 == "Abdul Kalam" or "abdul kalam" or "ABDUL KALAM" or "APJ Abdul Kalam":
        print("You are Right Mr.",Q3,"Is called as The Rocket Man of India")
        print()
        correct += 1
    else:
        print("You are Wrong", Q3, "is Not called as The Rocket Man of India")
        print()
        Incorrect += 1

    Q4 = int(input("Q4. What is The Minimum Age To Join The Arm Forces? "))
    if Q4 == 19:
        print("You are Right",Q4,"Is The Minimum Age To Join The Arm Forces")
        print()
        correct += 1
    else:
        print("You are Wrong",Q4,"Is Not The Minimum Age To Join The Arm Forces")
        print()
        Incorrect += 1

    Q5 = int(input("Q5. Which Is The Smallest Prime Number? "))
    if Q5 == 2:
        print("You are Right", Q5, "Is The Smallest Prime Number")
        print()
        correct += 1
    else:
        print("You are Wrong", Q5, "Is Not The Smallest Prime Number")
        print()
        Incorrect += 1

    print("The Number of Correct   Answers are: ", correct)
    print("The Number of Incorrect Answers are: ", Incorrect)
    print()
    print(f" *** Thank You For Playing {Name} *** ")

else:
    print("Get Lost", Name)
    exit()
