age = int(input())

years = age // 365
months = (age % 365) // 30
days = age - years*365 - months*30

print(str(years) + " ano(s)")
print(str(months) + " mes(es)")
print(str(days) + " dia(s)")
