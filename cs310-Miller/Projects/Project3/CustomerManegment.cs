//Written by Darrin Miller
 using System;

namespace CustomerManegment
{
    public class CustomerManegment
    {
        interface ICustomer
        {
            void CreateReceipt(double subtotal);
            void PrintCustInfo();
            void ChangePhoneNum(string newNumber);
        }
        public class BusinessCustomer : ICustomer , IComparable<BusinessCustomer>
        {
            private string firstname;
            private string lastname;
            private int id;
            private string business;
            private string phone;

            public BusinessCustomer(string first, string last, int id, string bus, string phone)
            {
                this.firstname = first;
                this.lastname = last;
                this.id = id;
                this.business = bus;
                this.phone = phone;
            }
            public void CreateReceipt(double subtotal)
            {
                Console.WriteLine($"subtotal:  {subtotal.ToString("0.00")}");
                Console.WriteLine($"Total:     {(subtotal*1.09).ToString("0.00")}");
                Console.WriteLine($"Thank you {firstname} {lastname} from {business}");
                Console.WriteLine("for shopping with us today!");
                Console.WriteLine("Hope to see you again soon!");
            }
            public void PrintCustInfo()
            {
                Console.WriteLine($"Firstname:     {firstname}");
                Console.WriteLine($"Lastname:      {lastname}");
                Console.WriteLine($"Id number:     {id.ToString("00000")}");
                Console.WriteLine($"Business name: {business}");
                Console.WriteLine($"Phone number:  {phone}");
            }
            public void ChangePhoneNum(string newNumber)
            {
                this.phone = newNumber;
            }
            public override string ToString()
            {
                return $"Firstname:     {firstname}\n" +
                       $"Lastname:      {lastname}\n" +
                       $"Id number:     {id.ToString("00000")}\n" +
                       $"Business name: {business}\n" +
                       $"Phone number:  {phone}\n";

            }
            public int CompareTo(BusinessCustomer? somecustomer)
            {
                if (somecustomer == null) throw new ArgumentNullException(nameof(somecustomer));
                    return this.id.CompareTo(somecustomer.id);
            }

        }
        
        
        
        static void Main(string[] args)
        {
            //Reads from file and populates BusCusts Stack
            //Informations in input file must be formatted as below, no spaces
            //firstname,lastname,idNumber,Business,Phone
            List<BusinessCustomer> BusCusts = new List<BusinessCustomer>();
            string info_file = @"..\..\..\CustInfo.txt";
            string out_file = @"..\..\..\OutFile.txt";
            using (StreamReader sr = new StreamReader(info_file))
            {
                string? line;
                line = sr.ReadLine();
                while (line != null)
                {
                    string[] piece = line.Split(',', StringSplitOptions.None);
                    BusCusts.Add(new BusinessCustomer(piece[0], piece[1], Int32.Parse(piece[2]), piece[3], piece[4]));
                    line = sr.ReadLine();
                }
            }

            //Outputs all customer data to console
            foreach (var i in BusCusts)
            {
                Console.WriteLine();
                i.PrintCustInfo();
            }
            //Sorts the outputs all customer data 
            BusCusts.Sort();
            foreach (var i in BusCusts)
            {
                Console.WriteLine();
                i.PrintCustInfo();
            }
            
            //Displays createreceipt method
            Console.WriteLine("\n\n");
            BusCusts[0].CreateReceipt(52.35);
            
            //Outputs formatted customer info to file
            using (StreamWriter sw = new StreamWriter(out_file))
            {
                foreach (var i in BusCusts)
                {
                    sw.WriteLine(i.ToString());
                }

                
            }

        }
    }
}
