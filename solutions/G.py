dia_inicio = int(input().split(' ')[1])
hora_inicio = [int(x) for x in input().split(" : ")]
dia_fim = int(input().split(' ')[1])
hora_fim = [int(x) for x in input().split(" : ")]

total_seconds = (dia_fim - dia_inicio + 1) * 24 * 3600 - (hora_inicio[0] * 3600 + hora_inicio[1] * 60 + hora_inicio[2]) \
- (24 * 3600 - (hora_fim[0] * 3600 + hora_fim[1] * 60 + hora_fim[2]))

days = total_seconds // (24 * 3600)
total_seconds = total_seconds % (24 * 3600)

hours = total_seconds // 3600
total_seconds = total_seconds % 3600

minutes = total_seconds // 60
total_seconds = total_seconds % 60

seconds = total_seconds

print(str(days) + " dia(s)")
print(str(hours) + " hora(s)")
print(str(minutes) + " minuto(s)")
print(str(seconds) + " segundo(s)")
