using System;

namespace DataLibrary
{
    public static class Calculator
    {
        public static double Add(double x, double y)
        {
            return x + y;
        }
        
        public static double Subtract(double x, double y)
        {
            return x - y;
        }
        
        public static double Multiple(double x, double y)
        {
            return x * y;
        }
        
        public static double Divide(double x, double y)
        {
            return x / y;
        }
        
        public static double Power(double x, double y)
        {
            return Math.Pow(x, y);
        }
        
        public static double Root(double x, double y)
        {
            return Math.Pow(x, 1 / y);
        }
    }
}