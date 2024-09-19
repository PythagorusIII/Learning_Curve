# Program to print even numbers between two limits

# take two limits from the user

begin = int(input('enter starting limit: '))

end = int(input('enter limit: '))

reverse = True if begin>end else False  

i = begin

while(i <= end if reverse == False else i >= end):

    if i % 2 == 0:
        print(i)

    if reverse == False:
        i += 1

    else:
        i -= 1

    