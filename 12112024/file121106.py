for i in range(10):
    for j in range(1000):
        a = int('1' + str(i) + '2157' + str(j) + '4')
        if a%2024 == 0:
            print(a, a/2024)