import std.stdio;
import std.math: abs;

void main()
{
    string s1, s2;
    s1 = readln();
    s2 = readln();
    
    int[26] freq_s1;
    int[26] freq_s2;
    
    foreach(ch; s1) freq_s1[ch-'a']++;
    foreach(ch; s2) freq_s2[ch-'a']++;
    
    int answer = 0;
    foreach(i; 0 .. freq_s1.length) answer += abs(freq_s1[i] - freq_s2[i]);
    writeln(answer);                       
}
