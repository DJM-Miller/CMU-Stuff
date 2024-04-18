using System;



namespace EventManager
{
    public abstract class Customer
    { 
        private string name;
        private uint accNum;
        private bool member;
        public string Name
        {
            get { return this.name; }
            set { this.name = value; }
        }
        public uint AccNum
        {
            get { return this.accNum; }
            set { this.accNum = value; }
        }
        public bool Member
        {
            get { return this.member; }
            set { this.member = value; }
        }
        
        public abstract void JoinMember(bool join);

        public void PrintCustInfo()
        {
            Console.WriteLine($"Name:      {Name}");
            Console.WriteLine($"Account #: {AccNum.ToString("0000")}");
            Console.WriteLine($"Membership: {Member.ToString()}");
        }
    }

    public class ShopCustomer : Customer
    {
        public ShopCustomer(string n, uint an, bool mem = false)
        {
            this.Name = n;
            this.AccNum = an;
            this.Member = mem;
        }
        public override void JoinMember(bool join)
        {
            Member = join;
        }

        public void OnFinishedOrdering(object source, EventArgs args)
        {
            Console.WriteLine($"Thank you {Name} for placing an order!");
        }

        public void OnShipping(object source, EventArgs args)
        {
            Console.WriteLine($"{Name} your order has shipped!");
        }
    }

    public abstract class Orders
    {
        private string item;
        private double price;
        private int shipday;
        private const double TaxRate = 0.07; //Default tax rate = 7%
        public string Item
        {
            get { return this.item; }
            set { this.item = value; }
        }
        public double Price
        {
            get { return this.price; }
            set { this.price = value; }
        }
        public int Shipday
        {
            get { return this.shipday; }
            set { this.shipday = value; }
        }

        public abstract double TotalPrice();
        public abstract void CheckShipDay(int current_day);

    }

    public class ShopOrders : Orders
    {
        private int quantity;
        private const double TaxRate = 0.09;
        private ShopCustomer customer;
        public int Quantity
        {
            get { return this.quantity; }
            set { this.quantity = value; }
        }

        public delegate void ShopOrdersEventHandler(object source, EventArgs args);
        public event ShopOrdersEventHandler OrderPlaced;
        protected virtual void OnFinishedOrdering()
        {
            if (OrderPlaced != null)
            {
                OrderPlaced(this, null);
            }
        }
        
        public ShopOrders(ShopCustomer cust, int quantity, string item, double price, int currentday)
        {
            this.customer = cust;
            this.quantity = quantity;
            this.Item = item;
            this.Price = price;
            this.Shipday = currentday + 3;

            this.OrderPlaced += customer.OnFinishedOrdering;
            OnFinishedOrdering();
        }

        public delegate void CheckShipDayEventHandler(object source, EventArgs args);

        public event CheckShipDayEventHandler Shipped;

        protected virtual void OnShipping()
        {
            if (Shipped != null)
            {
                Shipped(this, null);
            }
        }
        
        public override void CheckShipDay(int current_day)
        {
            if (current_day == Shipday)
            {
                this.Shipped += customer.OnShipping;
                OnShipping();
            }
        }

        public override double TotalPrice()
        {
            double subtotal = quantity * Price;
            return (TaxRate * Price) + Price;
        }

        public void printOrder()
        {
            Console.WriteLine();
            customer.PrintCustInfo();
            Console.WriteLine($"Order Date:  {Shipday-3}");
            Console.WriteLine($"Item:        {Item}");
            Console.WriteLine($"Quantity:    {quantity}");
            Console.WriteLine($"Total Price: ${TotalPrice().ToString("0.00")}");
            Console.WriteLine();
        }
        
    }
    
    

    public class EventManager
    {
        //Prompts for new customer info and creates EventCustomer object to be added to custList
        static void NewCustomer(ref List<ShopCustomer> custList)
        {
            Console.Write("Enter your name: ");
            string name = Console.ReadLine()!;
            uint size = (uint) (int)custList.Count;
            custList.Add(new ShopCustomer(name,size+1));
        }

        static void PlaceOrder(int accNum, string item, int quant, double price,  List<ShopCustomer> custList, ref List<ShopOrders> orderList, int day)
        {
            orderList.Add(new ShopOrders(custList[accNum], quant, item, price, day));
        }
        
        
        static void Main(string[] args)
        {
            int day = 1;
            Console.WriteLine();
            
            //Creates a list of 10 Potential Customers
            List<ShopCustomer> custList = new List<ShopCustomer>();
            string[] nam = new string[10] {"Jeremy", "Luke", "Picard", "Yoda", "Jenny", 
                                            "Hanes", "Frank", "Kyle", "Henry", "Seth"};
            for (uint i = 0; i < 10; i++)
                custList.Add(new ShopCustomer(nam[i], i + 1));
            
            //Creates a list of Orders from randomly chosen Customers from Existing List
            List<ShopOrders> orderList = new List<ShopOrders>();
            Random rand = new Random();
            string[] products = new string[5] { "Apples", "Strawberries", "Tomatoes", "Carrots", "Peppers" };
                //Orders on day 1 ship day 4
            for (int i = 0; i < 5; i++)
                PlaceOrder(rand.Next(0, 9), products[i], i,(rand.Next(20)+rand.NextDouble()),custList, ref orderList, day);
            day++;
                //Orders on day 2 ship day 5
            for (int i = 0; i < 5; i++)
            {
                PlaceOrder(rand.Next(0, 9), products[rand.Next(0, 4)], i, (rand.Next(20) + rand.NextDouble()), custList,
                    ref orderList, day);
                Task.Delay(100).Wait();
            }
            day++;
               
            //Check which orders should ship then increments the day
            for (int i = 0; i < 4; i++)
            {
                foreach (var j in orderList)
                {
                    j.CheckShipDay(day);
                    Task.Delay(100).Wait();
                }
                day++;
            }
            
            //Two uses of LINQ
            var CustomerNames4Letters = from cust in custList
                where cust.Name.Length == 4
                select cust;
            Console.WriteLine("Printing Customer info for customers with 4 letter names:");
            foreach (var i in CustomerNames4Letters)
            {
                i.PrintCustInfo();
                Console.WriteLine();
            }

            
            var ordersOver50 = from order in orderList
                where order.TotalPrice() >= 10.0
                select order;
            Console.WriteLine("Printing Order details for orders >=$10");
            foreach (var i in ordersOver50)
            {
                i.printOrder();
            }




            //Prints All Orders to Screen
            /*
            foreach (var i in orderList)
            {
                i.printOrder();
            }
            */


        }
    }
}