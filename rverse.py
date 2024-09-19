num = 145   
reverse = ""         

while(num != 0):

    digit = num % 10 

    reverse=reverse + int(digit)

    num = num // 10  
