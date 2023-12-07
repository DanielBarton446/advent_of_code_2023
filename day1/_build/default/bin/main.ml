let file = "data/input.txt"

let _concat_doot = 
  String.concat ""
;;

let _custom_print line = 
  print_endline (_concat_doot [line])
;;


(* let read_line file = *)
(*   let in_ch = open_in file in *)
(*   input_line in_ch *)

(* let read_lines file process = *)
(*   let in_ch = open_in file in *)
(*   try *)
(*     while true do *)
(*       let line = input_line in_ch in *)
(*         process line *)
(*     done *)
(*   with *)
(*   | End_of_file -> close_in in_ch *)
(* ;; *)

(* let _impossible = *)
(*   print_endline "ERROR: impossible situation happened you goofed"; *)
(*   exit 1 *)
(* ;; *)

let is_digit = function '0' .. '9' -> true | _ -> false

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

let parse_digit dig = 
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
  match input_line file with  
  | line -> 
      print_endline line;
      print_endline (string_of_int (parse_digit (get_first line) * 100 + parse_digit (get_last line)));

      let num = (parse_digit (get_first line) * 10 + parse_digit (get_last line)) in 
      solve file (sum + num)

  (* End of file, return result *)
  | exception End_of_file -> sum
;;



print_endline (string_of_int (solve(open_in file) 0))


(* read_lines file print_endline;; *)
(* read_lines file custom_print;; *)
(* read_lines file get_first;; *)
(* read_lines file get_last;; *)
(* read_lines file get_last;; *)
(* print_endline "---------------------";; *)
(* print_endline "Resuming control flow";; *)
(* print_endline "---------------------";; *)
