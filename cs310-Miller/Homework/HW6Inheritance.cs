using System;

namespace HW6Inheritance
{
    public class People
    {
        public string Name { get; set; } = default!;
    }

    public class Employ : People
    {
        public Employ(string name, double wage, int hours)
        {
            this.Name = name;
            this.Wage = wage;
            this.Hours = hours;
        }
        public double Wage { get; set; }
        public int Hours { get; set; }

        public double Pay()
        {
            return this.Wage * this.Hours;
        }
    }

    public class Student : People
    {
        public Student(string name, string course)
        {
            this.Name = name;
            this.Course = course;
        } 
        public string Course { get; set; }

        public void Output()
        {
            Console.WriteLine($"{Name} is taking a course in {Course}.");
        }
    }
    
    public class HW6Inheritance
    {
        static void Main(string[] args)
        {
            Employ emp1 = new Employ("Bob", 15.5, 40);
            Console.WriteLine($"\n{emp1.Name}'s pay is {emp1.Pay().ToString("0.00")}");
            Console.Write($"What would you like to change {emp1.Name}'s name to: ");
            string newName = Console.ReadLine()!;
            emp1.Name = newName;
            Console.WriteLine($"{emp1.Name}'s pay is {emp1.Pay().ToString("0.00")}");

            Student stu1 = new Student("Billy", "Economics");
            stu1.Output();
            stu1.Course = "Physics";
            stu1.Output();

        }
    }
}
