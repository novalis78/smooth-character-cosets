"""Verify the two fixed-prime calculations in growth-rate-seeded-cycles.tex."""

from math import isqrt


def cycle(p, state):
    root = isqrt(p)
    start = state
    states = []
    while True:
        r, norm = state
        assert root - norm < r <= root and norm <= root + r
        assert (p - r * r) % norm == 0
        states.append(state)
        r = ((r + root) // norm) * norm - r
        state = r, (p - r * r) // norm
        if state == start:
            return states


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def verify(p, cutoff, target):
    assert is_prime(p) and p % 24 == 23
    primes = [q for q in range(2, cutoff + 1) if is_prime(q)]
    negative = [q for q in primes if pow(q, (p - 1) // 2, p) == p - 1]
    assert negative == [target]
    seeds = {s for s in primes if s % 4 == 1}
    root = isqrt(p)
    unseen = {
        (r, norm)
        for r in range(1, root + 1)
        for norm in range(root - r + 1, root + r + 1)
        if (p - r * r) % norm == 0
    }
    classes = starts = incidences = weighted = 0
    while unseen:
        orbit = cycle(p, next(iter(unseen)))
        assert set(orbit) <= unseen
        unseen.difference_update(orbit)
        weight = sum(norm in seeds for _, norm in orbit)
        hits = sum(norm % target == 0 for _, norm in orbit)
        classes += 1
        starts += weight
        incidences += hits
        weighted += weight * hits
    assert starts == 2 * len(seeds)
    print(f"p={p}: {classes} classes, {starts} starts, "
          f"{incidences} incidences over all classes, seeded mean {weighted}/{starts}")
    return classes, starts, incidences, weighted


if __name__ == "__main__":
    assert verify(5711, 19, 19) == (5, 6, 8, 10)
    assert verify(28559, 11, 11) == (15, 2, 18, 0)
    assert [n for _, n in cycle(5711, (71, 5))][:6] == [5, 47, 26, 67, 10, 95]
    for r in (167, 168):
        print(f"p=28559, start ({r},5):", [n for _, n in cycle(28559, (r, 5))])
