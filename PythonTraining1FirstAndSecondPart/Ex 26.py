'''
ISN'T CORRECT
'''

f = open('26.txt')
s = [int(i) for i in f]
s = sorted(s[1:], reverse=True)
counter = 1
CurrentMx = 1
mx = 1
for i in range(len(s) - 1):
    if s[i] >= s[i + 1] + 5:
        CurrentMx += 1
    else:
        counter += 1
        if CurrentMx > mx:
            mx = CurrentMx
        CurrentMx = 0

if CurrentMx > mx:
    mx = CurrentMx
print(counter, mx)


f.close()