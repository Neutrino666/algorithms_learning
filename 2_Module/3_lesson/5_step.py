# реализация алгоритма Евклида

def gcd(a: int, b: int) -> int:
    while a % b != 0:
        a, b = b, a % b
    return b


def main():
    a, b = map(int, input().split())
    print(gcd(max(a, b), min(a, b)))


if __name__ == "__main__":
    main()