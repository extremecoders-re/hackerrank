let lines_list = ref []
;;

try
    while true do
        let line = read_line () in
        lines_list := line :: !lines_list
    done
with End_of_file -> ()
;;

let rec list_length = function
    | [] -> 0
    | hd :: tl -> 1 + list_length tl
;;

print_int (list_length !lines_list)       
