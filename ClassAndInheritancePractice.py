
#Defining a parent
class Restaurant:
    business = True
    phoneNumber = '123-456-7890'
    email = 'myrestaurant@aol.com'

#Desiging the first child 
class PizzaChain(Restaurant):
    cuisine = 'american'
    specialty = 'pizza'
    storeNumber = 345

#Designing the second child with some similiarities but also differences
class ThaiFood(Restaurant):
    cuisine = 'Thai'
    foodTruck = True

#Finally, showing that inheritance works!
#This first entry should print because email is part of the class definition
print(Restaurant.business)

#For these two, these properties are inherited from the parent Restaurant!
#If they don't print, then the inheritance was unsuccessful.
print(PizzaChain.phoneNumber)
print(ThaiFood.email)

#Success! These two children have inherited from Restaurant
