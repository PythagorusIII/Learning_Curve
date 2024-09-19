text = input("Enter a word: ")

reversed_text = text[::-1]

if text == reversed_text:
    print('palindrome')

else:
    print('not palindrome')



count = len(text)

reversed_string = ""

for i in range(count-1,-1,-1):
    
    reversed_string += text[i]

print(reversed_string)





