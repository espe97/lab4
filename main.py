# Алгоритм Евклида
def gcd_euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Бинарный алгоритм Евклида
def gcd_binary(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1

    while (a & 1) == 0:
        a >>= 1

    while b != 0:
        while (b & 1) == 0:
            b >>= 1

        if a > b:
            a, b = b, a
        
        b -= a

    return a << shift

# Расширенный алгоритм Евклида
def extended_gcd_euclid(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd_euclid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Расширенный бинарный алгоритм Евклида
def extended_binary_gcd(a, b):
    if a == 0:
        return b, 0, 1

    if b == 0:
        return a, 1, 0

    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1

    u, v = a, b
    x1, x2, y1, y2 = 1, 0, 0, 1

    while u != 0:
        while (u & 1) == 0:
            u >>= 1
            if (x1 | y1) & 1:
                x1 += b
                y1 -= a
            x1 >>= 1
            y1 >>= 1

        while (v & 1) == 0:
            v >>= 1
            if (x2 | y2) & 1:
                x2 += b
                y2 -= a
            x2 >>= 1
            y2 >>= 1

        if u >= v:
            u -= v
            x1 -= x2
            y1 -= y2
        else:
            v -= u
            x2 -= x1
            y2 -= y1

    return v << shift, x2, y2

# Основная программа с пользовательским вводом
def main():
    print("Введите два числа для нахождения их НОД:")
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))

    print("\nРезультаты:")
    
    # 1. Алгоритм Евклида
    print("НОД (алгоритм Евклида):", gcd_euclid(a, b))

    # 2. Бинарный алгоритм Евклида
    print("НОД (бинарный алгоритм Евклида):", gcd_binary(a, b))

    # 3. Расширенный алгоритм Евклида
    gcd, x, y = extended_gcd_euclid(a, b)
    print(f"НОД (расширенный алгоритм Евклида): {gcd}, x = {x}, y = {y}")

    # 4. Расширенный бинарный алгоритм Евклида
    gcd, x, y = extended_binary_gcd(a, b)
    print(f"НОД (расширенный бинарный алгоритм Евклида): {gcd}, x = {x}, y = {y}")

# Запуск программы
if __name__ == "__main__":
    main()
