def last_digit(num1,num2):
    last1 = num1% 10
    last2 = num2%10
    if last1 >last2:
        print(f'{last1}')
    else:
        print(f'{last2}')
    
last_digit(128,154)