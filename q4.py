text = input("enter the word:")
words = text.split()
i_count={}
for x in words:
    if x in i_count:
        i_count[x] += 1
    else:
        i_count[x] = 1

print(i_count)