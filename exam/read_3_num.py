num1 = int(input('Enter first numbers: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
sort = []

if num1 > num2 and num1 > num3:
    print(f'{num1} is the largest number')
elif num2 > num1 and num2 > num3:
    print(f'{num2} is the largest number')
else:
    print(f'{num3} is the largest number')

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f'{num2} is the second largest number')
    else:
        print(f'{num3} is the second largest number')

elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f'{num1} is the second largest number')
    else:
        print(f'{num3} is the second largest number')

elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print(f'{num1} is the second largest number')
    else:
        print(f'{num2} is the second largest number')

if num1 < num2  and num1 < num3:
    sort.append(num1)
    if num2 < num3:
        sort.append(num2)
        sort.append(num3)
    else:
        sort.append(num3)
        sort.append(num2)

if num2 < num1  and num2 < num3:
    sort.append(num2)
    if num1 < num3:
        sort.append(num1)
        sort.append(num3)
    else:
        sort.append(num3)
        sort.append(num1)

if num3 < num1  and num3 < num2:
    sort.append(num3)
    if num1 < num2:
        sort.append(num1)
        sort.append(num2)
    else:
        sort.append(num2)
        sort.append(num1)
        
print(sort)