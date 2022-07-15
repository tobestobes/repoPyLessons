name = input("Как тебя зовут?")

print(f'Привет, {name}!')

age = int(input(f"Скажи, {name} сколько тебе лет?"))

if age < 26:
    print(f'{age}? А мне 26! Я тебя старше на {26 - age} :)')
elif age == 26:
    print(f'{age}? И мне тоже! Получается мы с тобой ровесники :)')
else:
    print(f'{age}? А мне 26! Ты меня старше на {age - 26} :)')