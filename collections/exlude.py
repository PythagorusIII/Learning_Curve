lst = [2,3,4,5]

for i in range(0, len(lst)):
    sum = 0
    for j in range(len(lst), 0, -1):
        
        if i != j:
            
            sum = sum + lst[j]    
    print(sum)