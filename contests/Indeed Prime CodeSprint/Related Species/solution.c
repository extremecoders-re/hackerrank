#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main() 
{
    int i, j, T, N, A, B, min, max, last, *seqA, *seqB;
    
    scanf("%d", &T); // No of test cases
    
    for (i = 0; i < T; i++)
    {
        scanf("%d", &N); //length of the DNA sequence
        
        seqA = (int*) malloc(sizeof(int) * N);
        seqB = (int*) malloc(sizeof(int) * N);
        
        for (j = 0; j < N; j++) scanf("%d", &seqA[j]);
        for (j = 0; j < N; j++) scanf("%d", &seqB[j]);
        
        for (j = 0, last = -1; j < N; j++)
        {
            min = MIN(seqA[j], seqB[j]);
            max = MAX(seqA[j], seqB[j]);
            if (min >= last) last = min;
            else if (max >= last) last = max;
            else
            {
                printf("NO\n");
                break;
            }
        }
        if (j == N) printf("YES\n");
            
        free(seqA);
        free(seqB);
    }    
    return 0;
}