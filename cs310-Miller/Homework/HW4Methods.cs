using System;


namespace HW4
{
    public class HW4
    {
        static void SayHello(string stuff)
        {
            Console.WriteLine($"Hello {stuff}");
        }
        static string ToPrint()
        {
            return "Well Hello!";
        }
        static void SwapInts(ref int a, ref int b)
        {
            int temp = a;
            a = b;
            b = temp;
        } 
        static int Fib(int n)
        {
            if (n <= 1)
                return n;
            else
            {
                return (Fib(n - 2) + Fib(n - 1));
            }
        }
        static bool isPrime(int n)
        {
            if (n > 3)
            {
                for (int i = 2; i < (n + 1 / 2); i++)
                {
                    if (n % i == 0)
                        return false;
                }
            }

            return true;
        }

        //MAIN *****
        static void Main(string[] args)
        {
            
            //Void output text parameter
            Console.Write("\nEnter your name: ");
            string name = Console.ReadLine()!;
            SayHello(name);
            
            //Return to be printed
            Console.WriteLine(ToPrint());
            
            //Swap by Reference
            int x = 1;
            int y = 2;
            Console.WriteLine($"x = {x} : y = {y}");
            SwapInts(ref x,ref y);
            Console.WriteLine($"x = {x} : y = {y}");
            
            //Find Fibonacci number
            Console.Write("Enter nth Fibonacci number desired: ");
            int n = int.Parse(Console.ReadLine()!);
            if (n >= 0)
                Console.WriteLine($"The {n} Fibonacci number is {Fib(n)}");
            
            //Check Prime
            Console.Write("Enter positive number to check if Prime: ");
            n = int.Parse(Console.ReadLine()!);
            if (n > 0)
            {
                if(isPrime(n))
                    Console.WriteLine($"{n} is a Prime number");
                else
                    Console.WriteLine($"{n} is not a Prime number");
            }
        }
     }
}
        
