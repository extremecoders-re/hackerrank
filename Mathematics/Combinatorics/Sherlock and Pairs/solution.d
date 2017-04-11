import std.stdio;
import std.array: split;
import std.algorithm.iteration: map, reduce;
import std.conv: to;


void main()
{
    int T;
    string line;

    readf("%d ", &T);
    foreach(_; 0 .. T)
    {
        readln(); // skip N
        line = readln();
        
        // Convert numbers to integer
        auto numbers = map!(to!long)(line.split());
        
        // Associative array(dict) to store frequencies
        long[long] freq;
        
        // Calculate the frequency of each number
        foreach(n; numbers)
        {
          if (!(n in freq)) freq[n] = 1;
          else freq[n]++;
        }        
        writeln(reduce!((x,y) => x + y*(y-1))(long(0), freq));		
    }
}
