# 1. Create a list named fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 2. Print the entire list
print(f"Entire list: {fruits}")

# 3. Access and print the first and last items in the list
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")

# 4. Add a new fruit "fig" to the list
fruits.append("fig")

# 5. Remove "banana" from the list
fruits.remove("banana")

# 6. Change the value of the second item to "blueberry"
fruits[1] = "blueberry"

# 7. Print the length of the list
print(f"Length of the list: {len(fruits)}")# 1. Create a list named numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

numbers.append(100)

numbers.insert(0, 5)

numbers.remove(30)

numbers.sort()


numbers.reverse()

index_50 = numbers.index(50)

count_20 = numbers.count(20)

print(f"Updated list: {numbers}")
print(f"Index of 50: {index_50}")
print(f"Count of 20: {count_20}")
numbers = list(range(1, 11))

first_half = numbers[:5]

second_half = numbers[5:]

squares = [x**2 for x in numbers]


print(f"First half: {first_half}")
print(f"Second half: {second_half}")
print(f"Squares: {squares}")