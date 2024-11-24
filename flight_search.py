#!/usr/bin/env python3
"""
flight_search.py

This class is responsible for talking to the Flight Search API.

"""

__author__ = "Nelsandro"
__version__ = "0.1"

import requests
import datetime as dt
from dateutil.relativedelta import relativedelta


class FlightSearch:
    def __init__(self, amadeus_api_key: str, amadeus_api_key_secret: str, amadeus_base_end_point: str,
                 base_city: str):
        self.API_KEY = amadeus_api_key
        self.API_SECRET = amadeus_api_key_secret
        self.API_ENDPOINT = amadeus_base_end_point
        self.TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.token_header = {"Content-Type": "application/x-www-form-urlencoded"}
        self.parameters = {
            "grant_type": "client_credentials",
            "client_id": self.API_KEY,
            "client_secret": self.API_SECRET
        }
        self.BEARER_TOKEN = self.get_access_token()
        self.base_city = base_city

    def get_access_token(self):
        response = requests.post(url=self.TOKEN_ENDPOINT, headers=self.token_header, data=self.parameters)
        response.raise_for_status()
        return response.json()["access_token"]

    def get_flight_details(self, price: int, destination="LIS", number_of_offers="3"):
        today_date = dt.datetime.now().strftime("%Y-%m-%d")
        six_months_from_now = self._calculate_next_months(today_date)
        authorization = {"Authorization": f"Bearer {self.BEARER_TOKEN}"}
        v2_search_params = {
            "originLocationCode": self.base_city,
            "destinationLocationCode": destination,
            "departureDate": six_months_from_now,
            "adults": 1,
            "currencyCode": "EUR",
            "maxPrice": price,
            "max": number_of_offers

        }
        response = requests.get(url=self.API_ENDPOINT, headers=authorization, params=v2_search_params)
        return response.json()

    def _calculate_next_months(self, date: str) -> str:
        try:
            date = dt.datetime.strptime(date, '%Y-%m-%d')
            new_date = date + relativedelta(months=1)
            return new_date.strftime('%Y-%m-%d')
        except ValueError:
            return "Invalid date format. Please use 'YYYY-MM-DD'."
