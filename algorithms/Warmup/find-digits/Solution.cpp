#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int findDigits(int num)
{
    int num_copy = num;
    int digit, count;
    count = 0;
    while (num > 0)
        {
        digit = num % 10;
        num /= 10;
        if (digit != 0)
            {
            if ((num_copy % digit) == 0 ) count++;
        }        
    }
    return count;
}


int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int T, num;
    scanf("%d", &T);
    for(int i=0; i<T; i++)
    {
        scanf("%d", &num);
        printf("%d\n", findDigits(num));        
    }
    return 0;
}
