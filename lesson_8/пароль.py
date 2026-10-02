def validate_password(password: str = 'Password2007') -> bool:

    if len(password) < 8:
        raise ValueError('Пароль короткий, нужен длиннее')
    if not any(i.isdigit() for i in password):
        raise ValueError('Нету цифры')
    if not any(i.isupper() for i in password):
        raise ValueError('Нету заглавной буквы')
    if password != 'Password2007':
        raise ValueError('Пароль не верный')
    return True

try:
    validate_password(input('Password: '))
    print('Пароль верный')
except ValueError as e:
    print(f'Ошибка: {e}')