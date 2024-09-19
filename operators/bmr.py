age = int(input('Enter age: '))
weight = int(input('Enter weight: '))
height = int(input('Enter height: '))
gender = input('Enter gender: ').lower()

print(f'age={age}, weight = {weight}, height = {height}, gender = {gender}')

if gender == 'male':

    BMR = 10 * weight + 6.25 * height - 5 * age + 5 

elif gender == 'female':

    BMR = 10 * weight + 6.25 * height - 5 * age - 161

else:

    print("*****please enter valid gender*****")

print(BMR)

calorie = 0

activity_level = int(input("""
                       Select activity level
                       press 1 for sedentary
                       press 2 for lightly active
                       press 3 for moderatly active
                       press 4 for very active
                       press 5 for extra active
                        """))


if activity_level == 1:

    calorie = BMR * 1.2

elif activity_level == 2:

    calorie = BMR * 1.375

elif activity_level == 3:

    calorie = BMR * 1.55

elif activity_level == 4:

    calorie = BMR * 1.725

elif activity_level == 5:

    calorie = BMR * 1.9

else:
    print('Select valid choice for activity level')

print(f" total number of calories you need to maintain your currrent weight = {calorie}")

target_weight = int(input("Enter the weight to reduce in kg: "))

duration = int(input("Enter duration in weeks: "))

calorie_deficit = target_weight * 7700

days = duration * 7 

daily_calorie_deficit = calorie_deficit/days

print(f'your daily calorie deficit is {daily_calorie_deficit}')

