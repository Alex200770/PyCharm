some_str: str = 'Hello, World!'
encoded_str: bytes = some_str.encode('utf-8')
print(encoded_str)
print(encoded_str.decode('utf-8'))

print(chr(1))
print(ord('a'))