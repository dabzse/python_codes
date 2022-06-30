i_start = int(input("Enter a starting number: "))
i_finish = int(input("Enter a finish number: "))


def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if num % n != 0:
                continue
            else:
                return False
    return True


def show_primes(start, finish):
    primes = []
    for n in range(start, finish):
        if is_prime(n):
            primes.append(n)
    return primes


def work():
    primes = show_primes(start=i_start, finish=i_finish)
    print(primes)
    prime_len = len(primes)
    print(f"Primes found: {prime_len}")


if __name__ == '__main__':
    work()
