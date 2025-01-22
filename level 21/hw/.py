# Step 1
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Step 2
print("Entire list:", fruits)

# Step 3
print("First item:", fruits[0])
print("Last item:", fruits[-1])

# Step 4
fruits.append("fig")

# Step 5
fruits.remove("banana")

# Step 6
fruits[1] = "blueberry"

# Step 7
print("Length of the list:", len(fruits))# Step 1
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Step 2
numbers.append(100)

# Step 3
numbers.insert(0, 5)

# Step 4
numbers.remove(30)

# Step 5
numbers.reverse()

# Step 6
index_50 = numbers.index(50)
print("Index of 50:", index_50)

# Step 7
count_20 = numbers.count(20)
print("Count of 20:", count_20)# Step 1
numbers = list(range(1, 11))

# Step 2
first_half = numbers[:5]

# Step 3
second_half = numbers[5:]

# Step 4
squares = [x**2 for x in numbers]

# Step 5
print("First half:", first_half)
print("Second half:", second_half)
print("Squares:", squares)