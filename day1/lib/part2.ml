let is_digit = function 
  '0' .. '9' -> true 
  |        _ -> false
;;

let translate = function
  | "one"   -> 1
  | "two"   -> 2
  | "three" -> 3
  | "four"  -> 4
  | "five"  -> 5
  | "six"   -> 6
  | "seven" -> 7
  | "eight" -> 8
  | "nine"  -> 9
  | _ -> -1
;;

let is_in_letters = function
  | 'o' -> true 
  | 'n' -> true
  | 'e' -> true
  | 't' -> true
  | 'w' -> true
  | 'h' -> true
  | 'r' -> true
  | 'f' -> true
  | 'u' -> true
  | 'i' -> true
  | 'v' -> true
  | 's' -> true
  | 'x' -> true
  | 'g' -> true
  | _   -> false
;;

(* READ ME *)
(* need to make it so get first either parses first 
   word number or the first digit number of the string *)
let get_first line =
  print_endline "--------";
  print_endline line;
  print_endline "--------";
  let rec substring idx acc = 
    (* print_endline (string_of_int (String.length line)); *)
    (* print_endline (string_of_int (idx)); *)
    print_endline "current idx:";
    print_endline (string_of_int idx);
    print_endline ( String.make 1 line.[idx] );
    if idx >= (String.length line ) - 1 then
      failwith "Couldn't parse number"
    else
      let str = acc ^ (String.make 1 line.[idx]) in
        if translate str <> -1 then
          begin
            print_endline "found a number:";
            print_endline str;
            translate str
          end
        else
          if is_digit line.[idx] || not (is_in_letters line.[idx]) then
            (* reset accum *)
            substring (idx + 1) ""
          else
            (* sadly, we have to make the char a string and concatenate two strings *)
            substring (idx + 1) (acc ^ (String.make 1 line.[idx]))
  in
  substring 0 ""
;;
    

let process_line _line = 
  (* -69420; *)
  get_first _line
;;

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
