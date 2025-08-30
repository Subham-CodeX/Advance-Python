def fact(x):
    fac=1
    for i in range(1,x+1):
        fac*=i
    print(fac)

num = int(input("Enter number: "))
fact(num)