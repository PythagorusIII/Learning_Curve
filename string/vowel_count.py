text ="HEllopython"
text = text.casefold()
count = 0
for i in text:
    if i == 'a' or i == 'e'or i == 'i'or i == 'o'or i == 'u':
        print(f'{i}')
        count += 1
print(count)
