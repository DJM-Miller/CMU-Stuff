using System;

namespace HW16Async
{
    public class HW16Async
    {
        static Task EvenNums(List<int> aList)
        {
            return Task.Run(() =>
            {
                List<int> evens = aList.FindAll(x => (x % 2) == 0);
                foreach (var i in evens)
                {
                    Console.WriteLine($"Next even number: {i}");
                    Task.Delay(100).Wait();
                }
            });
            
        } 
        
        static Task ListTotal(List<int> aList)
        {
            return Task.Run(() =>
            {
                int total = 0;
                foreach (var i in aList)
                {
                    total += i;
                    Console.WriteLine($"Running Total: {total}");
                    Task.Delay(50).Wait();
                }

                Console.WriteLine($"List Total: {total}");
            });
        }

        static async Task Main(string[] args)
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

            Task printEvens = EvenNums(randomNums);
            Task calcTotal = ListTotal(randomNums);

            await calcTotal;
            await printEvens;
            




        }
    }
}