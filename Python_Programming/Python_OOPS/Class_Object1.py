class Parrot:

    # class attribute
    name = ""
    age = 0

# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")

'''In the above example, we created a class with the name Parrot with two attributes: name and age.
Then, we create instances of the Parrot class. Here, parrot1 and parrot2 are references (value) to our new objects.
We then accessed and assigned different values to the instance attributes using the objects name and the . notation.'''



'''The letter "f" in front of the string indicates that it is an f-string. An f-string, or formatted string literal,
is a way to embed expressions inside string literals, using curly braces {}.
The expressions inside the curly braces are evaluated at runtime and their results are formatted 
using the specified format.
In this case, the f-string is used to create a formatted string that includes the values of the 
name and age attributes of the parrot1 object. It's a concise and readable way to include variable values or expressions in a string without explicitly using concatenation or other string formatting methods.
'''