#Write a program to determine if a number, given on the command line, is prime.

#Example 1

from rsa import prime

def prime_erastosthenes(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print (i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)

print(prime_erastosthenes(200));

#Example 2

def SieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): # If prime[p] is not changed.
            for i in range(p * 2, n + 1, p):  # Update all multiples of p
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
   
    for p in range(n + 1):  # Print all prime numbers 
        if prime[p]: 
            print (p), 
    
    # driver program 
    if __name__=='__main__': 
        n = 30
        print ("The prime smaller"), 
        print ("than or equal to"), n 
        SieveOfEratosthenes(n)

#Example 3
#Only select teh list of continen the prime numbers.
#1. Make a list of all numbers from 2 to n.
#2. Stargint from 2, delete all of its multiples in the list, except itself.
#3. Repeat the step 2 till square root of n.
#4. The remaining list only contains prime numbers.

import math


print ("Enter the a number")
number = int(input())

primes = []
for i in range(2,number+1):
    primes.append(i)
i = 2
while(i <= int(math.sqrt(number))): 
    if i in primes:
        for j in range(i*2, number+1, i):
            if j in primes:
                primes.remove(j)
    i = i+1
print (primes)