using System;

namespace HW1
{
    public class HW1
    {
        static void Main(string[] args)
        { 
            //Declaring, outputting, and changing Variables
            int inum = 10;
            double dnum = 15.1;
            char character = 'C';
            string astring = "C#";
            
            //Output
            Console.WriteLine("************************");
            Console.WriteLine("Initial values:");
            Console.WriteLine($"int: {inum}");
            Console.WriteLine($"double: {dnum}");
            Console.WriteLine($"char: {character}");
            Console.WriteLine($"string: {astring}");
            
            //Changing Variables
            inum = 20;
            dnum = 11.5;
            character = 'A';
            astring = "Lets learn some C#";
            
            //Output
            Console.WriteLine("************************");
            Console.WriteLine("Values after change:");
            Console.WriteLine($"int: {inum}");
            Console.WriteLine($"double: {dnum}");
            Console.WriteLine($"char: {character}");
            Console.WriteLine($"string: {astring}");

            
            //Calculate area of triangle with Herons Formula
            double a, b, c, s, area;
            a = 3;
            b = 4;
            c = 5;
            s = (a + b + c) / 2;
            area = Math.Sqrt(s * (s - a) * (s - b) * (s - c));
            Console.WriteLine("************************");
            Console.WriteLine($"Triangle side lengths: {a}, {b}, {c}");
            Console.WriteLine($"The area of the triangle is: {area}");
            Console.WriteLine("************************");

        }
    }
}
