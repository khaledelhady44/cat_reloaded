n = int(input())
views = [list(map(int, input().split())) for i in range(n)]

answer = 0
for view in views:
    answer += 1 if sum(view) >= 2 else 0

print(answer)
