using System;

namespace HW5
{
    //Class could be used for the type and number
    //of animals in a zoo pen or whatever
    public class AnimalPen
    {
        private string Type;
        private int Number;
        
        //Constructor
        public AnimalPen(string Type, int Number)
        {
            this.Type = Type;
            this.Number = Number;
        }
        public string GetType()
        {
            return Type;
        }
        public void SetType(string newType)
        {
            this.Type = newType;
        }
        public int GetNum()
        {
            return Number;
        }
        public void SetNum(int newNumber)
        {
            this.Number = newNumber;
        }
        //Increase or decrease number by 1
        public void AddAnother()
        {
            this.Number++;
        }
        public void SubtractOne()
        {
            this.Number--;
        }



    }
    public class HW5
    {
        static void Main(string[] args)
        {
            AnimalPen Pen1 = new AnimalPen("Dogs", 6);
            AnimalPen Pen2 = new AnimalPen("Alpaca", 4);
            
            Console.WriteLine($"\nPen 1 has {Pen1.GetNum()} {Pen1.GetType()} in it");
            Console.WriteLine($"Pen 2 has {Pen2.GetNum()} {Pen2.GetType()} in it");
            
            Pen1.AddAnother();
            Pen2.SubtractOne();
            Console.WriteLine($"\nPen 1 now has {Pen1.GetNum()} {Pen1.GetType()} in it");
            Console.WriteLine($"Pen 2 now has {Pen2.GetNum()} {Pen2.GetType()} in it");
            
        }
    }
}