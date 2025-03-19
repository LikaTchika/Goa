# 1. სიის შედგენა მომხმარებლის შეყვანისგან
numbers = []  
print("write 10 words:")

for i in range(10):  # 10-ჯერ შემოწმება
    num = int(input(f"number {i+1}: "))
    numbers.append(num)

print("list:", numbers)

# მაქსიმალური ელემენტის პოვნა სიაში
max_num = numbers[0]  
for num in numbers:
    if num > max_num:
        max_num = num

print("biggest bumber:", max_num)

# ელემენტის წაშლა სიიდან
delete_num = int(input("witch number you wanna delite "))
if delete_num in numbers:
    numbers.remove(delete_num)
    print("new list:", numbers)
else:
    print("number is not on the list")

# 4. სიის საპირისპირო მიმდევრობით ჩაწერა
reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("reverse list", reversed_list)

# 5. ელემენტის ძებნა სიაში
search_num = int(input("witch word you wanna find? "))
found = False
for num in numbers:
    if num == search_num:
        found = True
        break

if found:
    print("word is in list.")
else:
    print("word is not on list")