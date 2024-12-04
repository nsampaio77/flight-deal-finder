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

    def update_new_lowest_price_on_google_sheet(self, new_google_sheet):
        for row in new_google_sheet['prices']:
            url = self.API_ENDPOINT + f"/{row['id']}"
            payload = {"price": row}
            response = requests.put(url=url, json=payload, headers=self.AUTH)
            response.raise_for_status()
            # Raise for status and print response for debugging
            try:
                response.raise_for_status()
                print(f"Updated row {row['id']}: {response.json()}")
            except requests.exceptions.HTTPError as e:
                print(f"Error updating row {row['id']}: {e}")
