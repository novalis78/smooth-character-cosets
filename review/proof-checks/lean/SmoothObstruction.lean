import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Analysis.Complex.Norm

/-! A completely multiplicative character that is one on primes through Y
is one on every positive Y-smooth integer. An exact cutoff at X is allowed. -/
open scoped BigOperators

namespace SmoothObstruction

def IsSmooth (Y n : ℕ) : Prop := ∀ q, q.Prime → q ∣ n → q ≤ Y

theorem oneOnSmooth (f : ℕ → ℂ) (unitValue : f 1 = 1)
    (mapProduct : ∀ a b, f (a * b) = f a * f b)
    (Y : ℕ) (smallPrimes : ∀ q, q.Prime → q ≤ Y → f q = 1)
    (n : ℕ) (positive : 0 < n) (smooth : IsSmooth Y n) : f n = 1 := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases hOne : n = 1
    · simpa [hOne] using unitValue
    · have hp := Nat.minFac_prime hOne
      have hdiv := Nat.minFac_dvd n
      have hpos := Nat.div_pos (Nat.le_of_dvd positive hdiv) hp.pos
      have hlt := Nat.div_lt_self positive hp.one_lt
      have hrest : IsSmooth Y (n / n.minFac) := by
        intro q hq hqd
        exact smooth q hq (Nat.dvd_trans hqd (Nat.div_dvd_of_dvd hdiv))
      calc
        f n = f (n.minFac * (n / n.minFac)) := congrArg f (Nat.mul_div_cancel' hdiv).symm
        _ = f n.minFac * f (n / n.minFac) := mapProduct _ _
        _ = 1 := by rw [smallPrimes _ hp (smooth _ hp hdiv), ih _ hlt hpos hrest, one_mul]

/-- The natural-number endpoints represent the floors of real cutoffs. -/
noncomputable def smoothThrough (X Y : ℕ) : Finset ℕ := by
  classical
  exact (Finset.range (X + 1)).filter (fun n => 0 < n ∧ IsSmooth Y n)

theorem exactSmoothSum (f : ℕ → ℂ) (unitValue : f 1 = 1)
    (mapProduct : ∀ a b, f (a * b) = f a * f b)
    (Y : ℕ) (smallPrimes : ∀ q, q.Prime → q ≤ Y → f q = 1) (X : ℕ) :
    ∑ n ∈ smoothThrough X Y, f n = ((smoothThrough X Y).card : ℂ) := by
  classical
  calc
    _ = ∑ _n ∈ smoothThrough X Y, (1 : ℂ) := by
      apply Finset.sum_congr rfl
      intro n hn
      have hm : 0 < n ∧ IsSmooth Y n := (Finset.mem_filter.mp hn).2
      exact oneOnSmooth f unitValue mapProduct Y smallPrimes n hm.1 hm.2
    _ = _ := by simp

/-- Any strict magnitude saving at even one length X forces a small prime
with nontrivial character value. -/
theorem strictCancellationDetectsPrime (f : ℕ → ℂ) (unitValue : f 1 = 1)
    (mapProduct : ∀ a b, f (a * b) = f a * f b) (Y X : ℕ)
    (saving : ‖∑ n ∈ smoothThrough X Y, f n‖ < ((smoothThrough X Y).card : ℝ)) :
    ∃ q, q.Prime ∧ q ≤ Y ∧ f q ≠ 1 := by
  classical
  by_contra! hall
  have hones : ∀ q, q.Prime → q ≤ Y → f q = 1 := by
    intro q hq hY
    exact hall q hq hY
  rw [exactSmoothSum f unitValue mapProduct Y hones X, ← Complex.ofReal_natCast,
    Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg (Nat.cast_nonneg _)] at saving
  exact (lt_irrefl _) saving

#print axioms oneOnSmooth
#print axioms exactSmoothSum
#print axioms strictCancellationDetectsPrime

end SmoothObstruction
