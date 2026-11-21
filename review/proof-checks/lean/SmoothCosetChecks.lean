import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Analysis.Complex.Norm
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Independent checks of finite steps in the proposed smooth-character argument. -/
open scoped BigOperators
noncomputable section

namespace SmoothCosetChecks

/-- A finite Fourier sum detects the value 1 among the mth roots of unity. -/
theorem rootFilter (m : ℕ) (z : ℂ) (hz : z ^ m = 1) :
    (∑ k ∈ Finset.range m, z ^ k) = if z = 1 then (m : ℂ) else 0 := by
  by_cases h : z = 1
  · simp [h]
  · simp [h, geom_sum_eq h m, hz]

/-- For each sample, z is its quotient character divided by the target's character.
The formula counts the samples landing in that coset. -/
theorem filterCount {ι : Type*} (s : Finset ι) (m : ℕ) (z : ι → ℂ)
    (hz : ∀ i ∈ s, z i ^ m = 1) :
    (∑ k ∈ Finset.range m, ∑ i ∈ s, z i ^ k) =
        ((s.filter (fun i => z i = 1)).card : ℂ) * m := by
  classical
  rw [Finset.sum_comm]
  calc
    _ = ∑ i ∈ s, if z i = 1 then (m : ℂ) else 0 := by
      exact Finset.sum_congr rfl (fun i hi => rootFilter m (z i) (hz i hi))
    _ = _ := by rw [← Finset.sum_filter]; simp

/-- With index r+1, a bound E for each nontrivial quotient-character
sum gives the exact factor r on the discrepancy after multiplication by the index. -/
theorem cosetDiscrepancy {ι : Type*} (s : Finset ι) (r : ℕ) (z : ι → ℂ)
    (hz : ∀ i ∈ s, z i ^ (r + 1) = 1) (E : ℝ)
    (hE : ∀ k ∈ Finset.range r, ‖∑ i ∈ s, z i ^ (k + 1)‖ ≤ E) :
    ‖((s.filter (fun i => z i = 1)).card : ℂ) * ((r + 1 : ℕ) : ℂ) - s.card‖ ≤
        (r : ℝ) * E := by
  classical
  have hf := filterCount s (r + 1) z hz
  rw [Finset.sum_range_succ'] at hf
  simp only [pow_zero, Finset.sum_const, nsmul_eq_mul, mul_one] at hf
  rw [← hf, add_sub_cancel_right]
  simpa using norm_sum_le_of_le (Finset.range r) hE

/-- Real-part loss controls a signed finite weighted sum whenever the weights
are bounded above. Negative weights are allowed. -/
theorem signedDeficit {ι : Type*} (s : Finset ι) (w v : ι → ℝ) (M : ℝ)
    (hw : ∀ i ∈ s, w i ≤ M) (hv : ∀ i ∈ s, v i ≤ 1) :
    (∑ i ∈ s, w i) - M * (∑ i ∈ s, (1 - v i)) ≤ ∑ i ∈ s, w i * v i := by
  rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
  apply Finset.sum_le_sum
  intro i hi
  have h := mul_nonneg (sub_nonneg.mpr (hw i hi)) (sub_nonneg.mpr (hv i hi))
  linarith

/-- A strict Fourier margin D in the all-aligned prime sum survives an additive
error err and forces a total real-part loss of at least (D - err)/M. -/
theorem strictMarginLoss {ι : Type*} (s : Finset ι) (w v : ι → ℝ) (M D err : ℝ)
    (hM : 0 < M) (hw : ∀ i ∈ s, w i ≤ M) (hv : ∀ i ∈ s, v i ≤ 1)
    (hu : (∑ i ∈ s, w i * v i) ≤ (∑ i ∈ s, w i) - D + err) :
    (D - err) / M ≤ ∑ i ∈ s, (1 - v i) := by
  have hd := signedDeficit s w v M hw hv
  apply (div_le_iff₀ hM).2
  rw [mul_comm]
  linarith

/-- On 0 ≤ d ≤ 8, converting a squared Euler-factor ratio 1+d to
logarithms loses at most the explicit factor 9. -/
theorem logEulerLoss (d : ℝ) (hd : 0 ≤ d) (h8 : d ≤ 8) :
    d / 9 ≤ Real.log (1 + d) := by
  have hpos : 0 < 1 + d := by linarith
  have h := Real.log_le_sub_one_of_pos (inv_pos.mpr hpos)
  rw [Real.log_inv] at h
  have hl : d / (1 + d) ≤ Real.log (1 + d) := by
    have hr : (1 + d)⁻¹ + d / (1 + d) = 1 := by
      rw [← one_div, ← add_div, div_self (ne_of_gt hpos)]
    linarith
  apply le_trans _ hl
  exact div_le_div_of_nonneg_left hd hpos (by linarith)

#print axioms strictMarginLoss
#print axioms logEulerLoss
#print axioms rootFilter
#print axioms filterCount
#print axioms cosetDiscrepancy
#print axioms signedDeficit

end SmoothCosetChecks
