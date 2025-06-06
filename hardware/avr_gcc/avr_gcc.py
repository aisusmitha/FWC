# Function to calculate the output of Circuit A
def calculate_circuit_A(A, B):
    # Simplified Boolean expression: NOT A OR B
    return int(not A or B)

# Function to calculate the output of Circuit B
def calculate_circuit_B(A, B):
    # Simplified Boolean expression: NOT A AND B
    return int(not A and B)

# Function to calculate the output of Circuit C
def calculate_circuit_C(A, B):
    # Simplified Boolean expression: A AND NOT B
    return int(A and not B)

# Function to calculate the output of Circuit D
def calculate_circuit_D(A, B):
    # Simplified Boolean expression: (NOT A AND NOT B) OR (A AND B) (XNOR)
    return int((not A and not B) or (A and B))

# Store the truth tables
truth_tables = {
    "Circuit A": [],
    "Circuit B": [],
    "Circuit C": [],
    "Circuit D": [],
}

# Generate truth tables for all possible inputs
print("Generating Truth Tables:")
print("A B | Q_A | Q_B | Q_C | Q_D")
print("----|-----|-----|-----|-----")

for A_val in [0, 1]:
    for B_val in [0, 1]:
        # Convert integer inputs to boolean for logic operations
        A_bool = bool(A_val)
        B_bool = bool(B_val)

        q_a = calculate_circuit_A(A_bool, B_bool)
        q_b = calculate_circuit_B(A_bool, B_bool)
        q_c = calculate_circuit_C(A_bool, B_bool)
        q_d = calculate_circuit_D(A_bool, B_bool)

        truth_tables["Circuit A"].append(q_a)
        truth_tables["Circuit B"].append(q_b)
        truth_tables["Circuit C"].append(q_c)
        truth_tables["Circuit D"].append(q_d)

        print(f"{A_val} {B_val} |  {q_a}  |  {q_b}  |  {q_c}  |  {q_d}")

print("\n--- Analysis ---")

# Compare truth tables numerically
# This part confirms that all truth tables are numerically distinct.
# If the problem statement is taken literally (3 are identical), then the problem itself has an issue.
unique_patterns = {}
for circuit_name, tt_values in truth_tables.items():
    pattern = tuple(tt_values) # Convert list to tuple for hashable key
    if pattern not in unique_patterns:
        unique_patterns[pattern] = []
    unique_patterns[pattern].append(circuit_name)

if len(unique_patterns) == 1:
    print("All circuits produce the same output.")
elif len(unique_patterns) == len(truth_tables) - 1:
    print("One circuit is different. Identifying it...")
    for pattern, names in unique_patterns.items():
        if len(names) == 1:
            print(f"The unique circuit is: {names[0]} with output pattern {pattern}")
            break
else:
    print("Based on numerical comparison, all circuits produce different outputs.")
    print("This contradicts the problem statement that 'three circuits give the same output except one'.")


print("\n--- Logical Reasoning for 'Odd One Out' ---")
print("Despite the numerical differences in truth tables, problems like this often imply a relationship between circuits.")
print("Let's review the simplified logical expressions:")
print("Circuit A: Q = NOT A OR B  (Logical Implication: A implies B)")
print("Circuit B: Q = NOT A AND B (One term of XOR)")
print("Circuit C: Q = A AND NOT B (Other term of XOR)")
print("Circuit D: Q = (NOT A AND NOT B) OR (A AND B) (XNOR: complement of XOR)")

print("\nObservations:")
print("1. Circuits B and C are the two distinct product terms that sum up to form an XOR gate ($A \oplus B = A\overline{B} + \overline{A}B$).")
print("2. Circuit D is an XNOR gate, which is the logical complement of an XOR gate. Thus, D is inherently related to B and C.")
print("3. Circuit A (Logical Implication: $A \implies B$) represents a different fundamental Boolean operation compared to the XOR/XNOR family.")

print("\nConclusion: The circuit that is logically the 'odd one out' is Circuit A.")
