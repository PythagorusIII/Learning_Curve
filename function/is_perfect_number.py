def is_perfect_number(num):
    total=0

    for i in range(1,num):

        if num % i == 0:
            total += i
    print(total)
    return True if total == num else False

is_perfect_number(6)