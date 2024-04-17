n = int( input("emter n : "))
for i in range(1, n + 1):  # Loop for rows
    for j in range(1, i + 1):  # Loop for columns
        print(chr(64 + j), end="")
    print()