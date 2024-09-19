num = int(input('enter a number: '))

flag = True

for i in range(2, num):
    flag = True if num % i == 0 else False
    if flag == True:
        print('not prime')
        break
    print('is prime')
    break

is_prime = True

for i in range(2,num):
    if num % i == 0:
        is_prime = False
        break
print(is_prime)



