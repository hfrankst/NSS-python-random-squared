import random

random_numbers = list() 
for i in range (20):
	random_numbers.append(random.randrange(0, 49, 2))

print(len(random_numbers))
print(random_numbers)
