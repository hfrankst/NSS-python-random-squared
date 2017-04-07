import random

random_numbers = list() 
for i in range (20):
	random_numbers.append(random.randrange(0, 49, 2))

print(len(random_numbers)) #making sure that the list has 20 numbers in it
print(random_numbers) #the list of random numbers

square_list = [i**2 for i in random_numbers] #the double asterisk is the squaring math function
print(square_list)
