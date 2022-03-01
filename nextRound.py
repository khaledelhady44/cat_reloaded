n, k = tuple(map(int, input().split()))
scores = list(map(int, input().split()))

k_score = scores[k - 1]

counter = 0
for score in scores:
    counter += 1 if score >= k_score and score > 0 else 0

print(counter)
