num = int(input('Enter the number: '))

last_digit = num % 10

print(last_digit)

is_even = last_digit % 2

print('even:',is_even == 0) 
print('odd',is_even != 0) 