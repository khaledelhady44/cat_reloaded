n = int(input())
arr = sorted([int(x) for x in input().split()])
max = arr[-1]
maxIndex = arr.index(max)

answer = arr[0: maxIndex][-1]
print(answer)
