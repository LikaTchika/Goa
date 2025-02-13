# 1. ცვლადები და მონაცემთა ტიპები
name = "Ana"
age = 15
height = 1.65
is_student = True

print(f"Hello, my name is {name}. I am {age} years old and {height}m tall.")

# 2. ოპერატორები
a = 10
b = 3

sum_ = a + b
diff = a - b
product = a * b
quotient = a / b
modulus = a % b
power = a ** b

print(f"Sum: {sum_}, Difference: {diff}, Product: {product}, Quotient: {quotient}, Modulus: {modulus}, Power: {power}")

# 3. ციკლები (for, while)
# for ციკლი - სიის ყველა ელემენტის დაბეჭდვა
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"For loop: {num}")

# while ციკლი - 1-დან 5-მდე რიცხვების დაბეჭდვა
counter = 1
while counter <= 5:
    print(f"While loop: {counter}")
    counter += 1

# 4. ფუნქციები
def greet_user(username, user_age):
    print(f"Hello {username}, you are {user_age} years old!")

greet_user(name, age)

# ფუნქცია, რომელიც აბრუნებს ორი რიცხვის ჯამს
def add_numbers(x, y):
    return x + y

result = add_numbers(7, 5)
print(f"Sum from function: {result}")

# ფუნქცია, რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი
def is_even(number):
    return number % 2 == 0

print(f"Is 10 even? {is_even(10)}")
print(f"Is 7 even? {is_even(7)}")
