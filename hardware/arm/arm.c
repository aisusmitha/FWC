#include <stdio.h>

int AND(int a, int b) {
    return a & b;
}

int OR(int a, int b) {
    return a | b;
}

int NAND(int a, int b) {
    return !(a & b);
}

int NOR(int a, int b) {
    return !(a | b);
}

int main() {
    int a, b;
    printf("A B | AND OR NAND NOR\n");
    printf("----------------------\n");
    for (a = 0; a <= 1; a++) {
        for (b = 0; b <= 1; b++) {
            printf("%d %d |  %d   %d    %d    %d\n", a, b, AND(a,b), OR(a,b), NAND(a,b), NOR(a,b));
        }
    }

    printf("\nGate Mapping:\n");
    printf("P = NOR  => 2\n");
    printf("Q = NAND => 4\n");
    printf("R = OR   => 1\n");
    printf("S = AND  => 3\n");
    printf("\nCorrect Option: (A) P–2, Q–4, R–1, S–3\n");

    return 0;
}

