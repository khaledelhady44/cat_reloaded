n = int(input())
words = [input() for i in range(n)]


def abbreviate(word):
    return word if len(word) <= 10 else word[0] + str(len(word)-2) + word[-1]


for word in words:
    print(abbreviate(word))
