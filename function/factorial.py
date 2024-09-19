def fact(num):
    fact = 1
    for i in range(1, num+1):
        fact =fact * i
    return fact


num = int(input("enter a number:"))

result = fact(num)

print(result)
