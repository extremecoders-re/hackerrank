open Printf

let rec do_it t = 
        match read_int_opt() with
        | None -> exit 0
        | Some (x) -> 
                    if t mod 2 = 1 then 
                        let () = printf "%d\n" x in
                        do_it (t+1)
                    else
                        do_it (t+1)
;;
do_it 0
