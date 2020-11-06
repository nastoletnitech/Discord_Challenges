using System;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using DataLibrary.Models;
using Newtonsoft.Json;

namespace DataLibrary
{
    public static class ApiCaller
    {
        private const string Url = "https://api.abalin.net/today?country=pl&timezone=Europe%2FPrague";
        private static HttpClient _httpClient;
        
        public static void InitializeClient()
        {
            _httpClient = new HttpClient {BaseAddress = new Uri(Url)};
        }

        private static async Task<T> GetAsync<T>(Uri url) where T: class, new()
        {
            var response = _httpClient.GetAsync(url);
            var json = await (await response).Content.ReadAsStringAsync();
            return JsonConvert.DeserializeObject<T>(json);
        }

        public static async Task<string> GetNames()
        {
            var names = await GetAsync<NameJsonModel>(_httpClient.BaseAddress);
            return names.Data.Namedays.Pl;
        }
    }
}