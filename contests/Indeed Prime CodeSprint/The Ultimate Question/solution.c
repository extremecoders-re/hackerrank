#include <stdio.h>

int main(){
    int a; 
    int b; 
    int c; 
    scanf("%d %d %d",&a,&b,&c);
    if (a + b + c == 42)  
        printf("%d+%d+%d",a,b,c);
    else if(a + b * c == 42)
        printf("%d+%d*%d",a,b,c);
    else if(a * b + c == 42)
        printf("%d*%d+%d",a,b,c);
    else if(a * b * c == 42)
        printf("%d*%d*%d",a,b,c);
    else
        printf("This is not the ultimate question");
    return 0;
}