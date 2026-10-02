def copy_nonempty_lines(source_path: str, target_path: str) -> int:
    count = 0
    with open(source_path, "r", encoding="utf-8") as file1:
        with open(target_path, "w", encoding="utf-8") as file2:
            for line in file1:
                line = line.strip()
                if line:
                    file2.write(line + "\n")
                    count += 1
    return count

with open('source.txt', 'w', encoding='utf-8') as text:
    text.write('Первая строка\n\n      Втора строка\n')
print(copy_nonempty_lines('source.txt', 'target'))