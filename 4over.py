x=int(input("Range of number"))
print("enter the elements")
for i in range (0,x):
    a=int(input())
    if(a>100):
        a="over"
        print(a)
    else:
        print(a)
