import java.util.*;

public class Solution 
{
    public static void main(String[] args) 
    {
        int n, highscore, lowscore, rec_highscore, rec_lowscore;
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        int[] score = new int[n];
        for(int i=0; i < n; i++) score[i] = in.nextInt();
        
        highscore = lowscore = score[0];
        rec_highscore = rec_lowscore = 0;
        
        for (int i = 0; i < n; i++)
        {
            if (score[i] > highscore)
            {
                rec_highscore++;
                highscore = score[i];                
            }
            else if (score[i] < lowscore)
            {
                rec_lowscore++;
                lowscore = score[i];                                
            }
        }
        System.out.println(rec_highscore + " " + rec_lowscore);
    }
}
