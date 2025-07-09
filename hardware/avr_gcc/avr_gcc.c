#include <stdio.h>

// Circuit A: NOT A OR B (A → B)
int calculate_circuit_A(int A, int B) {
    return (!A || B);
}

// Circuit B: NOT A AND B
int calculate_circuit_B(int A, int B) {
    return (!A && B);
}

// Circuit C: A AND NOT B
int calculate_circuit_C(int A, int B) {
    return (A && !B);
}

// Circuit D: (NOT A AND NOT B) OR (A AND B) → XNOR
int calculate_circuit_D(int A, int B) {
    return ((!A && !B) || (A && B));
}

int main() {
    int A, B;
    int truth_A[4], truth_B[4], truth_C[4], truth_D[4];
    int i = 0;

    printf("A B | Q_A | Q_B | Q_C | Q_D\n");
    printf("----|-----|-----|-----|-----\n");

    for (A = 0; A <= 1; A++) {
        for (B = 0; B <= 1; B++) {
            int q_a = calculate_circuit_A(A, B);
            int q_b = calculate_circuit_B(A, B);
            int q_c = calculate_circuit_C(A, B);
            int q_d = calculate_circuit_D(A, B);

            truth_A[i] = q_a;
            truth_B[i] = q_b;
            truth_C[i] = q_c;
            truth_D[i] = q_d;

            printf("%d %d |  %d  |  %d  |  %d  |  %d\n", A, B, q_a, q_b, q_c, q_d);
            i++;
        }
    }

    // Compare truth tables (by printing patterns)
    printf("\n--- Truth Table Patterns ---\n");
    printf("Circuit A: ");
    for (i = 0; i < 4; i++) printf("%d", truth_A[i]);
    printf("\n");

    printf("Circuit B: ");
    for (i = 0; i < 4; i++) printf("%d", truth_B[i]);
    printf("\n");

    printf("Circuit C: ");
    for (i = 0; i < 4; i++) printf("%d", truth_C[i]);
    printf("\n");

    printf("Circuit D: ");
    for (i = 0; i < 4; i++) printf("%d", truth_D[i]);
    printf("\n");

    printf("\n--- Logical Reasoning ---\n");
    printf("Circuit A: Q = NOT A OR B  --> A implies B\n");
    printf("Circuit B: Q = NOT A AND B --> Half of XOR\n");
    printf("Circuit C: Q = A AND NOT B --> Other half of XOR\n");
    printf("Circuit D: Q = (NOT A AND NOT B) OR (A AND B) --> XNOR\n");

    printf("\nConclusion: Circuit A is logically the 'odd one out' (Implication), while B, C, and D relate to XOR/XNOR logic.\n");

    return 0;
}

