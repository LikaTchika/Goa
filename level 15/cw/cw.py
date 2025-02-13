print("Even numbers from 1 to 50:")
for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=" ")


sum_result = 0
for num in range(11):
    sum_result += num
print("\nSum of numbers from 0 to 10:", sum_result)  

print("Numbers from 100 to 0 in reverse order:")
for num in range(100, -1, -1):
    print(num, end=" ")


print("\nOdd numbers from 1 to 50:")
for num in range(1, 51):
    if num % 2 != 0:
        print(num, end=" ")   