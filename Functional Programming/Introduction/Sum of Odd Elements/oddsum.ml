let num_list = ref []
;;

try
    while true do
        let num = read_int () in
        num_list := num :: !num_list
    done
with End_of_file -> ()
;;

let rec sum_odd = function
    | [] -> 0
    | hd :: tl -> 
            (if hd land 1 = 0 then 0 else hd) + sum_odd tl
;;

print_int (sum_odd !num_list)
