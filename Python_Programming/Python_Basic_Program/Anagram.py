def check(s1, s2):
    if(sorted(s1)==sorted(s2)):
        print("Anagram")
    else:
        print("Not Anagram")
s1=input("Enter String1: ")
s2=input("Enter string2: ")
check(s1, s2) 