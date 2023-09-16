n = int(input('введите целое чилсо: '))
sum = 0
for i in range(0, n):
    i += 1
    sum += i ** 3
print(sum)

n = int(input('введите целое чилсо: '))
i = 1
sum = 0
while i <= n:
    sum += i ** 3
    i += 1
print(sum)