def geometric_progression(a, b):
    while True:
        yield a
        a *= b
a = 2
b = 3

gp = geometric_progression(a, b)

for i in range(5):
    print(next(gp))