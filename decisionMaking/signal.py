colour = input('Enter the signal colour: ').lower()


if colour == 'red':
    print('Stop!')

elif colour == 'yellow' or colour =='orange':
    print('Slow down')

elif colour == 'green':
    print('Go')

else:
    print('Enter green, red, yellow or orange')