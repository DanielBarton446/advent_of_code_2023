let file = "data/input.txt"

let is_digit = function 
  '0' .. '9' -> true 
  |        _ -> false

let rec get_first str =
  match String.length str with
  | 0 -> failwith "No digit found in get_first"
  | _ when is_digit str.[0] 
      -> str.[0]
  | _ -> get_first (String.sub str 1 (String.length str - 1))
      
;;

let get_last str =
  let rec helper str i =
    match i with
    | -1 -> failwith "No digit found in get_last"
    | _ when is_digit str.[i] 
        -> str.[i]
    | _ -> helper str (i - 1)
  in
    helper str (String.length str - 1)
;;

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

let rec solve file sum = 
  (* input line is responsible for getting the line, hence no functions needed *)
  match input_line file with  
  | line -> 
      let num = (parse_digit_from_char (get_first line) * 10 + parse_digit_from_char (get_last line)) in 
      solve file (sum + num)

  (* End of file, return result *)
  | exception End_of_file -> sum
;;


print_endline (string_of_int (solve(open_in file) 0))
