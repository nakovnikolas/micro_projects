from datetime import (
    date,
    timedelta
)
import os
from dotenv import load_dotenv
import requests
import logging


# Load environment variables from .env file
load_dotenv()
# Set the basic config of the logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s-%(levelname)s-%(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)


class FinancialDataRetrievalSystem:
    def __init__(
        self,
        api_key: str,
        fmp_api_key: str,
        days_from_today: int
    ) -> None:
        # Initialize attributes
        self.api_key: str = api_key
        self.fmp_api_key: str = fmp_api_key
        self.base_url_price: str = "https://api.polygon.io/v2/aggs/ticker/"
        self.base_url_info: str = "https://api.polygon.io/v3/reference/tickers/"
        self.base_url_fmp: str = "https://financialmodelingprep.com/api/v3/stock_market/"
        self.date = date.today() - timedelta(days=days_from_today)

    def get_currency_exchange_rate(
        self,
        base_currency: str,
        target_currency: str
    ) -> float | None:
        # Retrieve the current exchange rate between
        # two currencies using the currency API
        url = f"{self.base_url_price}C:{base_currency.upper()}{target_currency.upper()}/range/1/day/{self.date}/{self.date}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data["results"][0]["c"]
        else:
            logging.info("404: Finance info not found")
            return None

    def get_company_share_price(self, company_symbol: str) -> float:
        # Retrieve the current price of
        # shares for a given company using the share API
        url = f"{self.base_url_price}{company_symbol}/range/1/day/{self.date}/{self.date}?apiKey={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "results" in data:
                return data["results"][0]["c"]
            else:
                logging.error(f"No info for {data['ticker']} company symbol")
                return data["ticker"]
        else:
            logging.error("404: Finance info not found")

    def get_currency_conversion(
        self,
        amount: float,
        base_currency: str,
        target_currency: str
    ) -> float:
        # Convert the given amount from one currency to another
        exchange_rate = self.get_currency_exchange_rate(
            base_currency,
            target_currency
        )
        converted_amount: float = amount * exchange_rate

        return converted_amount

    def get_company_info(self, company_symbol: str) -> None:
        # Retrieve additional information about a company (e.g., name, sector) using the share API
        url = f"{self.base_url_info}{company_symbol}?apiKey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data: dict[str] = response.json()
            result: dict[str] = data["results"]
            print(f"Company name: {result['name']}")
            print(f"Sector: {result['sic_description']}")
            print(f"Number of employees: {result['total_employees']}")
            print(f"Description: {result['description']}")
            print(f"Homepage: {result['homepage_url']}")
        else:
            logging.error("404: Finance info not found")

    def get_top_gainers(self):
        # Retrieve the top gaining companies from the share API
        url = f"{self.base_url_fmp}gainers?apikey={self.fmp_api_key}"
        response = requests.get(url)
        data = response.json()

        for company in data:
            print(company)
            print()

    def get_top_losers(self):
        # Retrieve the top losing companies from the share API
        url = f"{self.base_url_fmp}losers?apikey={self.fmp_api_key}"
        response = requests.get(url)
        data = response.json()

        for company in data:
            print(company)
            print()


# Example usage of the Financial Data Retrieval System
if __name__ == "__main__":
    # Configure API keys
    api_key = os.getenv("API_KEY")
    fmp_api_key = os.getenv("FMP_API_KEY")

    # Initialize the FinancialDataRetrievalSystem object
    financial_system = FinancialDataRetrievalSystem(
        api_key,
        fmp_api_key,
        days_from_today=1
    )

    # Call methods of the FinancialDataRetrievalSystem object as needed...
    financial_system.get_top_gainers()
    financial_system.get_top_losers()
