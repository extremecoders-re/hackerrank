#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PARTITION 0.35
#define RATIO 2.0f

int main()
{
	unsigned int i, blue, green, red, grey, leftHalfSum, rightHalfSum, histogram[256];
		
	memset(histogram, 0, 256*sizeof(int));
	
	while (feof(stdin) == 0)
	{
		
		scanf("%u,%u,%u", &blue, &green, &red);
		grey = (blue + green + red) / 3;
		if (grey > 255) printf("Grey value more than 255!!");
		else histogram[grey]++;
	}
	
	leftHalfSum = rightHalfSum = 0;
	for (i = 0; i < 256 * PARTITION; i++) leftHalfSum += histogram[i];
	for (i = 256 * PARTITION; i < 256; i++) rightHalfSum += histogram[i];
	
	if((float)leftHalfSum/rightHalfSum > RATIO) printf("night\n");
	else printf("day\n");
	return 0;
}