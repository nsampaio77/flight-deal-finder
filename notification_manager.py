#!/usr/bin/env python3
"""
notification_manager.py

This class is responsible for sending notifications with the deal flight details.

Sample message: Low price alert! Only 41 Libras to fly from London-STN to Berlin-SXF, from 2020-08-25 to 2020-09-10.
"""
import smtplib

__author__ = "Nelsandro"
__version__ = "0.1"


class NotificationManager:
    def __init__(self, sender, destination, pass__):
        self.sender = sender
        self.destination = destination
        self.pass__ = pass__

    def send_notification(self, price, date, destination):
        print("sent")
        message = f" Low Price Alert! \n Only {price} Euros " \
                  f"to fly to {destination} on {date}"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            try:
                connection.login(user=self.sender, password=self.pass__)
                connection.sendmail(from_addr=self.sender,to_addrs=self.destination,
                                        msg=f"Subject: Low Price Alert! \n\n {message}")
            except Exception as e:
                print(f" Error: {e}")
