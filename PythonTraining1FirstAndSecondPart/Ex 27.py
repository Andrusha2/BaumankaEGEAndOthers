'''
ISN'T CORRECT
'''
f = open('27-B.txt')
f = [int(i) for i in f]
f = f[1:]
counter = 0
for i in range(len(f)):
    for j in range(i + 1, len(f)):
        if (f[i] + f[j]) % 3 == 0 and f[i] * f[j] % 1024 == 0:
            counter += 1
print(counter)

