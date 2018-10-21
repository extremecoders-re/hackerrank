let rec f arr =
    match arr with
        | [] -> []
        | hd :: tl -> (if hd > 0 then hd else -hd) :: f tl


let rec read_lines () = 
    try let line = read_line () in
        line :: read_lines()
    with
        End_of_file -> []
            
let () =
    let inp = read_lines () in
    let arr = List.map int_of_string inp in
    let result = f arr in
    let output = List.map string_of_int result in
    print_string (String.concat "\n" output) ;;
