(* returns an array of n elements *)
let rec make_array n =
    match n with
    | 0 -> []
    | x -> x :: make_array (x-1)
;;

let () =
    let n = int_of_string (read_line ()) in
    let arr = make_array n in
    List.iter ( Printf.printf "%d " ) arr
