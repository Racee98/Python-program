#list are a collection of items in a particular order
#you can make a list of the alphabet, nunmbers  0-9, or the names of people
# you can put anything you want in a list
#the items in a list do not have to be related
# its always a good idea to make the name of your list plural since  they will contain more than one element
# in python square brackets indicate list  []
bicycles= ['trek','cannondale','redline','specialized']
print(bicycles)

#accessing idividual items in a list example shown below , items start with the nnumber 0
print(bicycles[0])
#the example above is what you want your users to see
# you can makethe output more neat by using the title methodo example shown below
print(bicycles[0].title())
#python considers the first item in the list to be 0 not 1
print(bicycles[1])
#the example above would print cannondale
# to get the last item of a list type -1 example shown below
print(bicycles[-1])
#n-2 return the second from last item in a list
#-3 return the third from last item on a list
# you can use individual values from a list as you would any other variables
# for example you can use f-strings to create a message based on a value from a list
#below we will pullthe first bicycle from the list and compose a message
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

names=['Domo','Zay', 'Cee']
print(names)
print(names[0])
print(names[1])
print(names[-1])
mesage= f"Hello {names[0]},how are you doing ?"
print(mesage)
favorite_transportation=['Sedan','Coupe','Truck','Motorcycle']
print(favorite_transportation)
message= f"My dream car is a BMW i8 {favorite_transportation[1].lower()}"
print(message)
message=f"I would love to have a Toyota {favorite_transportation[-1]}"
print(message)
