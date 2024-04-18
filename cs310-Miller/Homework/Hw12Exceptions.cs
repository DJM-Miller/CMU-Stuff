using System;

namespace HW12Exceptions
{
    public class HW12Exceptions
    {
        public class MyException : Exception
        {
            public MyException(string message) : base(message)
            {
                    
            }
        }
        
        static void Main(string[] args)
        {
            try
            {
                MyException e = new MyException("My custom exception");
                throw e;
            }
            catch (MyException e)
            {
                Console.WriteLine(e);
            }
        }
    }
}
