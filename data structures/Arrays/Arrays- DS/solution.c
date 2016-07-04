#include <stdio.h>


int main(){
    int N; 
    scanf("%d",&N);
    int *arr = malloc(sizeof(int) * N);
    for(int arr_i = 0; arr_i < N; arr_i++){
       scanf("%d",&arr[arr_i]);
    }
    
    for(int arr_i = N-1; arr_i >= 0; arr_i--){
       printf("%d ",arr[arr_i]);
    }
    
    return 0;
}
