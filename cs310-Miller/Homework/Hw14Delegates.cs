using System;

namespace HW14Delegates
{
    public class HW14Delegates
    {
        static void CircleArea(double radius)
        {
            Console.WriteLine($"Area: {(Math.PI*radius*radius).ToString("0.00")}");
        }

        static void CircleCircum(double radius)
        {
            Console.WriteLine($"Circumference: {(Math.PI * radius * 2).ToString("0.00")}");
        }

        public delegate void MultiDelegate(double radius);

        static double CArea(double radius)
        {
            return radius * radius * Math.PI;
        }

        static bool CheckRadius(double radius)
        {
            return radius > 1.0;
        }
        
        static void Main(string[] args)
        {
            //Multicast delegate
            MultiDelegate myCircleInfo = CircleArea;
            myCircleInfo += CircleCircum;
            myCircleInfo(4.0);
            
            //Func
            Func<double, double> area = CArea;
            Console.WriteLine($"Area: {area(1.0).ToString("0.00")}");
            
            //Action
            Action<double> area1 = CircleArea;
            area1(2.0);
            
            //Predicate
            Predicate<double> greaterThan1 = CheckRadius;
            if (greaterThan1(1.2))
            {
                Console.WriteLine("Radius is greater than 1");
            }
        }
    }
}