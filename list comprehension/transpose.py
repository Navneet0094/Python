l = [[1, 2, 3], [4, 5, 6]]

# Transpose the matrix using nested list comprehension
transpose = [[row[i] for row in l] for i in range(len(l[0]))]

print(transpose)
# l1 = [x[y] for x in temp for temp in ]