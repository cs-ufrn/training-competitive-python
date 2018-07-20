inp = [int(x) for x in input().split(' ')]

mins = (24 * 60) - (inp[0]*60 + inp[1]) - (24*60 - (inp[2]*60 + inp[3]))

if mins <= 0:
    mins += 24 * 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(mins // 60, mins % 60))
