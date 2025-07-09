#include <stdio.h>

// Define NOR gate function
int NOR(int a, int b) {
    return !(a || b);  // Logical NOR
}

// Logic circuit function
int logic_circuit(int P, int Q, int R) {
    int A = NOR(P, Q);   // A = ¬(P + Q)
    int B = NOR(Q, R);   // B = ¬(Q + R)
    int C = NOR(P, R);   // C = ¬(P + R)
    int D = NOR(Q, R);   // D = ¬(Q + R)

    // Stage 2
    int X = NOR(A, B);
    int Y = NOR(C, D);

    // Stage 3
    int F = NOR(X, Y);

    return F;
}

int main() {
    int P, Q, R;
    printf("P Q R -> F\n");

    for (P = 0; P <= 1; P++) {
        for (Q = 0; Q <= 1; Q++) {
            for (R = 0; R <= 1; R++) {
                int F = logic_circuit(P, Q, R);
                printf("%d %d %d -> %d\n", P, Q, R, F);
            }
        }
    }

    return 0;
}

