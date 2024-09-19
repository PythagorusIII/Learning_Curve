text = "ABCD"

count = len(text)

result = ""

for i in range(0, count+count, count):

    result += text

print(result)