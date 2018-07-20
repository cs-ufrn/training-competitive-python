N = int(input())
res = ["PUM\n" if x % 4 == 0 else str(x) + " " for x in range(1, 4*N + 1)]
print("".join(res), end='')
