#include <stdio.h>

// XOR using gates: (X AND NOT Y) OR (NOT X AND Y)
int xor_from_gates(int X, int Y) {
    int not_X = !X;
    int not_Y = !Y;

    int and1 = X && not_Y;
    int and2 = not_X && Y;

    int Z = and1 || and2;
    return Z;
}

int main() {
    int X, Y, Z;

    printf("X Y -> Z (XOR)\n");

    for (X = 0; X <= 1; X++) {
        for (Y = 0; Y <= 1; Y++) {
            Z = xor_from_gates(X, Y);
            printf("%d %d -> %d\n", X, Y, Z);
        }
    }

    return 0;
}

