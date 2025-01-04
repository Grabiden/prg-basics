paragraph = "cat dog mouse cat rat cat mouse"
words = paragraph.split()
dict = {}
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(dict)
