def divide_func(a, b):
    try:
        x = a / b
    except ZeroDivisionError as err:
        print(err)
    else:
        return x

print(divide_func(int(input("Введите делимое: ")), int(input("Введите делитель: "))))
