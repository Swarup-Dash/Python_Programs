def maximum(a, b, c):
    if(a>=b) and (a>=c):
        largest=a
    elif(b>=a) and (b>=c):
        largest=b
    else:
        largest=c
    print("Largest is",largest)
a=int(input())
b=int(input())
c=int(input())
maximum(a, b, c)

