#include <stdio.h>
#include <stdlib.h>

int main() 
{
    unsigned long long N, ans, i, temp;
    unsigned char *buf;
    unsigned long long freq[26] = {0};
    
    scanf("%llu", &N);
    buf = (char*)malloc(N+1);
    
    scanf("%s", buf);
    
    for (i = 0; i < N; i++)
        freq[buf[i] - 97]++; 
    
    ans = N;
    
    for (i = 0; i < 26; i++)
    {
        temp = freq[i];
        temp = (temp * (temp - 1)) >> 1;
        ans += temp;        
    }        
    
    printf("%llu", ans);
    free(buf);
    return 0;
}