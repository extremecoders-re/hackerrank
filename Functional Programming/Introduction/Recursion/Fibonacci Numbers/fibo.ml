let rec fibonacci n =
    match n with 
    | 0 -> 0
    | 1 -> 1
    | x -> fibonacci (x-1) + fibonacci (x-2)
    
let () =
    let n = read_int () in
    print_int (fibonacci (n-1))
