using System;

namespace HW2
{
    public class HW2
    {
        static void Main(string[] args)
        {
            //Calculate Taxes
            double income, taxes;
            Console.Write("Enter your income: ");
            income = Single.Parse(Console.ReadLine()!);
          
            Console.WriteLine($"\nIncome before Tax: {income.ToString("0.00")}");
            switch (income)
            {
                case < 10000:
                    taxes = income * .05;
                    break;
                case >=10000 and <=100000:
                    taxes = income * .097;
                    break;
                default:
                    taxes = income * .14;
                    break;
            }
            Console.WriteLine($"Taxes owed: {taxes.ToString("0.00")}");
            income -= taxes;
            Console.WriteLine($"Income after taxes: {income.ToString("0.00")}");
            Console.WriteLine("*******************************");
            
            //Output two triangles and rectangle of size n
            Console.WriteLine("Enter number of lines you would like: ");
            int n;
            n = int.Parse(Console.ReadLine()!);
            Console.WriteLine();
           
            if (n > 0)
            {
                //Print Triangle
                for (int i = 0; i <= n; i++)
                {
                    for (int j = 0; j < i; j++)
                    {
                        Console.Write('*');
                    }
                    Console.Write("\n");
                }
                Console.Write("\n\n");
                
                //Print Inverted Triangle
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j+i < n; j++)
                    {
                        Console.Write('*');
                    }
                    Console.Write("\n");
                }
                Console.Write("\n\n");
               
                //Print Square
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        Console.Write('*');
                    }
                    Console.Write("\n");
                }
            }
        }
    }
}
