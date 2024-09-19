def multiplication_table(num, n = 10):

    for i in range(1,n + 1):

        # mult = num * i
        # print(mult)
        print(f'{i}*{num} = {i * num}')

# num = int(input("Enter the number: "))
# n = int(input("Enter the range: "))
multiplication_table(5, 20)