year = int(input('Enter a year: '))

if year % 100 == 0:
    print(f'{year} is centuary year')
    
else:
    print(f'{year} is not a centuary year')