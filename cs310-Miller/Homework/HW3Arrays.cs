using System;

namespace HW2
{
    public class HW2
    {
        static void Main(string[] args)
        {
            //Populate Array
            var rand = new Random();
            int[] set1 = new int[10];
            for (int i = 0; i < 10; i++)
            {
                set1[i] = rand.Next(100);;
            }
            
            //Print unsorted array
            Console.WriteLine("Unsorted Array:");
            foreach (var x in set1)
            {
                Console.Write($"{x}, ");
            }
            Console.Write("\n");
            
            //Sort array
            int temp;
            for (int i = 0; i < 9; i++)
            {
                for (int j = i+1; j < 10; j++)
                {
                    if (set1[j] < set1[i])
                    {
                        temp = set1[j];
                        set1[j] = set1[i];
                        set1[i] = temp;
                    }
                }
            }
            
            //Print sorted array
            Console.WriteLine("Sorted Array:");
            foreach (var x in set1)
            {
                Console.Write($"{x}, ");
            }
            Console.Write("\n");

            int[] tempSet = new int[10];
            for (int i = 0; i < 10; i++)
            {
                tempSet[9 - i] = set1[i];
            }
            set1 = tempSet;
            
            //Print Reversed array
            Console.WriteLine("Reversed Array:");
            foreach (var x in set1)
            {
                Console.Write($"{x}, ");
            }
            Console.Write("\n");
            
            
            
            //3x3 array 
            byte[,] somebytes = { { 3, 2, 1 }, { 6, 5, 4 }, { 9, 8, 7 } };
            
            //Jagged array
            byte[][] jaggedArray = new byte[5][];
            jaggedArray[0] = new byte[] {1,2,3,4,5};
            jaggedArray[1] = new byte[] {5,6};
            jaggedArray[2] = new byte[] {1,2,3};
            jaggedArray[3] = new byte[] {5,6,87,9,2};
            jaggedArray[4] = new byte[] {4,9};
        }
    }
}
