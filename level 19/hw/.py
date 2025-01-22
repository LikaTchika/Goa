# 1. სიის შედგენა მომხმარებლის შეყვანისგან
numbers = []  # ცარიელი სია
print("შეიყვანეთ 10 რიცხვი:")

for i in range(10):  # 10-ჯერ შემოწმება
    num = int(input(f"რიცხვი {i+1}: "))
    numbers.append(num)

print("\nშექმნილი სია:", numbers)

# მაქსიმალური ელემენტის პოვნა სიაში
max_num = numbers[0]  # სიის პირველი ელემენტი
for num in numbers:
    if num > max_num:
        max_num = num

print("უდიდესი რიცხვი სიაში:", max_num)

# ელემენტის წაშლა სიიდან
delete_num = int(input("\nრომელი რიცხვის წაშლა გსურთ? "))
if delete_num in numbers:
    numbers.remove(delete_num)
    print("განახლებული სია:", numbers)
else:
    print("ეს რიცხვი სიაში არ არის.")

# 4. სიის საპირისპირო მიმდევრობით ჩაწერა
reversed_list = []
for i in range(len(numbers) - 1, -1, -1):  # ბოლო ელემენტიდან პირველამდე
    reversed_list.append(numbers[i])

print("სია საპირისპირო წესით:", reversed_list)

# 5. ელემენტის ძებნა სიაში
search_num = int(input("\nრომელი რიცხვის ძებნა გსურთ? "))
found = False
for num in numbers:
    if num == search_num:
        found = True
        break

if found:
    print("რიცხვი სიაში არსებობს.")
else:
    print("რიცხვი სიაში არ არის.")