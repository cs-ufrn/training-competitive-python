inp = [float(x) for x in input().split(' ')]

preco_a = inp[0]/inp[2]
preco_g = inp[1]/inp[3]

out = 'G' if preco_a >= preco_g else 'A'

print(out)
