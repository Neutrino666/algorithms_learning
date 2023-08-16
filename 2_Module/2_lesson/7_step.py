def fib_digit(n: int) -> int:
    cur = 1
    prev = 0

    if n == 1: 
        return n
    for _ in range(1, n):
        cur, prev = (prev + cur) % 10, cur
    return cur


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()