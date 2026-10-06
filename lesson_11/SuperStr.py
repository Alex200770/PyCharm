def is_repeatance(s: str):

    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            piece = s[:i]
            repeat_count = n // i
            if piece * repeat_count == s:
                return True
    return False

print(is_repeatance('aaaa'))
print(is_repeatance('abcab'))
print(is_repeatance('ababab'))
print('------------')

def is_palindrome(s: str):
    return s.lower() == s[::-1].lower()
print(is_palindrome('abba'))
print(is_palindrome('Anna'))
print(is_palindrome('ab'))