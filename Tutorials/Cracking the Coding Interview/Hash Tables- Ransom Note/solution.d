import std.stdio;
import std.array;

void main(string[] args)
{
    int m, n;

    // Not required for any purpose
    readf("%d %d\n", &m, &n);

    string[] mag_words = split(readln());
    string[] ran_words = split(readln());

    // Associative arrays to store word frequencies
    int[string] mag_word_freq;
    int[string] ran_word_freq;

    // Calculate the word frequencies
    foreach (word; mag_words)
    {
        if (!(word in mag_word_freq)) mag_word_freq[word] = 0;
        else mag_word_freq[word]++;
    }

    foreach (word; ran_words)
    {
        if (!(word in ran_word_freq)) ran_word_freq[word] = 0;
        else ran_word_freq[word]++;
    }

    // frequency of each word in ransom note must be <= corresponding frequency
    // in magazine
    foreach(key; ran_word_freq.byKey())
    {
        if (!(key in mag_word_freq))
        {
            writeln("No");
            return;
        }
        else if(mag_word_freq[key] < ran_word_freq[key])
        {
            writeln("No");
            return;
        }
    }
    writeln("Yes");
}
