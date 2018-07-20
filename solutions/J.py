dia_bola = int(input())
caixa = [int(x) for x in input().split(' ')] # A L P

test = all([dia_bola <= x for x in caixa])
print('S' if test else 'N')


