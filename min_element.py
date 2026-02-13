numbers = [6, 2, 4, 6, 7, 3, 9]

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum:", minimum)
