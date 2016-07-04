#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char str[10000];
int letterFreq1[26], letterFreq2[26];

int main()
{
	int T, i, l, j, d;
	scanf("%d", &T);
	for (i = 0; i < T; i++)
	{
		memset(str, 0, 10000);
		scanf("%s", &str);
		l = strlen(str);
		if (l % 2 == 1) printf("-1\n");
		else
		{
			memset(letterFreq1, 0, 26 * sizeof(int));
			memset(letterFreq2, 0, 26 * sizeof(int));
			for (j = 0; j < l/2; j++) letterFreq1[str[j]-97]++;
			for (j = l/2; j < l; j++) letterFreq2[str[j]-97]++;
			for (j = 0, d = 0; j < 26; j++) 
			{
				d += abs(letterFreq2[j] - letterFreq1[j]);
			}
			printf("%d\n",d>>1);
		}
	}	
	return 0;
}