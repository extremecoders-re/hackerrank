#include <stdio.h>

int main()
{
	int n, i, j, k, row, col, val, move;
	scanf("%d", &n);
	for (j = 0; j < n; j++)
	{
		scanf("%d", &i);
		int arr[i][i];
		row = -1;
		col = 0;
		val = 0;
		move = i;
		
		while (move>0)
		{
			//Down
			for (k=0; k<move; k++) arr[++row][col] = ++val;
			move--;
			
			//Right
			for (k=0; k<move; k++) arr[row][++col] = ++val;
				
			//Up
			for (k=0; k<move; k++) arr[--row][col] = ++val;
			move--;				
		
			//Left
			for (k=0; k<move; k++) arr[row][--col] = ++val;			
		}
		for(row = 0; row<i; row++)
		{
			for(col = 0; col<i; col++) printf("%d ",arr[row][col]);		
			printf("\n\n");			
		}

	}
	return 0;
}