from z3 import * 

# Define domain
Person = DeclareSort("Person")

# Predicates
Parent = Function('Parent', Person, Person, BoolSort())
Grandparent = Function('Grandparent', Person, Person, BoolSort())

# Constants
Jhon = Const('Jhon', Person)
Mary = Const('Mary', Person)
Joe = Const('Joe', Person)

# Solver
s = Solver()

# Variables for rules
x = Const('x', Person)
y = Const('y', Person)
z = Const('z', Person)

# Rule: Parent(x,y) and Parent(y,z) -> Grandparent(x,z)
s.add(ForAll([x, y, z], Implies(And(Parent(x, y), Parent(y, z)), Grandparent(x, z))))

# Facts
s.add(Parent(Jhon, Mary))
s.add(Parent(Mary, Joe))

# Query: prove Grandparent(Jhon, Joe)
s.push()
s.add(Not(Grandparent(Jhon, Joe)))
res = s.check()
print("Result:", res)   

if res == unsat:
    print("✅ Grandparent(Jhon, Joe) is proved.")
else:
    print("❌ Cannot prove Grandparent(Jhon, Joe).")
