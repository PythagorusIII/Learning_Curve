def smart_sub(num1, num2 , reverse = True):

    if reverse == False:
        return num2 - num1
    
    else:
        return num1 - num2

print(smart_sub(2,3, False))