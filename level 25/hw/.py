# გამოვიტანოთ random ფუნქცია
import random
print("Think of a number from 0-100, and I will try to guess it, but don't tell me.")

# დავამატოთ კოდი რომ მივუთითოთ თუ რამდენი ცდა გვაქვს და გადავცეტ ფუნქცია
attempts = 0
correct_number = random.randint(1, 100)

# სანამ 3 ცდა მაქვს გამოვიყენოთ პირველი
while attempts < 3:
    guess = int(input("I think it's number: "))
    attempts += 1

    if guess > correct_number:
        print('Higher')
    elif guess < correct_number:
        print('Lower')
    else:
        print('It\'s correct, I did a good job!')
        break
else:
    print('Sorry, I couldn\'t guess your number, but your number was', correct_number)















