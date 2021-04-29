n, m = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

result = [0] * (m+1)
result[0] = 1

for i in coin:
    for j in range(1, m+1):
        if j-i >= 0 :
            result[j] += result[j-i]

print(result[m])

