using System;
using System.Collections.Generic;
using System.IO;
class Solution {
/*
 * Complete the function below.
 */
    static int maxXor(int l, int r) {
        int max;
        max = 0;
        for (int a = l; a < r; a++)
            {
            for (int b = a + 1; b <= r; b++ )
                {
                if ((a ^ b) > max) max = a ^ b;
            }
        }
        return max;
    }

    static void Main(String[] args) {
        int res;
        int _l;
        _l = Convert.ToInt32(Console.ReadLine());
        
        int _r;
        _r = Convert.ToInt32(Console.ReadLine());
        
        res = maxXor(_l, _r);
        Console.WriteLine(res);
        
    }
}