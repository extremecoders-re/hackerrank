import java.util.HashMap;
import java.util.Scanner;
import java.util.Set;

public class Solution
{
    HashMap<Integer, Integer> arrayA;
    HashMap<Integer, Integer> arrayB;

    public Solution()
    {
        arrayA = new HashMap<Integer, Integer>(40);
        arrayB = new HashMap<Integer, Integer>(40);
    }

    public static void main(String[] args)
    {
        Solution obj = new Solution();
        obj.doIt();
    }

    private void doIt()
    {
        int T, N, K;
        Scanner sc = new Scanner(System.in);

        T = sc.nextInt();
        for (int i = 0; i < T; i++)
        {
            N = sc.nextInt();
            K = sc.nextInt();

            // Input Array A
            for (int j = 0; j < N; j++)
            {
                int temp = sc.nextInt();
                if(arrayA.containsKey(temp))
                    arrayA.put(temp, arrayA.get(temp) + 1);
                else arrayA.put(temp, 1);
            }

            // Input Array B
            for (int j = 0; j < N; j++)
            {
                int temp = sc.nextInt();
                if(arrayB.containsKey(temp))
                    arrayB.put(temp, arrayB.get(temp) + 1);
                else arrayB.put(temp, 1);
            }

            if (process(K))
                System.out.println("YES");
            else
                System.out.println("NO");

            arrayA.clear();
            arrayB.clear();
        }
    }

    private boolean process(int K)
    {
        //Get the keys of the first array
        Set<Integer> keysetA = arrayA.keySet();
        Set<Integer> keysetB = arrayB.keySet();

        //for each key in first array
        for (int x : keysetA)
        {
            int freq = arrayA.get(x);

            //The minimum value of the second number
            int minValue = K - x;
            if (minValue < 0) return false; //Negative values not possible

            //We need to check if the number of elements in arrayB
            //greater than or equal to minValue is at least freq
            int numValues = 0;
            for(int y: keysetB)
            {
                if (y >= minValue) numValues += arrayB.get(y);
                if (numValues >= freq) break;   //No need to proceed
            }

            if (numValues < freq) return false;
        }
        return true;
    }
}