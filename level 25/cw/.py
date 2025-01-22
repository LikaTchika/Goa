text = input("add text: ")

print("text in big letters:", text.lower())
print("text in small letters:", text.upper())
print("text with first big letter:", text.capitalize())

word_to_find = input("add word: ")
index = text.find(word_to_find)
