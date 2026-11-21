# Smooth integers in multiplicative cosets at a squared-logarithmic cutoff

Lennart Lopin (Euler's Identity LLC, ORCID [0009-0001-2751-2060](https://orcid.org/0009-0001-2751-2060))

Preprint: [`paper/smooth-character-cosets.pdf`](paper/smooth-character-cosets.pdf) (source in the same folder).
Archived version: Zenodo DOI to follow.

## Result

Let χ be a nonprincipal character modulo a prime p and assume the Riemann hypothesis
for L(s, χ). Fix 0 < a < 1 and put y = η(log p)² with η > 𝒞(1)⁻², the Fourier extremal
constant of Carneiro, Milinovich, Quesada-Herrera and Ramos
([Math. Comp., doi:10.1090/mcom/4154](https://doi.org/10.1090/mcom/4154)). Then,
uniformly in χ and p^a ≤ x ≤ p,

    Σ_{n ≤ x, P⁺(n) ≤ y} χ(n)  =  O(Ψ(x, y) e^{−bu}),   u = log x / log y,   b = b(a, η) > 0,

and the ordinary sum Σ_{n ≤ x} χ(n) satisfies the same bound for every η > 2/e².
Under Dirichlet GRH, every coset of every subgroup of (ℤ/pℤ)ˣ of index m ≤ e^{bu/2}
receives its expected share Ψ(x, y)/m of y-smooth integers up to x, with relative error
O(e^{−bu/2}). The published bounds allow η = 0.77. The certified bound
𝒞(1)⁻² < 0.760777412 ([doi:10.5281/zenodo.24408857](https://doi.org/10.5281/zenodo.24408857),
[repository](https://github.com/novalis78/least-nonresidue-two-shift)) allows every η ≥ 0.7608.

Applied to quadratic characters, the theorem forces a quadratic nonresidue below y.
Admissibility of some η < 𝒞(1)⁻² would therefore improve the known bound for the
least quadratic nonresidue. The argument does not show that 𝒞(1)⁻² is optimal.

The closest earlier uniform estimate we know of, Dong–Zhao–Zhou
([arXiv:2611.11389](https://arxiv.org/abs/2611.11389), Theorem 1.4), needs a cutoff of
order (log q)²(log log q)^C with C > 6. Section 1 of the preprint compares the result
with Granville–Soundararajan, Croot–Granville–Pemantle–Tetali, Soundararajan,
Lagarias–Soundararajan and Harper.

## Contents

| Path | What it is |
| --- | --- |
| `paper/` | The preprint (LaTeX source and PDF). |
| `predecessor/` | `smooth-quadratic-equidistribution`: the quadratic-residue case under full Dirichlet GRH, which the preprint generalizes. |
| `working-notes/` | Exploratory notes, 20–21 November 2026, on whether n_p = o((log p)²) under GRH (the "growth-rate" question). They are unreviewed working drafts and may contain errors. The scripts reproduce the fixed-prime examples in `growth-rate-continued-fractions` and `growth-rate-seeded-cycles`. `SignedMean.lean` holds scalar identities used in `growth-rate-signed-mean`. |
| `review/` | Pre-publication checks. `zbmath-forward-citations.xlsx` screens zbMATH forward citations of all works cited in the preprint (retrieved 2026-11-21). |

The first commit imports the working copy unchanged. Later commits record every edit
made for deposit.

## Building

```sh
cd paper && pdflatex smooth-character-cosets.tex && pdflatex smooth-character-cosets.tex
```

The scripts in `working-notes/` need only the Python standard library
(`python3 working-notes/check_seeded_cycles.py`).

## Status

- Mathematical review of the preprint: done (Claude, 2026-11-21).
- Line-by-line check of the cited theorem and equation numbers: in progress.
- Priority questions to A. J. Harper and Z. Dong: to be sent with the archived link.

## Provenance and licence

OpenAI Codex assisted with the literature search, derivations and drafting.
Anthropic's Claude checked the arguments and cited statements before deposit. The
author is responsible for any errors. The papers and notes (`*.tex`, `*.pdf`) are
licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The scripts
and the Lean file are under the MIT License (`LICENSE`).
