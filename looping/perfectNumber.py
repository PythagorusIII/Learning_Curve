num = int(input('Enter a number: '))
total = 0
for i in range(1, num):
    if num % i == 0:
        total += i

print('perfect number ') if total == num else print('not perfect')