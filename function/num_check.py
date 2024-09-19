def num_chk(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
num = int(input("enter a number: "))    
print(num_chk(num))