#Найти факториал числа используя рекурсивную функцию
def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n-1)

num = 5
print(f"Факториал {num} это {factorial_recursive(num)}")