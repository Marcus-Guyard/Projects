import sys

n, m = map(int, sys.stdin.readline().split())

lines = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

stations = [0] * n
count = 0
for _ in range(len(lines)):
    print(stations)
    if stations[0] == 0:
        stations[0] = sum(lines[_])
        continue
    for s in stations:
        if lines[_][0] - s <= m and s != 0:
            stations[stations.index(s)] += (lines[_][0] - s) + lines[_][1]
            count += 1
            break
        if s == 0:
            stations[stations.index(s)] += sum(lines[_])
            break
print(count)





