# this tutorial studies types
# variables have different types, which determines how much memory is given to it
# for example, on most systems, integers (ints) are given 4 bytes
# however, characters (chars) are given 1 or 2 bytes, depending on the encoding
# ASCII is one byte
# Unicode is two bytes
# these encodings are basically charts, mapping each number to a symbol, 
# such as a letter or puncuation mark
# a string is a collection of characters, so the size of a string is either
# 1 * the length(ASCII) plus one, or 2 * the length(Unicode) plus one
# you don't see the "plus one" much in python, however, in C and other languages, you usually do
# the "plus one" is called a terminating byte, represented as '\0'. It tells the program that it's the end of the string.

#this program takes a variable, and returns the type.

#written for python 3

variable = input("Give me a variable: ") # prints "Give me a variable: " and takes user input. stores it in "variable"
vartype = type(variable) #stores the result(return value) of the type function in "vartype"
print(vartype) #print the value of "vartype"
#try it with these values

# 3 
# Hello, World!
# 3.55555

#you'll notice each one returns "str", or string
#this is because user input from a keyboard is ALWAYS a string

#how to combat this?
#well, we could use the try/except statements

#try:
    #<code>
#except:
    #<code if the above code didn't work>

print("Trying again...")

try:
    variable = int(variable) #try to convert the variable to a integer
except:
    try:
        variable = float(variable) #if there was an error, then try to convert to float
    except:
        #if it reaches this point, it can't be converted to an int or a float, so it is a string
        pass # do nothing, business as usual


# now we'll print the type
vartype = type(variable) #set vartype to return value of type(variable)
print(vartype)


#play with it, you'll see it is correct, but it isn't printing very readable text

#we can fix this with if statements!! :D


print("That didn't look nice, here's some good output" + "\n") # prints the text, plus a '\n', which represents a new line. print() automatically adds a newline, but now we'll have two, which gives a nice break from a wall of text


if vartype == type(3): # type() will always return this weird text that changes based on type, so we can compare with type(constant) to check the type
    vartype = "Integer" # set the variable "vartype" to a String saying "Integer"
elif vartype == type("Hello, World!"):
    vartype = "String"
elif vartype == type(3.55555):
    vartype = "Float"
else: # if something goes wrong, give an error message
    vartype = "ERROR"

print(vartype) # show off the fancy type of our user input
