"""Check one Fourier witness for C(1) in Carneiro et al., arXiv:2404.08380.

Requires Python 3.10+, SymPy, and python-flint. From the download directory run

    python3 -m pip install sympy python-flint
    python3 verify_single_shift_36_arb.py

The only number-theoretic input is required when interpreting the output:
Theorem 1 of Carneiro et al. bounds the asymptotic least-quadratic-nonresidue
constant by C(1)^(-2) under GRH. The Fourier calculation itself is unconditional.

Define a=3/10, c=4/5 and R(z)=sum_{j=0}^{35} r_j z^j with rationals below.
Write R(2w-1)=sum_{k=1}^{36} d_k w^(k-1), P(u)=sum_k d_k u^k/k!,
and set Fhat(t)=exp(-u)P(u) for u=(c-pi*t)/a >= 0, zero otherwise.
The inverse Fourier transform uses exp(+2*pi*i*x*t). Up to a unit phase,
F(x)=(a/pi)*sum_k d_k/(1+2*i*a*x)^(k+1); hence F is integrable.

In the authors' definition (1.4), take A=1. After u-substitution and
theta=atan(2*a*x), the quotient is

  2*pi*a*exp(c) [ integral_m^inf exp(-h*u)P(u)du
                  -integral_0^m exp(-h*u)|P(u)|du ] / D,

where h=1+a, m=c/a, D=integral_0^(pi/2) |R(exp(-2*i*theta))|dtheta.
In the denominator, the identity 1/(1+i*tan(theta))=(1+exp(-2*i*theta))/2
turns the original integrand into exp(-2*i*theta)*R(exp(-2*i*theta));
the leading factor has unit modulus.

The integrands in the numerator have explicit antiderivatives between the
roots of P. SymPy isolates all interior real roots using exact rationals,
and Arb encloses the remaining elementary evaluations.

For D let f(theta)=R(exp(-2*i*theta)), K=sum_j 4*j^2*|r_j|. On each
panel [v,v+b] compare f with its linear interpolant. The norm of the error
at v+t is bounded by K*t*(b-t)/2 (linear interpolation remainder via the
Dirichlet Green kernel). The integral of the norm of the interpolant is at
most b*(|f(v)|+|f(v+b)|)/2 by convexity. Summing gives an upper bound on D
by the trapezoidal sum of endpoint norms plus K*(pi/2)*b^2/12. No
differentiability of the modulus is assumed. All transcendental and complex
arithmetic uses Arb outward-rounded balls.
"""

from fractions import Fraction
from math import comb, factorial

from flint import acb, arb, ctx, fmpq
from sympy import Poly, Rational, Symbol


def ball(value):
    value = Fraction(value)
    return arb(fmpq(value.numerator, value.denominator))


def to_sympy(value):
    return Rational(value.numerator, value.denominator)


def from_sympy(value):
    return Fraction(int(value.p), int(value.q))


def polynomial_value(coefficients, argument):
    result = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        result = result * argument + coefficient
    return result


def main():
    if not __debug__:
        raise RuntimeError("Run without Python's -O flag to enable certificate checks.")
    ctx.prec = 200
    r = [Fraction(i, 1000000) for i in (
        1000000, 4815715, 8710552, 7617483, 4487466, 3434816, 2345152, 1189056,
        938349, 510409, 258500, 235574, 72629, 71024, 46027, 3286,
        28100, -2855, 6332, 5339, -4625, 6832, -4287, 2822,
        -479, -732, 1601, -1653, 1541, -1050, 1019, -464,
        1320, 215, 2070, 5064,
    )]
    a, c = Fraction(3, 10), Fraction(4, 5)
    h, m = 1 + a, c / a
    degree = len(r)
    # Index k of d is the degree in P. P(0)=0 ensures F is integrable.
    d = [Fraction(0)] + [
        sum(r[j] * comb(j, k) * 2**k * (-1)**(j-k) for j in range(k, degree))
        for k in range(degree)
    ]
    u = Symbol("u")
    polynomial = Poly(sum(to_sympy(d[k]) * u**k / factorial(k)
                          for k in range(1, degree+1)), u)
    assert polynomial.eval(0) == 0 and polynomial.eval(to_sympy(m)) != 0
    roots = polynomial.intervals(
        inf=0, sup=to_sympy(m), eps=Rational(1, 10**30)
    )
    points = [ball(0)]
    for (left, right), multiplicity in roots:
        if left == right == 0:
            continue
        assert 0 < left <= right < to_sympy(m) and multiplicity == 1
        points.append(ball(from_sympy(left)).union(ball(from_sympy(right))))
    points.append(ball(m))
    assert len(points) == 4
    print("Number of interior roots: ", len(points)-2)

    # tail(u) is the signed integral of exp(-h*t)*P(t) from u to infinity.
    tail_coefficients = [
        ball(sum(d[k] / h**(k-j+1) for k in range(j, degree+1)) / factorial(j))
        for j in range(degree+1)
    ]
    tails = [
        (-ball(h)*point).exp() * polynomial_value(tail_coefficients, point)
        for point in points
    ]
    penalty = sum(abs(left-right) for left, right in zip(tails, tails[1:]))
    numerator = 2 * arb.pi() * ball(a) * ball(c).exp() * (tails[-1]-penalty)
    assert numerator > 0

    panels = 32768
    length = arb.pi()/2
    step = length/panels
    coefficients = [ball(value) for value in r]

    def modulus(z):
        return abs(polynomial_value(coefficients, z))

    trapezoid = (modulus(acb(1)) + modulus(acb(-1)))/2
    for j in range(1, panels):
        z = acb(0, -2*j*step).exp()
        trapezoid += modulus(z)
    trapezoid *= step
    second_derivative_bound = ball(sum(4*j*j*abs(value)
                                       for j, value in enumerate(r)))
    correction = length * second_derivative_bound * step**2 / 12
    denominator_bound = trapezoid + correction
    assert denominator_bound > 0
    upper_bound = (denominator_bound/numerator)**2
    print("Scaled numerator:        ", numerator)
    print("Trapezoidal sum:         ", trapezoid)
    print("One-sided correction:    ", correction)
    print("Upper bound for C(1)^-2: ", upper_bound)
    # The comparison succeeds only when the two balls are strictly disjoint.
    assert upper_bound < ball(Fraction(760777412, 1_000_000_000))
    print("Certified comparison: C(1)^(-2) < 0.760777412 < 0.76079030")


if __name__ == "__main__":
    main()
