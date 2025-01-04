translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
word = input("what word would you like to translate? ")
if word in translations:
    print(translations[word])
else:
    print("word not found")