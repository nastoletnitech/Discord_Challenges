using System.Collections.ObjectModel;

namespace DataLibrary.Models
{
    public class NameJsonModel
    {
        public Data Data { get; set; }
    }

    public class Dates    {
        public int Day { get; set; } 
        public int Month { get; set; } 
    }

    public class Namedays    {
        public string Pl { get; set; } 
    }

    public class Data    {
        public Dates Dates { get; set; } 
        public Namedays Namedays { get; set; } 
    }
}