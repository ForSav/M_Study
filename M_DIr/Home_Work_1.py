def palindrome(word=input('Write a word ')):
    if list(word) == list(reversed(word)):
        return True
    else:
        return False


print(palindrome())
