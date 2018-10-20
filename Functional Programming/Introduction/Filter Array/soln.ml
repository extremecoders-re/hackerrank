let x = read_int () in
while true do
    let y = read_int_opt() in
    match y with
        | None -> exit 0
        | Some (y) ->
            if y < x then 
                let _ = print_int y in 
                print_newline ()
done
;
