#BMI = weight in kg /(height in meter)**2

weight = int(input('Enter the weight in: '))
height_cm = int(input('Enter the height: '))

height_m = height_cm/100

print(f'Height is {height_m} m')
print(f'Weight is {weight} kg')

BMI = weight / height_m**2
BMI = round(BMI,1)

print(f'BMI is {BMI} \n A healthy body mass index (BMI) for most adults is between 18.5 and 24.9 ')

if BMI < 18.5:
    print('Underwight')
else:
    print('not healthy')
