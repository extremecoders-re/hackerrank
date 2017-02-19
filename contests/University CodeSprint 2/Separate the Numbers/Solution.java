import java.util.*;

public class Solution 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        boolean isBeautiful = false;
        int q = sc.nextInt();
        
        for(int i = 0; i < q; i++, isBeautiful = false)
        {
            String s = sc.next();
            
            for (int nod_seqstart = 1; nod_seqstart <= s.length() / 2; nod_seqstart++)
            {
                long start, seq;
                int pos;
                start = seq = Long.parseLong(s.substring(0, nod_seqstart));
                for (pos = nod_seqstart; pos < s.length();)                
                {
                    seq++;
                    String str_seq = String.valueOf(seq);
                    if (!s.regionMatches(pos, str_seq, 0, str_seq.length()))
                    {
                        break;
                    }
                    
                    pos += str_seq.length();
                }
                if (pos == s.length())
                {
                    System.out.println("YES " + start);
                    isBeautiful = true;
                    break;
                }
            }
            if (!isBeautiful) System.out.println("NO");
        }
    }
}
