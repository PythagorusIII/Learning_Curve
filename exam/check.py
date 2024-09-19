num = int(input('Enter a number: '))

original = num
total = 0
count = len(str(num))

while(num!=0):
    digit = num % 10

    total += digit**count

    num = num // 10

print(total)
if total == original:
    print('is armstrong')
else:
    print('not armstrong')

state = False
for i in range(2, original):
    if(original % i) == 0:
        state = True
    elif original % original == 0:
        state = True

if state == True:
    print('is prime')
elif state == False:
    print('not prime')

