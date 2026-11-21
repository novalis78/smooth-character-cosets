# An exact arithmetic certificate for the cutoff 0.77

The headline example in the smooth-character manuscript needs the strict inequality \(\mathcal C(1)^{-2}<0.77\). The two-term test below proves \(\mathcal C(1)^{-2}<0.76822\) using rational arithmetic. Carneiro, Milinovich, Quesada-Herrera and Ramos report a stronger numerical bound. This calculation provides an independent check of the margin needed for the example. It uses their Fourier convention, their definition (1.4) and the family in their equations (6.3)–(6.4). [Carneiro et al., §§1 and 6](https://arxiv.org/html/2404.08380v2)

## The Fourier transform and its signed integral

Set \(a=3/7\), \(c=k=1/2\), \(r=(c-\pi t)/a\), and take

\[
\widehat F(t)=\mathbf 1_{\{r\ge0\}}e^{-r}
 \left(\frac{r^3}{3!}+k\frac{r^7}{7!}\right).
\]

Substitution in the inverse Fourier transform with kernel \(e^{2\pi ixt}\) gives

\[
 F(x)=\frac a\pi e^{2icx}
 \left((1+2iax)^{-4}+k(1+2iax)^{-8}\right).
\]

This function belongs to \(L^1(\mathbb R)\) and has real nonnegative Fourier transform. It is an admissible test in (1.4). The equality of the supremum with its restriction to smooth compactly supported transforms in Theorem 4(i) transfers any strict margin to the test class used in the manuscript.

Write
\[
D(F)=\int_{-\infty}^0\widehat F(t)e^{\pi t}\,dt
     -\int_0^\infty|\widehat F(t)|e^{\pi t}\,dt.
\]
Let \(r_0=(1+a)c/a=5/3\) and \(P_j(s)=\sum_{i=0}^j s^i/i!\). Since \(\widehat F\ge0\), \(D(F)\) equals twice the negative-half-line integral minus the integral over the whole line. Substituting \(r\) and integrating integer gamma tails gives

\[
2\pi D(F)=2a\left[
 2e^{-c/a}\left(\frac{P_3(r_0)}{(1+a)^4}
        +k\frac{P_7(r_0)}{(1+a)^8}\right)
 -e^c\left(\frac1{(1+a)^4}+\frac k{(1+a)^8}\right)\right].
\]

Taylor's theorem gives \(e^{-7/6}\ge P_{11}(-7/6)\). The positive Taylor tail gives \(e^{1/2}\le P_{10}(1/2)+(1/2)^{11}/(11!(1-1/24))\). Substitution yields the following rational lower bound.

\[
 2\pi D(F)\ \ge N
 =\frac{39974528538709281866203793183}{124876091520350945280000000000}>0 .
\]

## An upper bound for the norm

Put \(2ax=\tan\theta\) and \(v=\cos^2\theta\). Taking the modulus, using symmetry and collecting the powers of \(\cos\theta\) gives

\[
 \|F\|_1=\frac1\pi\int_0^{\pi/2}v\sqrt{S(v)}\,d\theta,\qquad
 S(v)=|1+kv^2e^{-4i\theta}|^2
     =1+v^2-8v^3+\frac{33}{4}v^4 .
\]

Since \(0\le kv^2\le1/2\), the triangle inequalities give \(1/4\le S(v)\le9/4\). Hence \(z=1-4S(v)/9\) lies in \([0,8/9]\). Write \(b_1=1/2\) and \(b_{j+1}=b_j(2j-1)/(2j+2)\). All coefficients \(b_j\) are positive. The binomial series therefore gives

\[
 \sqrt{S(v)}\le\frac32\left(1-\sum_{j=1}^5 b_jz^j\right).
\]

The right side is a polynomial in \(v\) with rational coefficients. Its integral against \(v\,d\theta/\pi\) is rational since
\[
 \frac1\pi\int_0^{\pi/2}\cos^{2h}\theta\,d\theta
 =\frac{\binom{2h}{h}}{2\cdot4^h}.
\]
Expanding the five terms gives
\[
 \|F\|_1\le U=\frac{3108890602173610151}{11080543933191684096}.
\]
By (1.4), \(\mathcal C(1)\ge 2\pi D(F)/\|F\|_1\). Direct rational comparison gives \((U/N)^2<76822/100000<77/100\). The accompanying standard-library script recomputes the exponential bounds, moments and final comparison from the parameters. The analytic identities above are hand derivations.

## An independent check at the sharp endpoint

This second calculation checks a separate step of the smooth-sum proof. Assume its bound \(|Z_\chi(\alpha+it)|\le Z e^{-k_1u}\) for \(|t|\le e^{L/H}\) and its saddle estimates \(x^\alpha Z/\Psi(x,y)\asymp\sqrt{XH}\), \(\alpha\to1/2\), where \(X=\log x\), \(H=\log y\), \(L=\log p\), \(u=X/H\), and \(Z=\prod_{\ell\le y}(1-\ell^{-\alpha})^{-1}\). Everything below is uniform for fixed \(a_0>0,\eta>0\) in the range \(p^{a_0}\le x\le p,\ y=\eta(\log p)^2\), subject to those hypotheses.

Set \(T=e^{u/2}\) and \(D=e^{u/4}\). The ordinary truncated Perron error is bounded by a constant times
\[
 x^\alpha\sum_{\substack{n\ge1\\P^+(n)\le y}}
 \frac{n^{-\alpha}}{1+T|\log(x/n)|}.
\]
This follows term by term for any coefficient of modulus at most one, including the full weight at \(n=x\). Outside \(|\log(x/n)|\le1/D\) its contribution is at most \(x^\alpha ZD/T\). Inside the window, \((x/n)^\alpha\) is bounded, so it suffices to count the smooth integers there. [Gorodetsky, Lemma 3.5, initial Perron bound](https://doi.org/10.1017/prm.2023.115)

Each such \(n\) exceeds \(D\) for large \(p\). Multiply prime factors of \(n\), with multiplicity, until their running product first reaches \(D\). The resulting divisor satisfies \(D\le d\le yD\). Write \(m=n/d\). Then \(m\) is smooth and \(x/(2yD)\le m\le2x/D\). For each \(m\), eligible \(d\) lie in \([xe^{-1/D}/m,xe^{1/D}/m]\), an interval of length \(O(x/(mD))=O(y)\). The total count is at most
\[
 O\big(y\Psi(2x/D,y)\big)
 \ \ll\ y(2x/D)^\alpha Z,
\]
where the last step sums \((2x/(Dm))^\alpha\ge1\) for eligible smooth \(m\).

On dividing these two errors by \(\Psi(x,y)\), the factor \(\sqrt{XH}\,y\) is \(e^{o(u)}\), whereas \(D/T=e^{-u/4}\) and \(D^{-\alpha}=e^{-(1/8+o(1))u}\). The vertical integral contributes \(O(x^\alpha Z\,e^{-k_1u}\log(2T))\), giving the claimed exponential relative saving. This route verifies the sharp passage under the indicated analytic hypotheses even when \(x\) itself is a smooth integer.
