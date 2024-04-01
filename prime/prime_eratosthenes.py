def sieve_of_eratosthenes(limit):
    prime = [True for _ in range(limit + 1)]
    p = 2
    while p * p <= limit:
        if prime[p] is True:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return [p for p in range(limit + 1) if prime[p]]


# 範囲内の素数を取得し、特定の数が素数かどうかを判定するために使用する
def is_prime(n):
    primes = sieve_of_eratosthenes(int(n**0.5))
    for p in primes:
        if n % p == 0 and n > p:
            return False
    return True if n > 1 else False
