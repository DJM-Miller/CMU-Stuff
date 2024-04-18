using System;

namespace HW7Polymorphisim
{
    public class HW4Polymorphisim
    {
        public class Vehicle
        {
            public Vehicle(string make, string model, int miles)
            {
                this.make = make;
                this.model = model;
                this.miles = miles;
            }
            private string make = default!;
            public string Make
            {
                get { return this.make; }
                set { this.make = value; }
            }
            private string model = default!;
            public string Model
            {
                get { return this.model; }
                set { this.model = value; }
            }
            //Miles refers to odometer reading
            private int miles;
            public int Miles
            {
                get { return this.miles; }
                set { this.miles = value; }
            }
            //Assumes average 20mpg for random vehicles
            public virtual double TotalGalofGas()
            {
                return Miles / 20.0;
            }
            //Assumes oil change every 5000miles on the mark
            public virtual int NextOilChange()
            {
                return Miles % 5000;
            }
        }

        public class Car : Vehicle
        {
            public Car(string make, string model, int miles) : base(make, model, miles)
            {
                
            }
            //Assume average mpg of 25.0
            public override double TotalGalofGas()
            {
                return Miles / 25.0;
            }
            //Assume oil change every 3500 miles
            public override int NextOilChange()
            {
                return Miles % 3500;
            }
        }
        public class Truck : Vehicle
        {
            public Truck(string make, string model, int miles) : base(make, model, miles)
            {
                
            }
            //Assume average mpg of 15.0
            public override double TotalGalofGas()
            {
                return Miles / 15.0;
            }
            //Assume oil change every 6000 miles
            public override int NextOilChange()
            {
                return Miles % 6000;
            }
        }
        static void Main(string[] args)
        {
            Car car1 = new Car("Toyota", "Camry", 132005);
            Truck truck1 = new Truck("Ford", "F150", 175652);
            Console.WriteLine($"\nThe {car1.Make} {car1.Model} with {car1.Miles} miles has\n" +
                              $"{car1.NextOilChange()} miles to next oil change and has\n" +
                              $"used about {car1.TotalGalofGas().ToString("0.0")} Gallons of gas Total.");
            Console.WriteLine($"\nThe {truck1.Make} {truck1.Model} with {truck1.Miles} miles has\n" +
                              $"{truck1.NextOilChange()} miles to next oil change and has\n" +
                              $"used about {truck1.TotalGalofGas().ToString("0.0")} Gallons of gas Total.");
        }
    }
}