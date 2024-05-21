# GCD=Greatest commom divisor 
def find_gcd(a, b):
    while b:
        a=b
        b=a%b
    return a
n1=int(input("Enter 1st no: "))
n2=int(input("Enter 2nd no: "))
print("GCD of two number is",find_gcd(n1,n2))

