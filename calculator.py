a=float(input("enter a number"))
b=float(input("enter a number"))
print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division \npress 5 for percentege")
choice=int(input("enter your choice from 1-5:"))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b)
elif choice==5:
    print(a%b)
else:
    print("invalid input")