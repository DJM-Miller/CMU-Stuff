using System;

namespace HW9Interface
{
    public class HW9Interface
    {
        interface IAttack
        {
            //Calculates damage output
            double Damage();
            //Calculates action points left after attack
            bool Cost();
        }
        
        public class Slash : IAttack
        {
            public Slash(int power, int weaponScale, int actionPoints)
            {
                this.power = power;
                this.weapon_scale = weaponScale;
                this.action_points = actionPoints;
            }
            private int power;
            public int Power
            {
                get { return this.power; }
                set { this.power = value; }
            }
            private int weapon_scale;
            public int Weapon_scale
            {
                get { return this.weapon_scale; }
                set { this.weapon_scale = value; }
            }
            private int action_points;
            public int Action_points
            {
                get { return this.action_points; }
                set { this.action_points = value; }
            }
            public double Damage()
            {
                return power * weapon_scale;
            }
            public bool Cost()
            {
                if (action_points - power < 0)
                {
                    Console.WriteLine("Attack failed... Not enough AP");
                    return false;
                }
                else
                {
                    action_points = this.action_points - power;
                    return true;
                }
                
            }
            
        }
        static void Main(string[] args)
        { 
            Slash player1 = new Slash(5, 2, 9);
            Console.WriteLine($"Player 1 attempts an attack for {player1.Damage()} Damage");
            if(player1.Cost())
                Console.WriteLine($"Player 1 now has {player1.Action_points} Action points");
            Console.WriteLine($"Player 1 attempts an attack for {player1.Damage()} Damage");
            if(player1.Cost())
                Console.WriteLine($"Player 1 now has {player1.Action_points} Action points");
        }
    }
}


