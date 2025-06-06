def xor_from_gates(X, Y):
    not_X = int(not X)
    not_Y = int(not Y)
    
    and1 = X and not_Y
    and2 = not_X and Y
    
    Z = and1 or and2
    return int(Z)

# Test all combinations
print("X Y -> Z (XOR)")
for X in [0, 1]:
    for Y in [0, 1]:
        Z = xor_from_gates(X, Y)
        print(f"{X} {Y} -> {Z}")

