#a method of finding the greatest common divisor of two numbers by dividing
 #the larger by the smaller, the smaller by the remainder, the first remainder by the second remainder, 
 #and so on until exact division is obtained whence the greatest common divisor is the exact divisor.

def euclid_gcd(x, y):
 

    if x < y : 
        return euclid_gcd(x, y)

#We caluate GCD of the two intergers.  
    while y != 0:
     (x, y) = (y, x % y)

#Prints out the result from the GCD. 
    print("\n[+] GCD: {}".format(x))
    return x 

a = 66528 
b = 52920 

#results will be given by this methond.
euclid_gcd (a,b)


