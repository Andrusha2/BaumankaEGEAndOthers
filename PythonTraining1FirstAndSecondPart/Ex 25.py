for i in range(2023, 10 ** 10, 2023):
    n = str(i)
    if n[0] == '1' and n[2:5] == '493' and n[-2:] == '41':
        print(i)
