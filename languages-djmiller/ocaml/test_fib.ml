let rec fibonacci n =
  if n <= 0 then 0
  else if n = 1 then 1
  else fibonacci (n - 1) + fibonacci (n - 2)

let run_test input expected =
  let result = fibonacci input in
  if result = expected then
    Printf.printf "Test passed: fibonacci %d = %d\n" input expected
  else
    Printf.printf "Test failed: fibonacci %d expected %d, but got %d\n" input expected result

let run_tests () =
  run_test 0 0;
  run_test 1 1;
  run_test 5 5;
  run_test 10 55

let () =
  run_tests ()
