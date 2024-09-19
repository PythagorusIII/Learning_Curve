def is_armstrong_num(num):

    count = len(str(num))
    total = 0

    while(num != 0):
        digit = num % 10
        total += digit**count
        num = num // 10
    print(total)

    return True if num == total else False

is_armstrong_num(153)


