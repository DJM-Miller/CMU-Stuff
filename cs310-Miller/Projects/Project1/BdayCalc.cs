using System;
using System.Globalization;


namespace BdayCalc
{
    public class BdayCalc
    {
        static void Main(string[] args)
        {
            var CurrentTime = DateTime.Now;
            //Get Birthday from Console
            Console.WriteLine("\nEnter Valid Birthday for someone 0 to 120 years old");
            int day, month, year;
            do
            {
                Console.Write("Enter your Birth Year: ");
                year = int.Parse(Console.ReadLine()!);
                if(year > CurrentTime.Year || (CurrentTime.Year - year > 120))
                    Console.WriteLine("Invalid Year try again!");
            } while (year > CurrentTime.Year || (CurrentTime.Year - year > 120));
            do
            {
                Console.Write("Enter the month you were born(1-12): ");
                month = int.Parse(Console.ReadLine()!);
                if((year == CurrentTime.Year && month > CurrentTime.Month) || (month < 0 || month > 12))
                    Console.WriteLine("Invalid Month try again!");
            } while((year == CurrentTime.Year && month > CurrentTime.Month) || (month < 1 || month > 12));

            do
            {
                Console.Write("Enter the day you were born: ");
                day = int.Parse(Console.ReadLine()!);
                if((year == CurrentTime.Year && month == CurrentTime.Month && day > CurrentTime.Day) 
                        || (day < 0 && day > 32))
                    Console.WriteLine("Invalid Day try again!");
            } while ((year == CurrentTime.Year && month == CurrentTime.Month
                     && day > CurrentTime.Day) || (day < 1 || day > 31));

            var Bday = new DateTime(year, month, day);

            //Calculate age
            var Age = CurrentTime - Bday;
            double ageYears = Age.TotalDays / 365.24;
            Console.WriteLine($"\nYour Birthday is {Bday.ToString()}");
            Console.WriteLine($"Your are {ageYears.ToString("0.0")} Years old");

            //Find Western Astrological Sign
            Console.Write("Your Western Astrological sign is ");
            switch (month)
            {
                case 1:
                    if (day < 20)
                        Console.Write("Capricorn\n");
                    else
                        Console.Write("Aquarius\n");
                    break;
                case 2:
                    if (day < 19)
                        Console.Write("Aquarius\n");
                    else
                        Console.Write("Pisces\n");
                    break;
                case 3:
                    if (day < 21)
                        Console.Write("Pisces\n");
                    else
                        Console.Write("Ares\n");
                    break;
                case 4:
                    if (day < 20)
                        Console.Write("Ares\n");
                    else
                        Console.Write("Taurus\n");
                    break;
                case 5:
                    if (day < 21)
                        Console.Write("Taurus\n");
                    else
                        Console.Write("Gemini\n");
                    break;
                case 6:
                    if (day < 22)
                        Console.Write("Gemini\n");
                    else
                        Console.Write("Cancer\n");
                    break;
                case 7:
                    if (day < 23)
                        Console.Write("Cancer\n");
                    else
                        Console.Write("Leo\n");
                    break;
                case 8:
                    if (day < 23)
                        Console.Write("Leo\n");
                    else
                        Console.Write("Virgo\n");
                    break;
                case 9:
                    if (day < 23)
                        Console.Write("Virgo\n");
                    else
                        Console.Write("Libra\n");
                    break;
                case 10:
                    if (day < 24)
                        Console.Write("Libra\n");
                    else
                        Console.Write("Scorpio\n");
                    break;
                case 11:
                    if (day < 23)
                        Console.Write("Scorpio\n");
                    else
                        Console.Write("Sagittarius\n");
                    break;
                case 12:
                    if (day < 22)
                        Console.Write("Sagittarius\n");
                    else
                        Console.Write("Capricon\n");
                    break;

            }

            //Find Chinese Zodiac Sign 
            System.Globalization.ChineseLunisolarCalendar Chinese = new ChineseLunisolarCalendar();
            int ChineseYear = Chinese.GetYear(Bday);
            int zodiac = ChineseYear - 1900;
            if (zodiac < 0)
                zodiac = zodiac * -1;
            Console.Write("Your Chinese Zodiac sign is ");
            switch (zodiac %12)
            {
                case 0:
                    Console.Write("Rat\n");
                    break;
                case 1:
                    Console.Write("Ox\n");
                    break;
                case 2:
                    Console.Write("Tiger\n");
                    break;
                case 3:
                    Console.Write("Rabbit\n");
                    break;
                case 4:
                    Console.Write("Dragon\n");
                    break;
                case 5:
                    Console.Write("Snake\n");
                    break;
                case 6:
                    Console.Write("Horse\n");
                    break;
                case 7:
                    Console.Write("Goat\n");
                    break;
                case 8:
                    Console.Write("Monkey\n");
                    break;
                case 9:
                    Console.Write("Rooster\n");
                    break;
                case 10:
                    Console.Write("Dog\n");
                    break;
                case 11:
                    Console.Write("Pig\n");
                    break;
            }
        }
    }
}
