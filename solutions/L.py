count_testes = 0
while True:
    N = int(input())

    if (N == 0): break

    if count_testes > 0: print() # linha em branco apos output anterior

    count_testes += 1

    j = [input(), input()]

    print("Teste {}".format(count_testes))

    for i in range(0, N):
        resultado = sum([int(x) for x in input().split(' ')]) % 2
        print(j[resultado])
