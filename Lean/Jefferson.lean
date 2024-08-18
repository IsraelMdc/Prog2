/-
Arquivo com as soluções das questões do trabalho 2 de Lógica.
Autor: Jefferson O. Andrade
Data: 2023-06-15
-/

/- Questão 1 -/
example {p q r : Prop} : (p ∧ q) ∧ r ↔ p ∧ (q ∧ r) :=
  Iff.intro 
    (fun h₁ : (p ∧ q) ∧ r => 
      have hpq : p ∧ q := And.left h₁
      have hr : r := And.right h₁
      have hp : p := And.left hpq
      have hq : q := And.right hpq
      have hqr : q ∧ r := And.intro hq hr
      show p ∧ (q ∧ r) from And.intro hp hqr)
    (fun h₁ : p ∧ (q ∧ r) =>
      have hp : p := And.left h₁
      have hqr : q ∧ r := And.right h₁
      have hq : q := And.left hqr
      have hr : r := And.right hqr
      show (p ∧ q) ∧ r from And.intro (And.intro hp hq) hr)

/- Questão 2 -/
example {p q r : Prop} : (p ∨ q) ∨ r ↔ p ∨ (q ∨ r) := 
  Iff.intro
    /- (p ∨ q) ∨ r → p ∨ (q ∨ r) -/
    (fun h₁ : (p ∨ q) ∨ r =>
      Or.elim h₁
        /- (p ∨ q) → p ∨ (q ∨ r) -/
        (fun h₂ : p ∨ q => 
          Or.elim h₂ 
          /- p → p ∨ (q ∨ r) -/
          (fun h₃ : p =>
            show p ∨ (q ∨ r) from Or.intro_left (q ∨ r) h₃)
          /- q → p ∨ (q ∨ r) -/
          (fun h₃ : q =>
            have hqr : q ∨ r := Or.intro_left r h₃
            show p ∨ (q ∨ r) from Or.intro_right p hqr))
        /- r → p ∨ (q ∨ r) -/
        (fun h₃ : r =>
          have hqr : q ∨ r := Or.intro_right q h₃
          show p ∨ (q ∨ r) from Or.intro_right p hqr))
    /- p ∨ (q ∨ r) → (p ∨ q) ∨ r -/
    (fun h₁ : p ∨ (q ∨ r) => 
      Or.elim h₁
        /- p → (p ∨ q) ∨ r -/
        (fun h₂ : p =>
          have hpq : p ∨ q := Or.intro_left q h₂
          show (p ∨ q) ∨ r from Or.intro_left r hpq)
        /- (q ∨ r) → (p ∨ q) ∨ r -/
        (fun h₂ : q ∨ r => 
          Or.elim h₂
            /- q → (p ∨ q) ∨ r -/
            (fun h₃ : q =>
              have hpq : p ∨ q := Or.intro_right p h₃
              show (p ∨ q) ∨ r from Or.intro_left r hpq)
            /- r → (p ∨ q) ∨ r -/
            (fun h₃ : r =>
              show (p ∨ q) ∨ r from Or.intro_right (p ∨ q) h₃)))