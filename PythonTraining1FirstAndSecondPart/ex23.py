'''
Исполнитель преобразует число на экране.
У исполнителя есть две команды, которым присвоены номера:
1. Прибавить 1
2. умножить на 2
Первая команда увеличивает число на экране на 1, вторая умножает его на 2.
Программа для исполнителя это последовательность команд.
Например, если в начальный момент на экране находится число 1, то программа 212 последовательно преобразует его в 2, 3, 6 .
Сколько существует программ, которые преобразуют исходное число 1 в число 40 так, что в процессе выполнения на экране ни разу не появляется цифра 3?
'''


def f(x, y):
    if x > y or str(x).count('3') >= 1:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y)


print(f(1, 40))