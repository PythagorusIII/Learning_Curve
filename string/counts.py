text = 'pneumonoultramicroscopicsilicovolcanoconiosis'
count_vowel = 0
count_consonants = 0
vowel_sequence = ('a','e','i','o','u')
for i in (text):
    if i in vowel_sequence:
        print(f'{i} vowel')
        count_vowel += 1

    else:
        print(f'{i} consonants')
        count_consonants += 1

print(count_vowel)
print(count_consonants)