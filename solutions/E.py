def maior(a, b):
    return (a + b + abs(a-b)) // 2

numeros = [int(x) for x in input().split(' ')]
maior = maior(numeros[0], maior(numeros[1], numeros[2])) 

print(str(maior) + " eh o maior")
