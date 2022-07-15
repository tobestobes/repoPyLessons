income = int(input("Введите значение выручки: "))

costs = int(input("Введите значение издержек: "))

if income > costs:
    print(f"Компания работает в прибыль с рентабельностью в {income / costs:.2f}%")
elif income == costs:
    print(f"Компания работает в ноль")
else:
    print(f"Компания работает в убыток с рентабельностью в {income / costs:.2f}%")