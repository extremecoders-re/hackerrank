(* Enter your code here. Read input from STDIN. Print output to STDOUT *)

Program utopianTree;

{$mode objfpc}  //Required for Result identifier

function calcHeight(n: integer): integer;
var
    height, i: integer;
begin
    height := 1;
    i := 1;
    while i <= n do
    begin
        if (i mod 2) = 0 then
            Inc(height)
        else
            height := height * 2;
        Inc(i);
    end;
    Result := height;
end;

var
    T, N, i: integer;
begin
    Readln(T);
    for i := 1 to T do
    begin
        Readln(N);
        WriteLn(calcHeight(N));
    end;
end.