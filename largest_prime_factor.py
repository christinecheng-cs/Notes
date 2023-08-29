'''
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143

Source: ProjectEuler
'''

def largest_prime_factor(n):
  i = 2
  while n <= i:
    if n % i == 0:
      return i
    i = i + 1
return n
