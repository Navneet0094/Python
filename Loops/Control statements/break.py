numbers = [1, 3, 5, 6, 7, 8, 9]
for num in numbers:
    print(num)
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break