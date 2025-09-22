from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent, Xor
from itertools import product

# Define generic propositional variables
P, Q = symbols('P Q')

# Define expressions with labels, formulas, and human-readable statements
expressions = {
    "a) It is raining outside if and only if it is a cloudy day (Raining <-> Cloudy)": {
        "expr": Equivalent(P, Q),
        "statements": {P: "Raining", Q: "Cloudy"}
    },
    "b) If you got 80+ in the exam then you can earn A+ (Exam >= 80 -> Earn A+)": {
        "expr": Implies(P, Q),
        "statements": {P: "Exam ≥ 80", Q: "Earn A+"}
    },
    "c) Take either Advil or Tylenol (Advil XOR Tylenol)": {
        "expr": Xor(P, Q),
        "statements": {P: "Took Advil", Q: "Took Tylenol"}
    },
    "d) She studied hard or she is extremely bright (Studied V Bright)": {
        "expr": Or(P, Q),
        "statements": {P: "Studied hard", Q: "Bright student"}
    },
    "e) I am a rock and I am an island (Rock ∧ Island)": {
        "expr": And(P, Q),
        "statements": {P: "There is a rock", Q: "There is an island"}
    },
    "f) It is raining and I will not play football (Raining ∧ Not play)": {
        "expr": And(P, Not(Q)),
        "statements": {P: "It is raining", Q: "Will play football"}
    }
}

# Print truth tables
for label, data in expressions.items():
    expr = data["expr"]
    stmts = data["statements"]

    left_name = stmts[P]
    right_name = stmts[Q]

    print("\nTruth Table for:", label)
    print(f"{left_name:20} | {right_name:20} | Result")
    print("-" * 60)

    for p_val, q_val in product([False, True], repeat=2):
        vals = {P: p_val, Q: q_val}
        result = expr.subs(vals)
        print(f"{int(p_val):^20} | {int(q_val):^20} | {int(bool(result)):^6}")
