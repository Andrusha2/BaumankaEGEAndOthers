f = open('17.txt', 'r')
data = [int(i) for i in f]
sqmin = min([i ** 2 for i in data if abs(i) % 10 == 7])
answer = []
for i in range(len(data) - 1):
    if ((abs(data[i]) % 10 == 7) != (abs(data[i + 1]) % 10 == 7)) and ((data[i] ** 2 + data[i + 1] ** 2) < sqmin):
        answer.append(data[i] ** 2 + data[i + 1] ** 2)
print(len(answer))


f.close()