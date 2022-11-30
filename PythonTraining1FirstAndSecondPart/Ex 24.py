'''
Текстовый файл содержит только буквы A, C, D, F, O. Определите
максимальное количество идущих подряд групп символов вида
согласная + согласная + гласная.
'''


f = open('24.txt')
s = f.readline().replace('C', 'S').replace('D', 'S').replace('F', 'S')
s = s.replace('A', 'E').replace('O', 'E')
s = s.replace('SSE', '*')
m = mx = 0
for i in s:
    if i == '*':
        m += 1
        if m > mx:
            mx = m
    else:
        m = 0
print(mx)
f.close()
