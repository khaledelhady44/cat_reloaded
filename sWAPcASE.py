def swap_case(s):
    arr = [letter.lower() if letter.isupper() else letter.upper()
           for letter in s]
    return "".join(arr)


s = input()
print(swap_case(s))
