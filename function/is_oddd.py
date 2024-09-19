def is_odd(num):
    odd = True
    if num % 2 == 0:
        return False
    else:
        return True
    
num = int(input('enter a num'))

print(is_odd(num))
