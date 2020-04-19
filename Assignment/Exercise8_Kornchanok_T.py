print("---- Delivery for You ----")
usernameInput=input("Username : ")
passwordInput=input("Password : ")
a=159
b=149
c=139
if usernameInput=="Doggy" and passwordInput=="hong":
    print("Login Success")
    print("---- Welcom to Lovely Soft Drink ----")
    print("              Menu Today")
    print("1. Yuzu Honey Soda  159THB")
    print("2. Salt Thai Peach Soda  149THB")
    print("3. Cherry Pop Soda  149THB")
    print("4. Ginger Lemon  139THB")
    print("------------------------------------")
    userSelected1=int(input("Select your first drink number : "))
    if userSelected1==1:
        drinkNo=int(input("How many drink do you want? : "))
        result1=drinkNo*a
    elif userSelected1==2:
        drinkNo=int(input("How many drink do you want? : "))
        result1=drinkNo*b
    elif userSelected1==3:
        drinkNo=int(input("How many drink do you want? : "))
        result1=drinkNo*b
    elif userSelected1==4:
        drinkNo=int(input("How many drink do you want? : "))
        result1=drinkNo*c
    secondSelected=input("Additional drink?(Y/N):")
    if secondSelected=="Y":
        userSelected2=int(input("Select your second drink number : "))
        if userSelected2==1:
            drinkNo=int(input("How many drink do you want? : "))
            result2=drinkNo*a
        elif userSelected2==2:
            drinkNo=int(input("How many drink do you want? : "))
            result2=drinkNo*b
        elif userSelected2==3:
            drinkNo=int(input("How many drink do you want? : "))
            result2=drinkNo*b
        elif userSelected2==4:
            drinkNo=int(input("How many drink do you want? : "))
            result2=drinkNo * c
    else:
        result2=0
    print("------------------------------------")
    print("Total price : ",result1+result2,"THB")
    print("------------------------------------")
    print("           Let's drink!!")
    print("            Thank you")
else:
    print("Login Not Success")