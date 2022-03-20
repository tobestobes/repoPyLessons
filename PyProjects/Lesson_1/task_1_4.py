num = int(input("Введите многозначное число: "))

greatest_num = 0 # Наибольшая цифра

while num:
    cut = num % 10 # Отрезанная цифра
    if cut > greatest_num:
        greatest_num = cut
        if greatest_num == 9:
            break
    num = num // 10

print(f"Наибольшая цифра в числе - {greatest_num}")