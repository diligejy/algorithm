n = int(input())

words = [input() for _ in range(n)]


def isPalindrome(x):
    x = x.lower()
    if x == x[::-1]:
        return "YES"
    else:
        return "NO"


for idx, word in enumerate(words):
    print(f"#{idx + 1} " + isPalindrome(word)) 
