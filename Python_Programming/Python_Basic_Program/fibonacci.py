# Fibonacci: 0 1 1 2 3 5 8 13......
nterm=int(input("Enter number of term to print: "))
n1=0
n2=1
count=0
if nterm<0:
    print("please +ve number")
elif nterm==1:
    print("Fibonacci Sequency", nterm)
else:
    print("Fibonacci Sequence: ")
    while count<nterm:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1