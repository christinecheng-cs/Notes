'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Source: ProjectEuler
'''

def smallestmultiple(input):
	for num in range(2,21):
		if input % num != 0:
			return False
	return True

input = 20
while True:
    if smallestmultiple(input):
		break
	else:
		input = input + 1
print input
