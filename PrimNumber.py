"""
This is a program to find prime numbers with python, written by Thor Naughton
Project started: 04/06/2021
"""

def brutePrimes():
    startAt = int(input('Start search at (default is 0) :') or '0')
    upTo = int(input("End search at : "))

    

    #opens a file Primes.txt to write the prime numbers to
    with open('Primes.txt', 'w') as numFile:
        numFile.write('Prime numbers from {} to {}: \n'.format(startAt, upTo))
        #loops through all the numbers
        for num in range(startAt ,upTo+1):
            prime = True

            #checks if the number is prime.
            for i in range(2,num):
                if (num%i==0):
                    prime = False

            #Adds number to Primes.txt and prints the prime number to the console.
            if prime:
                numFile.write(str(num)+'\n')
                print(num)
                    



brutePrimes()

input('Press Enter to exit...')
