num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))
sort = []

if num1 < num2  and num1 < num3:
    sort.append(num1)
    if num2 < num3:
        sort.append(num2)