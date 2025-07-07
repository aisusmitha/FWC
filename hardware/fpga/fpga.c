#include <stdio.h>

int logic_or(int a, int b) {
    return a | b;
}

int logic_and(int a, int b) {
    return a & b;
}

int compute_output(int a, int b, int c) {
    int or1 = logic_or(a, b);
    int and1 = logic_and(b, c);
    return logic_or(or1, and1);
}

int main() {
    int a, b, c, f;
    printf("A B C | F\n");
    printf("------------\n");

    for (a = 0; a <= 1; a++) {
        for (b = 0; b <= 1; b++) {
            for (c = 0; c <= 1; c++) {
                f = compute_output(a, b, c);
                printf("%d %d %d | %d\n", a, b, c, f);
            }
        }
    }

    printf("\nCorrect input(s) for F = 1:\n");
    for (a = 0; a <= 1; a++) {
        for (b = 0; b <= 1; b++) {
            for (c = 0; c <= 1; c++) {
                if (compute_output(a, b, c) == 1) {
                    printf("A=%d, B=%d, C=%d\n", a, b, c);
                }
            }
        }
    }

    return 0;
}

