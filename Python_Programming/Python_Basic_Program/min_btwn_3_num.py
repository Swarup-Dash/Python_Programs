def minimum(a, b, c):
    if(a<b) and (a<c):
        smalest=a
    elif(b<a) and (b<c):
        smalest=b
    else:
        smalest=c
    print("Smalest is",smalest)
a=int(input())
b=int(input())
c=int(input())
minimum(a, b, c)

