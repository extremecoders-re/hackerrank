import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    
static int findDigits(int num)
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

    public static void main(String[] args) 
    {
        int T, num;
        Scanner sc = new Scanner(System.in);    
        T = sc.nextInt();    
        for(int i=0; i<T; i++)
        {
            num = sc.nextInt();
            System.out.println(findDigits(num));        
        }
    }
}