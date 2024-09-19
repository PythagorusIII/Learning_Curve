arr = [2,3,4,5]

sum = 7

for i in range(0, len(arr)-1):

    for j in range(i+1,len(arr)):

        if arr[i] + arr[j] == sum:
            print(f'{sum} is the sum of {arr[i]} and {arr[j]}')
            break
        else:
            pass
