my_list = list(map(int, input("Enter list numbers separated by spaces: ").split()))

if len(my_list) % 2 != 0:
    n = my_list[-1]
    my_list.pop()
    for i in my_list[::2]:
        x = my_list[i-1]
        my_list[i-1] = my_list[i]
        my_list[i] = x
    my_list.append(n)
else:
    for i in my_list[::2]:
        x = my_list[i-1]
        my_list[i-1] = my_list[i]
        my_list[i] = x

print(my_list)

# ---------------------------------------- правильный вариант

my_list = list(input("Enter list numbers without spaces: "))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)