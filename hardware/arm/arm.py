def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NAND(a, b):
    return int(not (a & b))

def NOR(a, b):
    return int(not (a | b))

# Input combinations
inputs = [(0,0), (0,1), (1,0), (1,1)]

print("A B | AND OR NAND NOR")
print("----------------------")
for a, b in inputs:
    print(f"{a} {b} |  {AND(a,b)}   {OR(a,b)}    {NAND(a,b)}    {NOR(a,b)}")

# Match logic
print("\nGate Mapping:")
print("P = NOR  => 2")
print("Q = NAND => 4")
print("R = OR   => 1")
print("S = AND  => 3")
print("\nCorrect Option: (A) P–2, Q–4, R–1, S–3")

