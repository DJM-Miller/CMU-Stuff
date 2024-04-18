using System;

namespace PointCalculator
{
    public class CartesianPoint
    {
        private int x;
        private int y;

        public CartesianPoint(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
        private int X
        {
            get { return this.x; }
            set { this.x = value; }
        }
        private int Y
        {
            get { return this.y; }
            set { this.y = value; }
        }

        public static CartesianPoint operator +(CartesianPoint left, CartesianPoint right)
        {
            int newX, newY;
            newX = left.X + right.X;
            newY = left.Y + right.Y;
            CartesianPoint newPoint = new CartesianPoint(newX, newY);
            return newPoint;
        }
        
        public static CartesianPoint operator *(CartesianPoint left, CartesianPoint right)
        {
            int newX, newY;
            newX = left.X * right.X;
            newY = left.Y * right.Y;
            CartesianPoint newPoint = new CartesianPoint(newX, newY);
            return newPoint;
        }
        
        public static CartesianPoint operator *(CartesianPoint left, int scale)
        {
            int newX, newY;
            newX = left.X * scale;
            newY = left.Y * scale;
            CartesianPoint newPoint = new CartesianPoint(newX, newY);
            return newPoint;
        }

        public static bool operator ==(CartesianPoint left, CartesianPoint right)
        {
            if (left.X == right.X && left.Y == right.Y)
            {
                return true;
            }

            return false;
        }

        public static bool operator !=(CartesianPoint left, CartesianPoint right)
        {
            return !(left == right);
        }
        public override string ToString()
        {
            return $"({this.X},{this.Y})";
        }
    }
    public class PointCalculator
    {
        static void Main(string[] args)
        {
            //Creating points
            CartesianPoint p1 = new CartesianPoint(1, 2);
            CartesianPoint p2 = new CartesianPoint(2, 1);
            CartesianPoint p3 = p1 + p2;//addition
            CartesianPoint p4 = p1 * p2;//multiply two points
            CartesianPoint p5 = p1 * 3;//multiply point and scale
            CartesianPoint p6 = new CartesianPoint(1, 2);//Just used for positive equality to P1
            
            //Output
            //Removed p1.ToString() etc., warning said it was redundant assume it calls
            //ToString() automatically
            Console.WriteLine($"Point 1: {p1}");
            Console.WriteLine($"Point 2: {p2}");
            Console.WriteLine($"Point 3 = P1 + P2: {p3}");
            Console.WriteLine($"Point 4 = P1 * P2: {p4}");
            Console.WriteLine($"Point 5 = P1 * scale of 3: {p5}");
            
            //Checks for equality
            if(p1 == p6)
                Console.WriteLine($"Point1:{p1} is equal to Point6:{p6}");
            else
                Console.WriteLine($"Point1: {p1} is not equal to Point6:{p6}");
            if(p1 != p2)
                Console.WriteLine($"Point1: {p1} is not equal to Point2:{p2}");
            else
                Console.WriteLine($"Point1: {p1} is equal to Point2:{p2}");
            
        }
    }
}
