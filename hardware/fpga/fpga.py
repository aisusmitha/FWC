def logic_or(a, b):
    return a | b

def logic_and(a, b):
    return a & b

def compute_output(a, b, c):
    or1 = logic_or(a, b)
    and1 = logic_and(b, c)
    f = logic_or(or1, and1)
    return f

# Try all 8 combinations
print("A B C | F")
print("------------")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            f = compute_output(a, b, c)
            print(f"{a} {b} {c} | {f}")

print("\nCorrect input(s) for F = 1:")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            if compute_output(a, b, c) == 1:
                print(f"A={a}, B={b}, C={c}")

