n = int(input())
operations = [input() for i in range(n)]
x = 0

for operation in operations:
    x += 1 if operation.find("+") != -1 else -1

print(x)
