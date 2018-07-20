for i in range(0,10):
    valor = int(input())
    if valor <= 0:
        valor = 1
    print("X[{}] = {}".format(str(i), str(valor)))
