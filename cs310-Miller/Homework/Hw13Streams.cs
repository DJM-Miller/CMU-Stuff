using System;

namespace HW13
{
    public class HW13Streams
    {
        static void Main(string[] args)
        {
            string in_file = @"..\..\..\in_file.txt";
            string out_file = @"..\..\..\out_file.txt";
            
            using (StreamReader sr = new StreamReader(in_file))
            {
                using (StreamWriter sw = new StreamWriter(out_file))
                {
                    int count = 0;
                    string? line;
                    do
                    {
                        line = sr.ReadLine();
                        if (count % 4 == 0)
                            sw.WriteLine("REDACTED");
                        else
                            sw.WriteLine(line);
                        count++;
                    } while (line != null);
                }
            }
        }
    }
}