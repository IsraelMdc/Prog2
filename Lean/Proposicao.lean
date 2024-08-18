/-
Arquivo com as soluções das questões do trabalho 2 de Lógica.
Autor: Israel Magalhães do Carmo
Data: 2023-07-06
-/

/-
example {p q r : Prop} : (p → (q → r)) ↔ (p ∧ q → r) := 
  Iff.intro
  (
  fun (hp : p) : q → r => fun (hq :q) : r =>
   have hr : r := And.right hr
  have hq : q := And.left hq
  )

  
  (fun h1 : (p ∧ q → r) =>
  have hpq : p ∧ q := And.left h1
  have hp : p := And.left h1
    _sorry
  )
  -/




  
/-
example : ((p ∨ q) → r) ↔ (p → r) ∧ (q → r) := 
example : ¬(p ∨ q) ↔ ¬p ∧ ¬q := 
example : ¬p ∨ ¬q → ¬(p ∧ q) := 
-/
example : ∀ p : Prop, ¬(p ∧ ¬p) :=
  λ p h : p ∧ ¬p
    (h.right h.left)

section
  variable p : Prop

  example : ¬ (p ∧ ¬ p) :=
    assume h : p ∧ ¬ p,
      show false, from  (and.left h) (and.right h) 
end

/-
example : p ∧ ¬q → ¬(p → q) := 
example : ¬p → (p → q) := 
example : (¬p ∨ q) → (p → q) := 
example : p ∨ False ↔ p :=
example : p ∧ False ↔ False := 
example : (p → q) → (¬q → ¬p) := 
-/