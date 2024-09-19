num1 = 100
num2 = 200

print(f'\n numbers before swaping are {num1} And {num2}')

temp = num2
num2 = num1
num1 = temp

print(f'\n After swaping numbers are {num1} and {num2}')

print(num1, num2, temp)



num3 = 300
num4 = 400

print(f'\n numbers before swaping are {num3} And {num4}')

num3,num4 = num4,num3

print(f'\n After swaping numbers are {num3} and {num4}')



num5 = 500
num6 = 600

print(f'\n numbers before swaping are {num5} And {num6}')

num5 = num5 + num6      #
num6 = num5 - num6      # this is only aplicble for numbers
num5 = num5 - num6      #

print(f'\n After swaping numbers are {num5} and {num6}')

