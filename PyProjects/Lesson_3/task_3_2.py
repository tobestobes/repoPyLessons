def my_func(**kwargs):
    return ' '.join(kwargs.values())

print(my_func(a=input("Введите имя: "), b=input("Введите фамилию: "), c=input("Введите год рождения: "), d=("Введите город проживания: "), e=("Введите email: "), f=input("Введите телефон: ")))