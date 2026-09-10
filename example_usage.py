from client import RobinsonUnifier

def main():
    print("=== Testing Neuro-Symbolic Robinson Unification ===")
    unifier = RobinsonUnifier()

    t1 = ("Parent", "?X", "Bob")
    t2 = ("Parent", "Alice", "?Y")
    subst = unifier.unify(t1, t2)
    print(f"Unifying {t1} with {t2}:")
    print(f"Substitution: {subst}")

    assert subst == {"?X": "Alice", "?Y": "Bob"}
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
