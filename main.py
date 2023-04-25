from pprint import pprint

import requests


class CountryInfoAPI:
    def __init__(self) -> None:
        self.base_api_url = "https://restcountries.com/v3.1"
        self.session = requests.Session()

    def get_country_info(self, name: str) -> dict:
        api_url = f"{self.base_api_url}/translation/{name.lower()}/"
        response = self.session.get(api_url)
        if response.status_code != 200:
            raise Exception("County didn't found")
        else:
            return response.json()

    def __del__(self) -> None:
        if self.session:
            self.session.close()
            del self.session


def main():
    country_api_client = CountryInfoAPI()
    country_name = input("Enter the country's name:")
    country_info = country_api_client.get_country_info(country_name.strip())
    pprint(country_info)


if __name__ == "__main__":
    main()

