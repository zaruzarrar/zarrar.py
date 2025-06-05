medical=input("do you have any medical condition Y or N:")
attendance=float(input("enter your attendance:"))
if medical=="Y":
    print("you are allowed")
else:
    if attendance>=75:
        print("you are allowed")
    else:
        print("you are prohibited")

        
