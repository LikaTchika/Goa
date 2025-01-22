count = 1
total = 0
even_count = 0

while count <= 100:
    if count % 2 == 0:
        total += count
        even_count += 1
    count += 1

average = total / even_count
print("The average of even numbers from 1 to 100 is:", average) number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.") year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.") score = int(input("Enter your score (1-100): "))

if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score < 90:
    print("Your grade is B")
elif 70 <= score < 80:
    print("Your grade is C")
else:
    print("Your grade is D")