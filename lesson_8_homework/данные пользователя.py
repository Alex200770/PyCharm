def register_user(username: str, age: int):
    errors = []
    if not isinstance(age, int):
        errors.append('Некоректный возраст')
    if not isinstance(username, str):
        errors.append('Некоректное имя пользователя')
    if not username.isalpha():
        errors.append('Имя не должно содеражать цифры')
    if username == '':
        errors.append('Вы забыли ввести имя пользователя')
    if len(username) < 3:
        errors.append('Имя пользователя должно иметь не менее 3-х символов')
    if age < 14:
        errors.append('Извините, регистрация доступна от 14 лет')
    if errors:
        raise ValueError('\n'.join(errors))
    print(f'Регистрация пользователя {username} успешно завершена')

try:
    name = str(input('Введите имя пользователя: '))
    user_age = int(input('Введите возраст пользователя: '))
    register_user(name, user_age)
except ValueError as e:
    print(f'Ошибка: {e}')
