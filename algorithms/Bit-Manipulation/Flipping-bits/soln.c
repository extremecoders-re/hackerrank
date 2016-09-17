#include <stdio.h>

int main() {

    int i, T;
    unsigned int x;
    scanf("%d", &T);
    for (i = 0; i < T; i++)
    {
        scanf("%u", &x);
        printf("%u\n", ~x);
    }
    return 0;
}
