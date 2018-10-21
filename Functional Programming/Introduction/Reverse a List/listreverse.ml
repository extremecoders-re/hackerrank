(*Read all lines till EOF*)
let lines_list = ref []
;;

try
    while true do
        let line = read_line () in
        (* New line is added at the begining*)
        lines_list := line :: !lines_list
    done
with End_of_file -> ()
;;

(*Print contents of list*)
let rec print_list li = 
match li with
    | [] -> ()
    | hd :: tl -> 
            let () = print_string (hd ^ "\n") in 
            print_list tl            
;;

print_list !lines_list        
