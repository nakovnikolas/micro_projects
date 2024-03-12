import requests

# Replace 'YOUR_API_KEY' with your actual API key from Finnhub
API_KEY = '43671c44b8721d12f3580ace48d48b97'



url = f"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={API_KEY}"
headers = {
        "Content-Type": "application/json",
        "Authorization": f"X-Finnhub-Token : {API_KEY}"
    }
response = requests.get(url, headers=headers)
data = response.json()

print(data)



# # Example usage
# top_gainers_data = get_top_gainers()

# # Print the top gaining companies
# print("Top Gaining Companies:")
# for result in top_gainers_data:
#     print("Symbol:", result['symbol'])
#     print("Name:", result['companyName'])
#     print("Change:", result['change'])
#     print("Percent Change:", result['changesPercentage'])
#     print("----------")
