using System;

namespace HW15Linq
{
    public class HW15Linq
    {
        static void Main(string[] args)
        {
            //Fills list with random numbers
            List<int> randomNums = new List<int>();
            Random rand = new Random(10);
            for (int i = 0; i < 20; i++)
            {
                randomNums.Add(rand.Next(1,100));
            }
            Console.Write("Random List: ");
            foreach (var i in randomNums)
            {
                Console.Write($"{i} ");
            }
            Console.WriteLine();
            
            //Lambda for odd numbers
            Console.Write("ODD Numbers: ");
            List<int> oddNums = randomNums.FindAll(x => (x % 2) != 0);
            foreach (var i in oddNums)
            {
                Console.Write($"{i} ");
            }
            Console.WriteLine();
            
            //Lambda for multiples of 5
            Console.Write("Multiples of 5: ");
            List<int> NumsTimes5 = randomNums.FindAll(x => (x %5 ) == 0);
            foreach (var i in NumsTimes5)
            {
                Console.Write($"{i} ");
            }
            Console.WriteLine();
            
            //Creates 2 groups of even numbers: Greater than 50,  <= 50
            List<int> EvenNums = randomNums.FindAll(x => (x % 2) == 0);
            var GroupEvenNums = from number in EvenNums group number by number <= 50;
            
            foreach (var group in GroupEvenNums)
            {
                if(group.Key)
                    Console.Write("Even numbers less than or equal to 50: ");
                else
                    Console.Write("Even numbers Greater than 50: ");
                
                foreach (var i in group)
                {
                    Console.Write($"{i} ");
                }
                Console.WriteLine();
            }
            //LINQ for Names that end in letter e
            List<string> names = new List<string>() { "Bob", "Luke", "Kyle", "Haily", "Sophie", "Aspen" };
            IEnumerable<string> subsetNames = from name in names
                                            where name[name.Length - 1] == 'e'
                                            select name;
            Console.Write("Names that end in e: ");
            foreach (var name in subsetNames)
            {
                Console.Write($"{name} ");
            }

        }
    }
}