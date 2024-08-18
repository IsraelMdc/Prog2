/-
logica-trab2.lean

Arquivo com as soluções das questões do trabalho 2 de Lógica.
Autor: Daniel Vieira Lima
Data: 2023-06-21
-/

/- Questão 1 -/

/-
example : (p → (q → r)) ↔ (p ∧ q → r) := sorry
-/
import tactic

variables p q r : Prop

example : (p → (q → r)) ↔ (p ∧ q → r) :=
begin
  split, 

  { intros h₁ h₂,
    cases h₂ with hp hq, 
    apply h₁ hp, 
    exact h₁ hp hq, 
  },

  { intros h₃ hp hq,
    apply h₃, 
    exact ⟨hp, hq⟩, 
  },
end

/- Questão 2 -/

example : ((p ∨ q) → r) ↔ (p → r) ∧ (q → r) := sorry

import tactic

variables p q r : Prop

example : ((p ∨ q) → r) ↔ (p → r) ∧ (q → r) :=
begin
  split, 
  
  { intro h₁,
    split, 

    { intro hp,
      apply h₁, 
      left, 
      exact hp, 
    },

    { intro hq,
      apply h₁, 
      right, 
      exact hq, 
    },
  },

  
  { intros h₂ h₃,
    intro h₄,
    cases h₄ with hp hq, 
    { apply h₂.left, 
      exact hp, 
    },
    { apply h₃.left, 
      exact hq, 
    },
  },
End


/- Questão 3 -/

example : ¬(p ∨ q) ↔ ¬p ∧ ¬q := sorry

import tactic

variables p q : Prop

example : ¬(p ∨ q) ↔ ¬p ∧ ¬q :=
begin
  split, 

  { intro h₁,
    split, 

    { intro hp,
      apply h₁,
      left, 
      exact hp, 
    },

    { intro hq,
      apply h₁,
      right, 
      exact hq, 
    },
  },

  { intro h₂,
    intro h₃,
    cases h₃ with hp hq, 
    { apply h₂.left, 
      exact hp, 
    },
    { apply h₂.right, 
      exact hq, 
    },
  },
End

/- Questão 4 -/

example : ¬(p ∧ ¬p) := sorry

import tactic

variables p q : Prop

example : ¬p ∨ ¬q → ¬(p ∧ q) :=
begin
  intro h₁,
  intro h₂,
  cases h₁ with hnp hnq, 
  { apply hnp, 
    exact h₂.left, 
  },
  { apply hnq, 
    exact h₂.right, 
  },
End


/- Questão 5 -/

example : p ∧ ¬q → ¬(p → q) := sorry

import tactic

variables p : Prop

example : ¬(p ∧ ¬p) :=
begin
  intro h₁,
  have hnp : ¬p := h₁.right,
  have hp : p := h₁.left,
  contradiction,
end


/- Questão 6 -/

example : p ∧ ¬q → ¬(p → q) := sorry

import tactic

variables p q : Prop

example : p ∧ ¬q → ¬(p → q) :=
begin
  intros h₁ h₂,
  apply h₁.right, 
  apply h₂, 
  exact h₁.left, 
end


/- Questão 7 -/

example : ¬p → (p → q) := sorry

import tactic

variables p q : Prop

example : (¬p ∨ q) → (p → q) :=
begin
  intros h₁ h₂,
  cases h₁ with hnp hq,
  { contradiction },
  { exact hq }
end


/- Questão 8 -/

example : (¬p ∨ q) → (p → q) := sorry

import tactic

variables p q : Prop

example : (¬p ∨ q) → (p → q) :=
begin
  intros h₁ h₂, 
  cases h₁ with h₃ h₄, 

  {
    contradiction, 
  },

  {
    exact h₄, 
  },
end


/- Questão 9 -/

example : p ∨ False ↔ p := sorry

import tactic

variable p : Prop

example : p ∨ false ↔ p :=
begin
  split, 

  {
    intro h₁, 
    cases h₁, 

    {
      exact h₁, 
    },

    {
      contradiction, 
    },
  },

  {
    intro h₂, 
    left, 
    exact h₂, 
  },
end


/- Questão 10 -/

example : p ∧ False ↔ False := sorry

import tactic

variables p : Prop

example : p ∧ false ↔ false :=
begin
  split, -- Dividir o teorema em duas direções

  { intro h,
    cases h with hp hfalse,
    exact hfalse,
  },

  { intro h,
    exact false.elim h,
  },
End

/- Questão 11 -/

example : (p → q) → (¬q → ¬p) := sorry

import tactic

variables p q : Prop

example : (p → q) → (¬q → ¬p) :=
begin
  intro h₁,
  intro h₂,
  by_contradiction h₃,
  have h₄ : q := h₁ (by_contradiction h₃),
  contradiction,
end