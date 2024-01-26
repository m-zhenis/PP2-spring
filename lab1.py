#SYNTAX
#1
print("Hello World")

#2
if 5>2:
    print("YES")


#COMMENTS
#1
  #This is a comment
    
#2
'''
    This is a comment
written in 
more than just one line
'''

#VARIABLES
#1
carname = "Volvo"

#2
x = 50

#3
x = 5
y = 10
print(x+y)

#4
x = 5
y = 10
z = x + y
print(z)

#5
x,y,z = "Orange", "Banana", "Cherry"

#6
x = y = z = "Orange"

#7
def myfunc():
    global x
    x = "fantastic"




#DATA TYPES
#The following code example would print the data type of x, what data type would that be?   
   
#1
x = 5
print(type(x))
#answer: int

#2
x = "Hello World"
print(type(x))
#answer: str

#3
x = 20.5
print(type(x))
#answer: float

#4
x = ["apple", "banana", "cherry"]
print(type(x))
#answer: list

#5
x = ("apple", "banana", "cherry")
print(type(x))
#answer: tuple

#6
x = {"name" : "John", "age" : 36}
print(type(x))
#answer:dict

#7

x = True
print(type(x))
#answer: bool

#NUMBERS
#1
x = 5
x = float(x)

#2
x = 5.5
x = int(x)

#3
x = 5
x = complex(x)


#STRINGS
#1
#Use the len function to print the length of the string.
x = "Hello World"
print(len(x))

#2
#Get the first character of the string txt.
txt = "Hello World"
x = txt[0]

#3
#Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]

#4
#Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()

#5
#Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()

#6
#Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()

#7
#Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H","J" )

#8
#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {} "
print(txt.format(age))
