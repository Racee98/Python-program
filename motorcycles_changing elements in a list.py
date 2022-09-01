#most list you create will be dynamic
#dynamic list mean you can add and remove elements
#when cganging an element in a list , use the name of t he list followed by index(position)of the element that you what to change
#after that you then provide the new value you want that item to have
#changing an item in a list will be shown below
motorcycles=['Honoda','Yamaha','Suziki']
print(motorcycles)
motorcycles[0]='Ducatti'
print(motorcycles)
#there are several ways you can add new elements to a lists
#the simplest way to add and element to a list is to append the item to the list
#when you append an item to a list it is addedto the end of the list
#in the example below i will appemd an item to a list
#to append an item use .append('item')shown in example below
motorcycles=['Honoda','Yamaha','Suziki']
motorcycles.append('Ducatti')
print(motorcycles)
#the append method allows you to build list dynamically
# you can start with an empty list and elements
# shown in the example below
motorcycles=[]
motorcycles.append('Honda')
motorcycles.append('Yamaha')
motorcycles.append('Suzuki')
print(motorcycles)
#you can also insert elements into a list
#to insert elements into  list use the insert method shown below
# to use the insert method you must type .insert(0,'Ducatti') this is an example any numberor elemnet may be used
motorcycles=['Honda', 'Yamaha','Suzuki']
motorcycles.insert(0,'Ducati')
print(motorcycles)
#you can also remove an item or items from a list
#you can remove an item using the del method an example would be shown below
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
# you can remove any item from a list using the del method
#to remove the second item within the abovoe list you would put del motorcycles[1]
#in both examples ofremoving an item from the list you cand no longer acces the value

# the pop() method can alsobe used to remove an item from the end of a list
#the pop allows you to remove a item and stillbe able to use it
#the pop()method will be shown in an example below
#to pop an item from a list start by defining and printing the list of motorcycles
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
# pop the value from the list and store the value under a variable

popped_motorcycles=motorcycles.pop()
#print the  list to ensure  the value has been removed from the list 
print(motorcycles)
#to prove we still have access to the value that was removed print the variable that stores the popped value
print(popped_motorcycles)
#in an example below we will use  the pop method to say what the last motorcycle we brought
motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(1)
print(f" the last motorcycle I owned was a {first_owned.title()}.")
#when popping an item from any position u can use  the pop() put  the item you want to remove in the parenthesis

first_owned=motorcycles.pop(0)
print(f"the first motorcycles I ever owned was a {first_owned.title()}.")
#remember each time you use pop the item is no longer stored in the list
# deciding between using del or pop is pop you can remove  the item and still you it

#sometimes you will not know the position of an item you want to remove
# if you only know the value of an item you want to remove you can use the remove method
#for example remove the Ducati value below
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
#you can also use the remove method to work with a value thats being removed from the list
#in the example below we are going to remove ducati from the list and print a reason for removing it
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"/nA {too_expensive.title()} is  to expensive for me")
#below create a list of people you would like to invite to dinner then print a message to each person inviting them
dinner_list=['zay','rob','domo']
print(dinner_list)
print(f" {dinner_list[0]}, would you like to come to the dinner?")
print(f" {dinner_list[1]}, would you like to come to the dinner?")
print(f" {dinner_list[2]}, would you like to come to the dinner?")
#one of the guest cant make it so send out a new set of invitations
print(f"{dinner_list[0]} can not make it to the dinner")
dinner_list[0]='tae'
print(dinner_list)
#print a second set of invitations to each person who is on the new list
print(f" Hello {dinner_list[0]}, would you like to come to my dinner?")
print(f"hey {dinner_list} we have found a bigger venue so more people will be getting an invite")
#use the insert method to add guest at the beginning and middle of the list
#use the append method to add a guest at the end of your list
print(dinner_list)
dinner_list.insert(0,'Jay')
print(dinner_list)
dinner_list.insert(2,'cee')
print(dinner_list)
dinner_list.append('zee')
print(dinner_list)
print(f" Hello {dinner_list[0]}, would you like to attend my dinner?")
print(f" Hello {dinner_list[1]}, would you like to attend my dinner?")
print(f" Hello {dinner_list[2]}, would you like to attend my dinner?")
print(f" Hello {dinner_list[3]}, would you like to attend my dinner?")
print(f" Hello {dinner_list[4]}, would you like to attend my dinner?")
print(f" Hello {dinner_list[5]}, would you like to attend my dinner?")

