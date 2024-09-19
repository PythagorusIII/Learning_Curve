num = int(input('Enter a number:'))

if num % 15 == 0:
    print('FIZZBUZZ')

elif num % 5 == 0:
    print('BUZZ')

elif num % 3 == 0:
    print('FIZZ')

else:
    print(f'{num} is invalid number')


    # if 15 it is ivisible by