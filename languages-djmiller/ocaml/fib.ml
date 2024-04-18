let rec fib n =
    if n <= 0 then 0
    else if n = 1 then 1
    else fib (n-1) + fib (n-2);;



print_string("Fibonacci of x is : ");
print_int(fib 10);
print_newline ();