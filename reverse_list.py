numbers = [6, 2, 4, 6, 7, 3, 9]

start = 0
end = len(numbers) - 1

while start < end:
    numbers[start], numbers[end] = numbers[end], numbers[start]
    start += 1
    end -= 1

print("Reversed:", numbers)
