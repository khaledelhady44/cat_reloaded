matrix = [list(map(int, input().split())) for i in range(5)]

xLocation = [sum(row) for row in matrix].index(1)
yLocation = matrix[xLocation].index(1)

print(abs(2 - xLocation) + abs(2 - yLocation))
