numbers = input("Enter numbers: ").split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for i in range(len(numbers)):
    if numbers[i] > 100:
        numbers[i] = "over"

print(numbers)
