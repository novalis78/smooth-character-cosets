# Proposition 1 in the smooth-character manuscript

**Assessment.** Reading the upper half of Chirre's Theorem 1(i) in degree one and combining it with the draft's smooth-number asymptotic reproduces the stated ordinary-sum bound, including the threshold \(2/e^2\). The reasoning below is a hand derivation. The companion Python script independently encloses the elementary constants using rational arithmetic.

### The moving line

Write \(L=\log p\), \(J=\log L\), \(X=\log x=\theta L\), \(H=\log y\), \(u=X/H\). With \(V=\sqrt{x}\log x\), \(|t|\le V\), the analytic conductor satisfies \(\log Q\in[L,(1+\theta/2)L+O(J)]\). Thus \(\log\log Q=J+O(1)\). On \(\sigma=1/2+\lambda/(2J)\) with \(\lambda\) in a fixed compact subinterval of the positive reals, \((1-\sigma)^2\log\log Q\ge1\) for large \(p\). The leading term of the upper bound equals

\[
\frac{\log Q}{2\log\log Q}\log\bigl(1+(\log Q)^{1-2\sigma}\bigr).
\]

Here \((\log Q)^{1-2\sigma}=e^{-\lambda}(1+O(1/J))\). The second term and the upper error in the source are both \(O(L/J^2)\). This proves the draft's uniform majorant on the moving line under RH for the individual primitive character. The adverse factor \(1/(\sigma-1/2)\) occurs in Chirre's *lower* error. [Chirre, Theorem 1(i), pp. 2–3](https://arxiv.org/pdf/1805.01119)

### The sharp endpoint

Let \(h=x^{-1/2}\) and let \(\Phi\) be the standard normal distribution function. Gaussian Fourier inversion gives, for every real \(v\),

\[
\frac1{2\pi i}\int_{\Re s=2}\exp(sv+h^2s^2/2)\,\frac{ds}{s}=\Phi(v/h).
\]

One can differentiate the absolutely convergent integral in \(v\) and fix the integration constant by letting \(v\to-\infty\). Substituting \(v=\log(x/n)\) proves the exact Gaussian Perron identity with absolute summability on this line. For a standard normal \(W\), the difference between the averaged sharp sum at \(xe^{hW}\) and the sum at \(x\) is at most \(1+x\mathbb E|e^{hW}-1|=O(\sqrt x)\), including at an integer \(x\). Throughout the contour shift, periodicity and partial summation give \(|L(s,\chi)/s|\le p/\Re s\). The discarded Gaussian tails are bounded by a constant times \(p x^\sigma (x/V)e^{-(\log x)^2/2}\), smaller than any fixed negative power of \(x\) since \(p\le x^{1/a}\).

### An independent maximum calculation

Taking \(\lambda=\log(1/\theta)+s_0\), where \(s_0>0\) is fixed, gives the exponent coefficient above \(\log\sqrt x\) at most \(\log(1/\theta)+s_0+g(\theta)+o(1)\), times \(u\). Write \(z=\theta/(2+\theta)\). Then

\[
g(\theta)=\bigl(1/\theta+1/2\bigr)\log(1+\theta)
=\frac1{2z}\log\frac{1+z}{1-z}
=\int_0^1\frac{ds}{1-z^2s^2}.
\]

The integrand increases with \(z\) throughout \(0<z\le1/3\). Thus \(g(\theta)\le g(1)=3\log(2)/2\) on the entire range. Subtracting this maximum and \(\log(1/\theta)\) from the coefficient \(1+\log(2\sqrt\eta/\theta)\) in the saddle estimate gives \(M(\eta)=1+\tfrac12\log(\eta/2)\). A fixed \(0<s_0<M(\eta)/2\) exists for every fixed \(\eta>2/e^2\). All the \(o(1)\) terms then vanish uniformly for \(\theta\in[a,1]\). The additive \(O(\sqrt x)\) is absorbed since the saddle coefficient is itself uniformly positive. Although the envelope takes its maximum at \(\theta=1\), the ordinary character sum at exactly \(x=p\) is zero.

Run `python3 check_ordinary_margin.py` to enclose the threshold, the margin at \(0.77\), and the margins just above and below the threshold. The proof gives a sufficient cutoff and does not determine an optimal cutoff for character sums.
