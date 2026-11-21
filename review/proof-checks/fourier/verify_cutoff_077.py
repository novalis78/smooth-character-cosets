"""Exact rational checks for a two-term Fourier witness at eta=77/100.

Run with Python 3.8+ and its standard library. See cutoff_077_derivation.md
for the analytic identities whose rational evaluations are checked here.
"""

from fractions import Fraction as Q
from math import comb, factorial


def exp_partial(argument, degree):
    return sum(argument**j / factorial(j) for j in range(degree + 1))


def multiply(left, right):
    """Multiply polynomials listed in ascending order of degree."""
    result = [Q(0)] * (len(left) + len(right) - 1)
    for i, left_coefficient in enumerate(left):
        for j, right_coefficient in enumerate(right):
            result[i + j] += left_coefficient * right_coefficient
    return result


def weighted_moment(coefficients):
    """Evaluate pi^-1 integral v P(v) dtheta, v=cos(theta)^2, 0<=theta<=pi/2."""
    return sum(c * Q(comb(2 * (j + 1), j + 1), 2 * 4 ** (j + 1))
               for j, c in enumerate(coefficients))


def main():
    a, c, k = Q(3, 7), Q(1, 2), Q(1, 2)
    r = (1 + a) * c / a

    # Taylor's theorem bounds exp(-7/6) from below using odd degree.
    exp_negative_lo = exp_partial(-c / a, 11)
    # Majorize the Taylor tail for exp(1/2) by its first term times a
    # geometric series. The ratio after the degree-11 term is <= (1/2)/12.
    exp_positive_hi = exp_partial(c, 10) + (c**11 / factorial(11)) / (1 - c / 12)
    baseline = (1 + a)**-4 + k * (1 + a)**-8
    gamma_tails = exp_partial(r, 3) / (1 + a)**4 + k * exp_partial(r, 7) / (1 + a)**8
    numerator_lo = 2 * a * (2 * exp_negative_lo * gamma_tails - exp_positive_hi * baseline)

    # S(v)=|1+(1/2) cos^4(theta) exp(-4 i theta)|^2.
    # It lies in [1/4,9/4]. For z=1-4S/9 the binomial series for
    # sqrt(1-z) has strictly negative coefficients after its constant.
    square = [Q(1), Q(0), Q(1), Q(-8), Q(33, 4)]
    z = [-Q(4, 9) * coefficient for coefficient in square]
    z[0] += 1
    z_power = [Q(1)]
    integral = weighted_moment(z_power)
    binomial = Q(1, 2)
    for j in range(1, 6):
        z_power = multiply(z_power, z)
        integral -= binomial * weighted_moment(z_power)
        binomial *= Q(2 * j - 1, 2 * (j + 1))
    norm_hi = Q(3, 2) * integral

    assert numerator_lo == Q(39974528538709281866203793183, 124876091520350945280000000000)
    assert norm_hi == Q(3108890602173610151, 11080543933191684096)
    assert 0 < numerator_lo and 0 < norm_hi
    cutoff_hi = (norm_hi / numerator_lo)**2
    assert cutoff_hi < Q(76822, 100000) < Q(77, 100)
    print('lower bound for 2*pi*D(F):', numerator_lo)
    print('upper bound for ||F||_1:', norm_hi)
    print('Verified by rational comparison: C(1)^(-2) < 0.76822 < 0.77')


if __name__ == '__main__':
    main()
