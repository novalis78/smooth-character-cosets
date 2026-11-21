import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Scalar identities used in the signed-discrepancy calculation.
The inputs are abstract. No existence or estimate for a geometric host is assumed here. -/

namespace Nonresidue.SignedMean

theorem average_rows {I : Type*} [Fintype I] [Nonempty I]
    (thick gap : I → ℝ) (err projected : ℝ)
    (hrow : ∀ i, thick i ≤ gap i + err)
    (hproj : ∑ i, thick i = (Fintype.card I : ℝ) * projected) :
    projected ≤ (∑ i, gap i) / (Fintype.card I : ℝ) + err := by
  have hc : (0 : ℝ) < Fintype.card I := by exact_mod_cast Fintype.card_pos
  have h := Finset.sum_le_sum (s := Finset.univ) (fun i _ => hrow i)
  rw [hproj, Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ,
    nsmul_eq_mul] at h
  apply sub_le_iff_le_add.mp
  apply (le_div_iff₀ hc).mpr
  linarith

theorem count_residual (m k rd logTwoPi level weight place euler localErr gamma rounding : ℝ)
    (hk : k ≠ 0) :
    weight + m * (rd - logTwoPi) + m * level -
      ((m - 1 + m * (m - 1) / (2 * k)) * (rd - logTwoPi) -
       (m - 1) / (2 * k) * rd + (m + m * (m - 1) / (2 * k)) * level +
       euler + localErr + place - gamma + rounding) =
    (1 - (m - 1)^2 / (2 * k)) * rd -
      (1 - m * (m - 1) / (2 * k)) * logTwoPi -
      m * (m - 1) / (2 * k) * level + (weight - place) -
      euler - localErr + gamma - rounding := by
  field_simp
  ring

theorem lattice_recombination
    (ask gain cc height fo divSum mass logT weight vol m level
      muN muM localCost : ℝ) :
    ask - (divSum - mass * (weight + m * vol)) =
      mass * (weight + m * vol + m * level - logT) +
      (ask - gain) + (muM + gain + fo - localCost - muN) +
      (cc + height - fo - (divSum - mass * logT)) +
      (muN - height - cc) - muM + (localCost - m * mass * level) := by
  ring

theorem complementary_discrepancy
    (ask gain cc height fo divSum mass logT m level muN muM localCost : ℝ) :
    (ask - gain) + (muM + gain + fo - localCost - muN) +
      (cc + height - fo - (divSum - mass * logT)) +
      (muN - height - cc) - muM + (localCost - m * mass * level) =
      ask - divSum + mass * logT - m * mass * level := by
  ring

end Nonresidue.SignedMean
