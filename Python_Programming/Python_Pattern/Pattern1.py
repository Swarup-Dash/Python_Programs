def star(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ", end="") 
        print("\n")  
n=int(input("Enter range"))
star(n) 