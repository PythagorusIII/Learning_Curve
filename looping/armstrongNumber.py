num = int(input('Enter a number: '))

original = num
total = 0
count = len(str(num))

while(num != 0):

    digit = num % 10

    total += digit**count

    num = num // 10

print(f'total is: {total}')
print(f"{original} is an armstrong number" if total == original else f"{original} is not an exponent")
