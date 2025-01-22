# მომხმარებლისგან პროდუქტის ფასის შეყვანა
price = float(input("შეიყვანეთ პროდუქტის ფასი: "))

# ფასდაკლების განსაზღვრა და საბოლოო ფასის გამოთვლა
if price > 50:
    discount = price * 0.10
    final_price = price - discount
    print("პროდუქტზე გამოყენებულია 10%-იანი ფასდაკლება. საბოლოო ფასი: {final_price} ლარი")
elif 20 <= price <= 50:
    discount = price * 0.05
    final_price = price - discount
    print("პროდუქტზე გამოყენებულია 5%-იანი ფასდაკლება. საბოლოო ფასი: {final_price} ლარი")
else:
    print("ფასდაკლება არ გამოიყენება. საბოლოო ფასი: {price} ლარი")




    


        





number=int(input("enter number"))
if number 0:
    print("its zero")
if number <0:
    print("dadebiti ricxvia")
if number >0:
    print("uaryofiti ricxvia")


age= int(input("enter your age"))

if age > 1 and age < 13:
print('child')

if age > 13 and age < 19:
print('teen')

if age >19 and < 20:
    print('adult')




grade = int(input("enter your grade from 0 to 100"))

if grade 0 or grade 100:
elif grade > 90:
print print ("you got A")

elif <= 80 grade <= 89
print("you got B")

elif  70 <= grade <= 79
print("you have C")

elif 60 <= grade <= 69
print("you got D")

else 60 <= grade <= 69
print("you got F")


