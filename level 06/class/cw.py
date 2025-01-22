name = input("შეიყვანეთ სახელი: ")
surname = input("შეიყვანეთ გვარი: ")
age = input("შეიყვანეთ ასაკი: ")
country = input("შეიყვანეთ ქვეყანა: ")
city = input("შეიყვანეთ ქალაქი: ")
favorite_car = input("შეიყვანეთ საყვარელი მანქანა: ")
favorite_color = input("შეიყვანეთ საყვარელი ფერი: ")

sentence = f"{name} {surname}, {age} წლის, ცხოვრობს {country}-ში, ქალაქ {city}-ში. მისი საყვარელი მანქანაა {favorite_car}, ხოლო საყვარელი ფერია {favorite_color}."
print(sentence)
num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

print(f"{num1} + {num2} = {num1 + num2}")  # შეკრება
print(f"{num1} - {num2} = {num1 - num2}")  # გამოკლება
print(f"{num1} * {num2} = {num1 * num2}")  # გამრავლება
print(f"{num1} // {num2} = {num1 // num2}")  # მთლიანი გაყოფა
print(f"{num1} % {num2} = {num1 % num2}")  # ნაშთის პოვნა