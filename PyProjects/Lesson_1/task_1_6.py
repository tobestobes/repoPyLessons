a = int(input("Введите начальный параметр в километрах: "))

b = int(input("Введите желаемый результат: "))

day = 1

while a < b:
    if a <= 0 or b <= 0:
        break
    print(f"{day}-й день: {a:.2f} км")
    a = a * 1.1
    day = day + 1

print(f"{day}-й день: {a:.2f} км")

print(f"За {day} дня спортсмен достигнет результата")