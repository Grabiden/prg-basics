sentence = 'I completely agree with you'
sentence2 = sentence.split()
result = list(map(lambda x: (len(x), sentence2)))
print(result)