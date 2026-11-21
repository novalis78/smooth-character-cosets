"""Reproduce the fixed-prime examples and the interval table in the accompanying note."""

from collections import Counter
from decimal import Decimal, localcontext
from functools import lru_cache
from math import isqrt


def primes_up_to(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for q in range(2, isqrt(limit) + 1):
        if sieve[q]:
            sieve[q * q :: q] = bytes((limit - q * q) // q + 1)
    return [q for q in range(2, limit + 1) if sieve[q]]


def legendre(a, p):
    value = pow(a % p, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def period(d):
    root = isqrt(d)
    assert root * root < d
    offset, denominator, quotient = 0, 1, root
    while True:
        offset = quotient * denominator - offset
        numerator = d - offset * offset
        assert numerator % denominator == 0
        denominator = numerator // denominator
        yield denominator
        if denominator == 1:
            return
        quotient = (root + offset) // denominator


@lru_cache(maxsize=None)
def prime_factors(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if n > 1:
        factors.append(n)
    return tuple(factors)


def analyze_period(p, m, cutoff):
    hits = set()
    rows = []
    for k, norm in enumerate(period(m * p), 1):
        parity = k % 2
        assert legendre(norm, p) == (-1) ** parity
        row = parity  # bit zero is the sign; bit q records v_q modulo two
        for q in prime_factors(norm):
            if q > cutoff:
                row ^= 1 << q
            elif q != 2 and legendre(-m, q) == -1:
                hits.add(q)
        rows.append(row)
    return hits, rows


def has_odd_relation(rows):
    pivots = {}
    for row in rows:
        while row > 1:
            pivot = row.bit_length()
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
        if row == 1:
            return True
    return False


def check_examples():
    p = 1_478_231
    norm1 = list(period(p))[14]
    norm2 = list(period(2 * p))[49]
    assert (norm1, norm2) == (5 * 47, 29 * 47)
    assert legendre(5, p) == 1 and legendre(29, p) == -1
    p, q = 5711, 19
    assert next(r for r in primes_up_to(q) if legendre(r, p) == -1) == q
    eligible = [m for m in range(1, 5) if legendre(-m, q) == -1]
    assert eligible == [1, 4]
    assert all(norm % q for m in eligible for norm in period(m * p))


def main():
    check_examples()
    primes = primes_up_to(2_000_000)
    small = primes_up_to(50)
    counts = Counter()
    joint_only = []
    for p in primes:
        if p < 100_000 or p % 24 != 23:
            continue
        if any(legendre(q, p) == -1 for q in small if q < 23):
            continue
        counts["cohort"] += 1
        with localcontext() as context:
            context.prec = 50
            cutoff = int(Decimal(p).ln() ** 2 / 5)
        assert cutoff < small[-1]
        direct = {q for q in small if q <= cutoff and legendre(q, p) == -1}
        hits1, rows1 = analyze_period(p, 1, cutoff)
        hits2, rows2 = analyze_period(p, 2, cutoff)
        assert (hits1 | hits2) <= direct
        rank1 = has_odd_relation(rows1)
        rank2 = has_odd_relation(rows2)
        joint = has_odd_relation(rows1 + rows2)
        assert not joint or hits1 or hits2
        counts["direct"] += bool(direct)
        counts["factor m=1"] += bool(hits1)
        counts["factor m=1 or 2"] += bool(hits1 or hits2)
        counts["rank m=1"] += rank1
        counts["rank m=2"] += rank2
        counts["rank separately, either succeeds"] += rank1 or rank2
        counts["rank jointly"] += joint
        if joint and not (rank1 or rank2):
            joint_only.append(p)
    for test, count in counts.items():
        print(f"{test}: {count}")
    print("Joint rank alone succeeds at", joint_only)


if __name__ == "__main__":
    main()
