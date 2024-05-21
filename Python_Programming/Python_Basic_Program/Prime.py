n1=int(input("Enter a number"))
n2=False
if n1>1:
    for i in range(2, n1):
        if(n1%i)==0:
            n2=True
            break
if n2:
    print(n1,"is not prime")
else:
    print(n1, "is prime")