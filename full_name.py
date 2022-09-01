first_name="ada"
last_name="lovelace"
full_name= f"{first_name} {last_name}"
print(full_name)
#to insert a variables value into a string put f before the quotation mark
# then place brackets around the name or names of the  variable 


print(f"hello,{full_name.title()}!")
#the title method is  used to change a  name to title case  
#the above statement is an example of using and f string to compose complete messages usinng the associated variables
message= f"Hello,{full_name.title()}!"
print(message)
#above is an example of using f strings to compose a message then assign the   entire message to a variable


#whitespace refers to any non printing character such as spaces tabs or end of line symbols
#to add toyour text use \t as shown below
print("\tPython")

# to add a new line in a string use \n as shown below
print("Languages:\nPython\nC\nJavaScript")

#to combine tabs and newlines in a  single string use the string "\n\t" shown below

print("languages:\n\tPython\n\tC\n\tJavaScript")
# the rstrip method is used to eliminate whitespaces in python
# the r strip method is used like this .rstrip()for the right side .lstrip for the left side or use strip() for both sides example shown below
favorite_language=' Python '
favorite_language.rstrip()')

