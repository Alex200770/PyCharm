my_string_list: list[str] = ['Hello from 2027', 'How are you?']

with open('some_text.txt', 'w') as file:
    file.writelines(line + '\n' for line in my_string_list)

with open('some_text.txt', 'a') as file:
    file.write('Alex\n')

with open('some_text.txt', 'r') as text:
    file_text = text.read()

print(file_text)

with open('some_text.txt3', 'w') as text:
    text.writelines(line + '\n' for line in my_string_list)
    text.seek(7)
    text.write('OOO')