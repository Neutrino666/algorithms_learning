def fib(n: int) -> int:
    arr = [0, 1]

    if n <= 1: 
        return n
    for _ in range(1, n):
        arr.append(sum(arr))
        arr = arr[-2:]
    return arr[-1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()