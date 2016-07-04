#include <stdio.h>

int main()
{
    unsigned int T, N, i, j, d1, d2, d3, d4, d5, carry;
    scanf("%u", &T);

    for (i = 0; i < T; i++)
    {
        scanf("%u", &N);
        d1 = 1;
        d2 = d3 = d4 = d5 = 0;
        
        for (j = 0; j < N; j++)
        {
        	d1 <<= 1;
        	if (d1 >= 10) { d1 -= 10; carry = 1; } else carry = 0;
        	
			d2 = (d2 << 1) + carry;
        	if (d2 >= 10) { d2 -= 10;  carry = 1; } else carry = 0;
        	
        	d3 = (d3 << 1) + carry;
        	if (d3 >= 10) { d3 -= 10;  carry = 1; } else carry = 0;
        	
        	d4 = (d4 << 1) + carry;
        	if (d4 >= 10) { d4 -= 10;  carry = 1; } else carry = 0;
        	
        	d5 = (d5 << 1) + carry;
        	if (d5 >= 10) d5 -= 10;
        }
        printf("%u\n", ((d5 * 10000) + (d4 * 1000) + (d3 * 100) + (d2 * 10) + d1) - 1);
    }
    return 0;
}