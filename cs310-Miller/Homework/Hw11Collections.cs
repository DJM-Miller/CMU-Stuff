using System;

namespace HW11Collections
{
    public class HW11Collections
    {
        static void Main(string[] args)
        {
            //Dictionary
            Dictionary<string, int> myDict = new Dictionary<string, int>();
            myDict.Add("Beatles", 1);
            myDict.Add("Pink Floyd", 2);
            myDict.Add("Led Zeppelin", 3);
            PrintDict(myDict);
            Console.WriteLine();
            //Stack
            Stack<Double> myDubs = new Stack<double>();
            myDubs.Push(2.01);
            myDubs.Push(1.02);
            myDubs.Push(5.03);
            PrintStack(myDubs);
            Console.WriteLine($"\nStack total is {StackTotal(myDubs)}");
            //Queue
            Queue<int> myInts = new Queue<int>();
            for(int i = 0; i<5;i++)
                myInts.Enqueue(i);
            PrintQueue(myInts);
            Console.WriteLine();
        }


        static Double StackTotal(Stack<Double> stack1)
        {
            Double total = 0.0;
            foreach (var i in stack1)
            {
                total += i;
            }

            return total;
        }
        static void PrintQueue<T>(Queue<T> queue1) where T: notnull
        {
            foreach (var i in queue1)
            {
                Console.Write($"{i.ToString()} ,");   
            }
        }
        static void PrintStack<T>(Stack<T> stack1) where T: notnull
        {
            foreach (var i in stack1)
            {
                Console.Write($"{i.ToString()} ,");   
            }
        }
        static void PrintDict<T, T2>(Dictionary<T, T2> dict1) where T: notnull
        {                                                //"where T : notnull removed a warning
            foreach (var i in dict1)
            {
                Console.Write($"{i.Value} : {i.Key} ,");
            }
           
        }
    }
}
