#include <stdio.h>
#define USE_DIVISION_METHOD

//Division method is fast for large inputs

int main()
{
    unsigned int T, i, l ,b;

#ifdef USE_DIVISION_METHOD
    unsigned int divisor, dividend, remainder;
#else
    unsigned int min;
#endif

    scanf("%u", &T);
    for (i = 0; i < T; i++)
    {
        scanf("%u %u",&l, &b);
        
#ifdef USE_DIVISION_METHOD
        divisor = (l < b) ? l : b;
        dividend = (l > b) ? l : b;
        do
        {
            remainder = dividend % divisor;
            dividend = divisor;
            divisor = remainder;
        }
        while (remainder > 0);
        printf("%u\n", ((l/dividend)*(b/dividend)));
        
#else
        for(min = (l < b ? l : b); min > 0 && ((l % min != 0) || (b % min != 0)); min--);
        printf("%u\n", ((l/min)*(b/min)));
#endif
    }
    return 0;
}