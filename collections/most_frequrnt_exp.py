expence = [12000, 14000, 12000, 7000]

check = []
count = 0

for i in expence:

    if i != check:

        check.append(i)

    else:

        count+=1

print(count)
