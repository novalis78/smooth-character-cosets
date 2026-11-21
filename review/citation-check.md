# Citation check (2026-11-21)

Each theorem and equation number cited in `paper/smooth-character-cosets.tex` was checked
against its source by an independent reader (a Claude subagent). It fetched every source,
read the cited statements, and compared their hypotheses with the manuscript's.

**Result.** All 11 citations are confirmed. No cited result needs GRH for all characters
where the manuscript claims that RH for the single L(s, χ) suffices. The single-character
bound for the argument S(t, χ) comes from Carneiro–Chandee–Milinovich (Theorem 5 and
Example 8), not from the GRH statement (3.4) of Carneiro et al. The manuscript already
says so.

| # | Source | Cited item | Verdict |
| --- | --- | --- | --- |
| 1a | Carneiro–Milinovich–Quesada-Herrera–Ramos, arXiv:2404.08380v2 | (1.1); Theorems 1 and 5 (1.14600 < C(1) < 1.14731) | Confirmed |
| 1b | same | Theorem 4(i), (4.13), §4.4: the supremum can be taken over F with F̂ ∈ C_c^∞ | Confirmed |
| 1c | same | (3.1)/Lemma 9 explicit formula for primitive χ (unconditional) | Confirmed. It also needs decay in the strip, now stated via Paley–Wiener as in §4.1. |
| 1d | same | (3.3)–(3.4) zero counting, ½-multiplicity endpoint convention | Confirmed. (3.4) is a GRH statement, replaced by CCM for a single χ. |
| 2 | Carneiro–Chandee–Milinovich, arXiv:1503.00955 (Math. Z. 281, 2015) | Theorem 5, Example 8: S(t, χ) bound under RH for L(s, χ) alone | Confirmed. Stated for t > 0; S(0, χ) follows by t → 0⁺, now noted. |
| 3 | Chirre, arXiv:1805.01119 | Theorem 1(i) upper bound, degree-1 analytic conductor | Confirmed. The adverse μ(σ) factor occurs only in the lower bound. |
| 4 | Gorodetsky, Proc. Roy. Soc. Edinburgh A 155 (2025) | Lemma 3.5, (3.10)–(3.16), truncated Perron with a positive majorant | Confirmed (journal numbering; arXiv v3 numbers it (3.7)–(3.11)). The free abscissa σ is set equal to the saddle α, now stated. |
| 5 | Hildebrand–Tenenbaum, JTNB 5 (1993) | Theorem 1.6, saddle-point formula, uniform for x ≥ y ≥ 2 | Confirmed |
| 6 | Granville–Soundararajan, JAMS 14 (2001), authors' version | Conjecture 1, Theorem 2 under RH for L(s, χ) | Confirmed. The arXiv preprint states Theorem 2 under GRH. Its second part (ordinary sum at (log q)²(log log q)^20) is now cited. |
| 7 | Dong–Zhao–Zhou, arXiv:2611.11389v1 | Theorem 1.4: cutoff (log q + (log x)²)(log₂ q)^C, C > 6 | Confirmed. The whole paper was read and contains nothing at a fixed multiple of (log q)² and no coset corollary. |
| 8 | Croot–Granville–Pemantle–Tetali, ANTS VIII (Penn copy) | §7.3, Lemma 7 under GRH, error Ψ(x, y)(log n)³/√y | Confirmed (numbering differs in another posted copy) |
| 9 | Soundararajan, arXiv:0707.0299 | §4 saddle-weighted distance, √y ≤ q ≤ y^A | Confirmed |
| 10 | Lagarias–Soundararajan, arXiv:1102.4911v2 | Proposition 5.1 under GRH | Confirmed |
| 11 | Harper, arXiv:1208.5992 | Theorem 3 (r ≤ y^b), Proposition 1 (r ≤ x^d) | Confirmed |

Chirre's footnote defines O-notation "for t sufficiently large". The theorem itself states
uniform bounds in the range (1 − σ)² log log C(t) ≥ c, and here C(t) ≥ 3p. No change needed.

## Priority search (about 30 minutes, not exhaustive)

Nothing earlier was found that bounds smooth character sums for x ≤ q at y ≍ (log q)²
(any fixed multiple) with a power-of-u or e^{−bu} saving under RH/GRH, or that proves
equidistribution of y-smooth integers in cosets mod p at that cutoff. Nearest:

- Dong–Zhao–Zhou: cutoff (log q)²(log log q)^C with C > 6.
- Granville–Soundararajan Theorem 2 (second part): S(x, χ) ≪ Ψ(x, (log q)²(log log q)^20).
- Croot–Granville–Pemantle–Tetali Lemma 7; Montgomery–Vaughan 1977 Lemma 2: GRH errors with polynomial-in-log/√y factors.
- Lagarias–Soundararajan; Drappeau (arXiv:1203.1742, 1302.4318): nontrivial only for y ≥ (log x)^{4−ε}.
- Unconditional, other regimes: Soundararajan 2008 and Harper (arXiv:1103.2106), q ≤ y^{4√e−δ}; Hardy–Xu (arXiv:2607.00592); Shparlinski (arXiv:1705.10148); Bourgain–Konyagin–Shparlinski (arXiv:1103.0296).
- Ankeny, Bach, Lamzouri–Li–Soundararajan (arXiv:1309.3595): primes ≤ C(log q)² generate (ℤ/qℤ)ˣ. This is generation, not equidistribution.
