for i in range(101):
    if int((bin(i)[2::])[::-1], 2) == 13:
        print(i)