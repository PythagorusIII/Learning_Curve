def is_prime(num):
    prime = True
    for i in range (2,num):
        if num % i == 0:
            prime = False
            break
        else:
            prime = True
    print("prime" if prime == True else "not prime" )

num = int(input("enter a number: "))

is_prime(num)