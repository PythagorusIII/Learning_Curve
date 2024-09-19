# limit = int(input('Enter the range: '))
# prev = 0
# current = 1
# next = 0 
# print(prev)
# print(current)

# for i in range(1,limit - 1):
#     next = prev + current
#     prev = current
#     current = next
#     print(next)


check = int(input('Enter your number: '))

prev = 0
current = 1
next = 0
flag = True
i = 0

while(flag == True):
    next = prev + current 
    prev = current
    current = next
    print(next)
    if next == check:
        flag == True
        break
    else:
        flag == False
print(f'{check} is fibonachi') if flag == True else print(f'{check} is not fibonachi')



