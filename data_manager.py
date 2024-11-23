#!/usr/bin/env python3
"""
data_manager.py

This class is responsible for talking to the Google Sheet.

"""

import requests

__author__ = "Nelsandro"
__version__ = "0.1"


class DataManager:
    def __init__(self, google_sheet_bearer_token, google_sheet_endpoint):
        self.API_BEARER_TOKEN = google_sheet_bearer_token
        self.API_ENDPOINT = google_sheet_endpoint
        self.AUTH = {"Authorization": f"Bearer {self.API_BEARER_TOKEN}"}
        self.destinations_data = self.get_destinations_and_prices()

    def get_destinations_and_prices(self):
        response = requests.get(url=self.API_ENDPOINT, headers=self.AUTH)
        response.raise_for_status()
        return response.json()

    def update_new_lowest_price(self, destination, price):
        # TODO: Add implementation allowing to update the new lowest prince of the next 6 months"
        pass
