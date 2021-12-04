#author: johannes tafferner
#date: 04.12.2021
#version: 1.0
#python version: 3.6


#tldr: sum of even fibonacci numbers <= 4,000,000


def listFibonaccisBelowThreshold(threshold = 4000000):
	
	#initializing the first to values that are required to calculate all consecutive fibonacci numbers
	previous = 0
	fibonacci = 1
	
	listOfEvenFibonaccis = []
	
	while True:
		
		temp = fibonacci #temporary storing value of num2
		
		fibonacci = previous + fibonacci #calculating next fibonacci number by summing the previous two
		
		previous = temp #shifting initial values to the next two numbers
		
		if fibonacci > threshold:
			return listOfEvenFibonaccis
		
		listOfEvenFibonaccis.append(fibonacci)
		
#now we need the sum of all even numbers returned by the previous function
		
sumOfEvenFibonaccis = sum(x for x in listFibonaccisBelowThreshold() if x % 2 == 0)

print(sumOfEvenFibonaccis)