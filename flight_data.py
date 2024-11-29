#!/usr/bin/env python3
"""
flight_data.py

This class is responsible for structuring the flight data.

"""
from flight_search import FlightSearch
from notification_manager import NotificationManager
from variables import AMADEUS_BASE_ENDPOINT, AMADEUS_API_KEY, AMADEUS_API_KEY_SECRET
import json


__author__ = "Nelsandro"
__version__ = "0.1"


def test():
    # Define a dictionary to hold all the data
    combined_data = []

    # List of JSON file paths
    file_paths = ["data_entry_1.json", "data_entry_2.json", "data_entry_3.json", "data_entry_4.json"]

    # Loop through the file paths and load the data
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            data = json.load(f)  # Load the JSON data
            combined_data.append(data)  # Append the data to the list
    return combined_data



class FlightData(NotificationManager):
    def __init__(self, destination_price, sender, destination, pass__):
        self.f_searcher = FlightSearch(amadeus_api_key=AMADEUS_API_KEY, amadeus_api_key_secret=AMADEUS_API_KEY_SECRET,
                                       amadeus_base_end_point=AMADEUS_BASE_ENDPOINT, base_city="WAW",
                                       destinations=destination_price)
        self.all_flight_offers_list = self.f_searcher.get_flight_details_for_all_cities()
        super().__init__(sender, destination, pass__)
        self.destination_price_data = destination_price
        self.flight_date = self.f_searcher.flight_date
        self.google_sheet_price = 0
        self.current_flight_price = 0
        self.final_destination = ""


    def compare_prices_and_send_notification(self):
        for offer in self.all_flight_offers_list:
            for desired_destination in self.destination_price_data["prices"]:
                try:
                    list_of_stops = offer["data"][0]["itineraries"][0]["segments"]
                    self.final_destination = list_of_stops[len(list_of_stops)-1]["arrival"]["iataCode"]
                    if self.final_destination == desired_destination["iataCode"]:
                        self.google_sheet_price = desired_destination["lowestPrice"]
                        current_flight_price = float(offer["data"][0]["price"]["grandTotal"])
                        if self.google_sheet_price > self.current_flight_price:
                            self.send_notification(price=current_flight_price,
                                                   date=self.flight_date,
                                                   destination=self.final_destination)
                except IndexError as e:
                    print(f"No offers were found problably: {e}")

