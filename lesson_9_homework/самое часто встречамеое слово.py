#import this

def do_the_most_common_words(principal_file: str, secondary_file: str):

    result = []

    with open(principal_file, 'r', encoding='utf-8') as file1:

        text = file1.read()
        a = text.lower().split()
        most_common = max(set(a), key=a.count)  # считаем самое встречаемое слово в тексте
        total = a.count(most_common)
        with open(secondary_file, 'w', encoding='utf-8') as file2:
            for i in text.splitlines():
                cnt = i.lower().split().count(most_common)
                result.append(f'Слово {most_common} Встретилось {cnt} раз')
            file2.write(most_common + '\n')
            result.append(f'Всего слов {most_common} встретилось {total} раз')
            file2.write(f'Всего таких слов в тексте: {total}')
    return result

with open('principal.txt', 'w', encoding='utf-8') as t:
    t.write('sweater Weather\nsnowy weather\nsonny weather\ncloady Weather weather weather\n')

result = do_the_most_common_words('principal.txt', 'secondary.txt')
print(*result, sep='\n')