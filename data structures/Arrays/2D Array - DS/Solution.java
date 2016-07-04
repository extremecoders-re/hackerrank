import java.util.*;

public class Solution {

    public static void main(String[] args) 
    {
        Scanner in = new Scanner(System.in);
        int arr[][] = new int[6][6];
        
        for(int arr_i=0; arr_i < 6; arr_i++)
            for(int arr_j=0; arr_j < 6; arr_j++)
                arr[arr_i][arr_j] = in.nextInt();
        
        int max, temp;
        max = arr[0][0] + arr[0][1] + arr[0][2] + arr[1][1] + arr[2][0] + arr[2][1] + arr[2][2];
        for (int r=0; r <= 6-3; r++)
        {
            for (int c=0; c <= 6-3; c++)
            {
                temp = arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1] + arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2];
                if (temp > max) max = temp;
            }
                
        }
        System.out.println(max);
    }
}
