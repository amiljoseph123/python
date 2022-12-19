a=input("Enter the first number:")
b=input("Enter the second number:")
c=input("Enter the third number")
print("The greatest number is:")
if((a>b)and(a>c)):
    print(a)
else:
    if(b>a)and(b>c):
        print(b)
    else:
        print(c)
