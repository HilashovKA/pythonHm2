def set_products(n: int) -> list:
    set = [1]
    for i in range(2, n+1):
        set.append(set[-1] * i)
    return set
n = int(input('Введите натуральное число: '))
set = set_products(n)
print(set)