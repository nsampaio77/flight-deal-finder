#!/usr/bin/env python3
"""
main.py

An app with the goal to e-mail you automatically, with information about flight deals

"""
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from variables import (GOOGLE_SHEET_ENDPOINT,
                       GOOGLE_SHEET_BEARER_TOKEN,
                       GMAIL_ACCOUNT_SENDER,
                       GMAIL_ACCOUNT_DEST,
                       GMAIL_ACCOUNT_PASS)

__author__ = "Nelsandro"
__version__ = "0.1"

d_manager = DataManager(google_sheet_bearer_token=GOOGLE_SHEET_BEARER_TOKEN,
                        google_sheet_endpoint=GOOGLE_SHEET_ENDPOINT)
destination_and_prices = d_manager.get_destinations_and_prices()
flight_manager = FlightData(sender=GMAIL_ACCOUNT_SENDER,
                            destination=GMAIL_ACCOUNT_DEST,
                            pass__=GMAIL_ACCOUNT_PASS,
                            destination_price=destination_and_prices)
flight_manager.compare_prices_and_send_notification()
