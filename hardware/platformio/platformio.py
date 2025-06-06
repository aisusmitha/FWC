# Define the NOR gate
def NOR(a, b):
    return int(not (a or b))

# Logic circuit function
def logic_circuit(P, Q, R):
    A = NOR(P, Q)       # A = ¬(P + Q)
    B = NOR(Q, R)       # B = ¬(Q + R)
    C = NOR(P, R)       # C = ¬(P + R)
    D = NOR(Q, R)       # D = ¬(Q + R)
    
     # Stage 2
    X = NOR(A, B)
    Y = NOR(C, D)
    
    # Stage 3
    F = NOR(X,Y)
    return F

# Test all combinations of inputs P, Q, R
print("P Q R -> F")
for P in [0, 1]:
    for Q in [0, 1]:
        for R in [0, 1]:
            F = logic_circuit(P, Q, R)
            print(f"{P} {Q} {R} -> {F}")

