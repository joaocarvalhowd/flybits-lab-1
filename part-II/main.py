import os

PRIME_NUMBER_LOWER = int(os.getenv('PRIME_NUMBER_LOWER'))
PRIME_NUMBER_UPPER = int(os.environ.get('PRIME_NUMBER_UPPER'))

for num in range(PRIME_NUMBER_LOWER,PRIME_NUMBER_UPPER + 1):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)
