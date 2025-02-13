
sentence = input("Enter a sentence: ")
words_list = sentence.split()
print(words_list)

words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)

sentence = input("Enter a sentence: ")
word_to_replace = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
modified_sentence = sentence.replace(word_to_replace, new_word)
print(modified_sentence)

text = input("Enter a string: ")
lower_text = text.lower()
print(lower_text)sentence = input("Enter a sentence: ")
upper_sentence = sentence.upper()
print(upper_sentence)