#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//---------------------------------------------------
void removeDuplicates(char str[])
{
	int i, j, len, p;
	len = strlen(str);
	
	char *no_dupli = (char*)malloc(len + 1);
	memset(no_dupli, 0, len + 1);
	
	for (i = 0, p = -1; i < len; i++)
	{
		if (str[i] != 0) 
		{
			no_dupli[++p] = str[i];
			for (j = 0; j < len; j++)
			{
				if (str[j] == no_dupli[p]) str[j] = 0;			
			}
		}		
	}
	memset(str, 0, len);
	memcpy(str, no_dupli, len);
	free(no_dupli);
}

//---------------------------------------------------
void buildTable(char str[], char table[])
{
	int p;
	char ch;
	strcpy(table, str);
	for (p = strlen(str), ch = 'A'; ch <= 'Z'; ch++)
		if (strchr(str, ch) == 0) table[p++] = ch;
}

//---------------------------------------------------
void sortTable(char str[], char table[], int width)
{
	char s_table[27];
	char ch;
	int j, pos, p;
	
	memset(s_table, 0, sizeof(s_table));
	
	for(p = 0, ch = 'A'; ch <= 'Z'; ch++)
	{
		pos = (int)(strchr(str, ch) - str);
		if (pos >= 0)
		{
			for(j = pos; j < 26; j += width)
				s_table[p++] = table[j];
		}
	}
	
	strcpy(table, s_table);		
}

//---------------------------------------------------
char decryptChar(char ch, char table[])
{
	return 'A' + (int)(strchr(table, ch) - table);
}

//---------------------------------------------------
int main() 
{
	int i, j, N;
	char keyword[8], ciphertext[256], table[27];

	
	scanf("%d", &N);
	getchar();
	for(i = 0; i < N; i++)
	{
		memset(keyword, 0, sizeof(keyword));
		memset(ciphertext, 0, sizeof(ciphertext));
		memset(table, 0, sizeof(table));
		
		// Forget possible buffer overflow
		gets(keyword);
		gets(ciphertext);
		
		removeDuplicates(keyword);
		buildTable(keyword, table);
		sortTable(keyword, table, strlen(keyword));
		
		for(j = 0; j < strlen(ciphertext); j++)
		{
			if (ciphertext[j] == ' ')
			{
				printf(" ");
				continue;
			}
			printf("%c", decryptChar(ciphertext[j], table));
		}
		printf("\n");
	}
	return 0;
}