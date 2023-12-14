let process_line _line = 
  -69420
;;

let is_digit = function 
  '0' .. '9' -> true 
  |        _ -> false

let contains_substring str substr = 
  failwith "NOT IMPLEMENTED YET"

let parse_digit_from_char dig = 
  match dig with
  | '0' -> 0
  | '1' -> 1
  | '2' -> 2
  | '3' -> 3
  | '4' -> 4
  | '5' -> 5
  | '6' -> 6
  | '7' -> 7
  | '8' -> 8
  | '9' -> 9
  | _ -> failwith "Not a digit"
;;


let get_first _line = 
  let rec helper idx acc = 
    failwith "NOT IMPLEMENTED YET"
  in
  helper 0 ""


let rec solve file sum = 
  (* input line is responsible for getting the line, hence no functions needed *)
  match input_line file with  
  | line -> 
      let num = process_line line in
      (* print_int num; *)
      (* print_newline (); *)
      solve file (sum + num)

  (* End of file, return result *)
  | exception End_of_file -> sum
;;
