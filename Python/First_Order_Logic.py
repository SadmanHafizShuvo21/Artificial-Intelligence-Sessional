class Domain:
    def __init__(self, elements):
        self.elements = elements

class Predicate:
    def __init__(self, name, func):
        self.name = name
        self.func = func  # function that takes one or more arguments

    def evaluate(self, *args):
        return self.func(*args)

class Quantifier:
    def __init__(self, quantifier_type, variable, predicate, domain):
        self.quantifier_type = quantifier_type  # 'forall' or 'exists'
        self.variable = variable
        self.predicate = predicate
        self.domain = domain

    def evaluate(self):
        if self.quantifier_type == 'forall':
            return all(self.predicate.evaluate(x) for x in self.domain.elements)
        elif self.quantifier_type == 'exists':
            return any(self.predicate.evaluate(x) for x in self.domain.elements)
        else:
            raise ValueError("Unknown quantifier")

# Example: ∀x IsEven(x)
domain = Domain([2, 4, 6, 8])

def is_even(x):
    return x % 2 == 0

P = Predicate("IsEven", is_even)
Q = Quantifier("forall", "x", P, domain)
R = Quantifier("exists", "x", P, domain)

print("∀x IsEven(x):", Q.evaluate())  # Output: True
print("∃x IsEven(x):", R.evaluate())  # Output: True
