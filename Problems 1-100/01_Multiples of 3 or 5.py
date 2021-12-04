#author: johannes tafferner
#date: 04.12.2021
#version: 1.0
#python version: 3.6


#tldr: sum of all the multiples of 3 or 5 below 1000


#using a list comprehension with a sum function to solve the prolem
sum_of_multiples = sum(x for x in range(1000) if (x % 3 == 0) or (x % 5 == 0))

#same implementation using for loops
sum_of_multiples = 0
for x in range(1000):
	
	if x % 3 == 0 or x % 5 == 0:
		sum_of_multiples += x
		
print(sum_of_multiples)