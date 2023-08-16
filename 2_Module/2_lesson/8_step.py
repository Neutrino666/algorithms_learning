# Программа находит остаток деления на m, n-го числа фибоначи

def fib_mod(n: int, m: int) -> int:
    cur = 1
    prev = 0
    arr_mod = [0, 1]

    if n == 1: 
        return n
    for _ in range(1, n):
        cur, prev = (prev + cur) % m, cur
        # Создается массив Периода Пизано
        arr_mod.append(cur)
        if arr_mod[-2:] == [0, 1]:
            arr_mod = arr_mod[:-2]
            return arr_mod[n % len(arr_mod)]
    return cur


def main():
    # n - порядковый номер последовательности Фибоначчи
    # m - делитель для чисел Фибоначчи
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()