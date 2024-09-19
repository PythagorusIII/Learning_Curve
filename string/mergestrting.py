# text1 ="PQRS"
# text2 ="ABCD"
# last= ""

# for i in range(0,3):

#     last = last + text1[i] + text2[i]

# print(last)


text1 ="ABC"
text2 ="PQRST"

smallest = text1 if text1 < text2 else text2
largest = text1 if text1 > text2 else text2

result =""

for i in range(0,  len(smallest)):

    result = result + largest[i] + smallest[i]

result += largest[len(smallest):]
print(result)