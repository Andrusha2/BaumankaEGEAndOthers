'''
Даны целые неотрицательные числа a,b,c,d, при этом 0≤c<d. Выведите в порядке возрастания все числа от a до b, которые
 дают остаток c при делении на d.
'''
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = [i for i in range(a, b + 1)]
print(*list(filter(lambda x: x % d == c, s))) КРУТОЙ СПОСОБ, НО РАЗРАБЫ САЙТА - ХУЕСОСЫ
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(c + (a - c + d - 1) // d * d, b + 1, d):
    print(i, end=' ')