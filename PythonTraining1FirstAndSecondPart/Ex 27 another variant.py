'''
ISN'T CORRECT
'''
def g(a):
    spis = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    for i in spis:
        if a % i == 0:
            return i


d = {1024: 10, 512: 9, 256: 8, 128: 7, 64: 6, 32: 5, 16: 4, 8: 3, 4: 2, 2: 1, 1: 0}
f = open('27-A.txt')
s = [int(i) for i in f]
s = s[1:]
r0 = [0] * 11
r1 = [0] * 11
r2 = [0] * 11
main = [r0, r1, r2]
for j in s:
    if j % 3 == 0:
        main[0][d.get(g(j))] += 1
    elif j % 3 == 1:
        main[1][d.get(g(j))] += 1
    else:
        main[2][d.get(g(j))] += 1
print(main)
f.close()
