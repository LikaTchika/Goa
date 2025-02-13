
words =("python", "is", "fun")
final = " ".join(words)
print(final)



name= input("write your name:")
age= input("write your age:")
msg = "helo, {0} you are {1} years old".format(name,age)
print(msg)



msg = input() #პირობა
print (msg.replace("#", " ")) # სემოვიტანეT print ფუნქცია ავიღეთ msg და დავუწერეტ ახალი ნასწვლი ფუნქცია replace და ის რაც იყო ანუ # და შევცვალეთ ""



sentance = input("write any sentance you want:")
words = sentance.split()
print("list of words:", words)


sentance=input("write any sentance:")
O_word = input("write any word you wanna replace:")
N_word = input("write the new word:")
update =sentance.replace(O_word,N_word)