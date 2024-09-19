#  range function = range(start, stop, step)

# 
start = int(input('Enter the starting number: '))
end = int(input('Enter the ending number: '))

if start < end:
    for num in range(start, end+1, 1):
        print(num)

else:
    for num in range(start, end-1, -1):
        print(num)