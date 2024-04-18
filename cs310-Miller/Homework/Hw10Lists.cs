using System;

namespace HW9Interface
{
    public class HW9Interface
    { 
        
        static void FillList(ref List<int> theList, int numofnum)
        {
            Random rand = new Random();
            for (int i = 0; i < numofnum; i++)
            { 
                theList.Add(rand.Next(1000));
            }
        }

        static void InserttoList(ref List<int> theList, int num)
        {
            int index = theList.BinarySearch(num);
            if (index < 0)
            {
                theList.Insert(~index, num);
            }
            else
                theList.Insert(index,num);
        }
        static void PrintList<T>(List<T> List1)
        {
            foreach (var i in List1)
            {
                Console.Write($"{i} ");
            }
        }
        
        static void Main(string[] args)
        {
            List<int> myNums = new List<int>();
            FillList(ref myNums, 10);
            myNums.Sort();
            PrintList(myNums);
            Console.WriteLine();
            InserttoList(ref myNums, 656);
            PrintList(myNums);
            Console.WriteLine();
            
            List<string> myStrs = new List<string>();
            myStrs.Add("Hi there,");
            myStrs.Add("how is your");
            myStrs.Add("day going?");
            PrintList(myStrs);


        }
    }
}