import math

a=float(input("Enter coefficient a: "))
b=float(input("Enter coefficient b: "))
c=float(input("Enter coefficient c: "))

#Discriminent b**2-4ac

discriminent=b**2 - 4*a*c

if discriminent>0:
    alpha=(-b + math.sqrt(discriminent) )/ (2*a)
    bita=(-b - math.sqrt(discriminent) )/ (2*a)
    print(f"Alpha :{alpha}")
    print(f"Bita :{bita}")
    
elif discriminent==0:
    alpha_beta=-b/(2*a)
    print(f"Alpha_beta is {alpha_beta}")
    
else:
    real_part= -b/(2*a)
    imaginary_part = math.sqrt(abs(discriminent))/(2*a)
    print(f"Alpha: {real_part} + {imaginary_part}i")
    print(f"Bita: {real_part} + {imaginary_part}i")