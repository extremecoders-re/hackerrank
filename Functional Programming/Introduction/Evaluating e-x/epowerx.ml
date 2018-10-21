open Printf

let rec factorial = function
    | (0|1) -> 1
    | n -> n * factorial (n-1)

let i2f = float_of_int
let term x n = (x ** i2f n) /. (i2f (factorial n))

let rec sum_of_terms x limit =
    match limit with
        | 10 -> 0. (*First 10 terms*)
        | k -> (term x k) +. sum_of_terms x (limit+1)
    
let () = 
    for i = 1 to read_int () do
        let x = read_float () in
        printf "%.4f\n" (sum_of_terms x 0)
    done    
