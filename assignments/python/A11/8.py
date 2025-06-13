# snakes and ladder

num = 100
for i in range(10):
    if i % 2 == 0:
        for j in range(10):
            print(num, end=" ")
            num -= 1
    else:
        start = num - 9
        for j in range(start, num + 1):
            print(j, end=" ")
        num -= 10
    print()
