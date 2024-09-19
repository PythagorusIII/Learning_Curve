height_cm =  int(input('Enter youtr height: '))

height_m = height_cm / 100

weight = int(input('Enter you  weight: '))

BMI = weight / (height_m**2)
BMI = round(BMI)

print(f'your BMI is {BMI}')


if BMI < 19:
    print('You are Under weight')
elif 19 < BMI < 25:
    print('You are normal weight')
elif 25 < BMI < 30:
    print('You are normal weight')
elif BMI >= 30:
    print('obese')
else:
    print('invalid')