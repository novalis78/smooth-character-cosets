"""Enclose the numerical constants in Proposition 1 using exact rationals.

Run with Python 3. The lower and upper endpoints printed are rounded outwards.
The analytic inputs, including Chirre's estimate and the saddle point asymptotic,
are separate from these elementary constants.
"""

from fractions import Fraction


def log_interval(value, terms=100):
    """Enclose log(value) using the series for twice atanh((value-1)/(value+1))."""
    if value <= 0:
        raise ValueError("logarithm requires a positive argument")
    if value < 1:
        lower, upper = log_interval(1 / value, terms)
        return -upper, -lower
    z = (value - 1) / (value + 1)
    power = z
    partial = Fraction(0)
    for k in range(terms):
        partial += 2 * power / (2 * k + 1)
        power *= z * z
    # Every omitted denominator is at least 2*terms+1.
    tail = 2 * power / ((2 * terms + 1) * (1 - z*z))
    return partial, partial + tail


def cutoff_interval(terms=40):
    """Enclose 2/exp(2) independently of log_interval."""
    term = total = Fraction(1)
    for k in range(1, terms + 1):
        term *= Fraction(2, k)
        total += term
    first_omitted = term * Fraction(2, terms + 1)
    # All ratios after the first omitted term are at most 2/(terms+2).
    tail = first_omitted / (1 - Fraction(2, terms + 2))
    return 2 / (total + tail), 2 / total


def decimal_endpoint(integer, places):
    sign = "-" if integer < 0 else ""
    whole, fractional = divmod(abs(integer), 10**places)
    return f"{sign}{whole}.{fractional:0{places}d}"


def enclosure(lower, upper, places=15):
    scale = 10**places
    floor = (lower.numerator * scale) // lower.denominator
    ceil = -((-upper.numerator * scale) // upper.denominator)
    return f"[{decimal_endpoint(floor, places)}, {decimal_endpoint(ceil, places)}]"


def check_sign(value, expected_positive):
    cutoff_lo, cutoff_hi = cutoff_interval()
    log_lo, log_hi = log_interval(value / 2)
    lo, hi = 1 + log_lo / 2, 1 + log_hi / 2
    if expected_positive:
        assert value > cutoff_hi and lo > 0
    else:
        assert value < cutoff_lo and hi < 0
    print(f"margin at eta={value}: {enclosure(lo, hi)}")


def main():
    log_lo, log_hi = log_interval(Fraction(2))
    print(f"maximum envelope coefficient g(1): {enclosure(3*log_lo/2, 3*log_hi/2)}")
    cutoff_lo, cutoff_hi = cutoff_interval()
    print(f"ordinary-sum cutoff 2/exp(2): {enclosure(cutoff_lo, cutoff_hi)}")
    check_sign(Fraction("0.77"), True)
    check_sign(Fraction("0.270671"), True)
    check_sign(Fraction("0.270670"), False)


if __name__ == "__main__":
    main()
