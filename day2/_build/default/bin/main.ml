let process_line _line = 
  -69
;;

let rec solve file sum = 
  (* input line is responsible for getting the line, hence no functions needed *)
  match input_line file with  
  | line -> 
      let num = (process_line line) in 
      solve file (sum + num)

  (* End of file, return result *)
  | exception End_of_file -> sum
;;
