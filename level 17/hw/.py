# პროგრამა
numbers = []

first_number = int(input("შეიყვანეთ პირველი რიცხვი: "))
numbers.append(first_number)

print("შეიყვანეთ სხვა რიცხვები (დაასრულეთ შეყვანა ცარიელი ხაზით):")
while True:
    try:
        num = input()
        if num == "":
            break
        numbers.append(int(num))
    except ValueError:
        print("შეიყვანეთ მხოლოდ რიცხვები ან დაასრულეთ შეყვანა ცარიელი ხაზით.")

print(f"სულ შეყვანილი რიცხვების რაოდენობაა: {len(numbers)}")# პროგრამა
input_numbers = input("შეიყვანეთ რიცხვები მძიმით გამოყოფილი ფორმატით (მაგ.: 1, 2, 3, 4): ")
numbers = list(map(int, input_numbers.split(',')))
total_sum = sum(numbers)
print(f"რიცხვების ჯამი: {total_sum}")