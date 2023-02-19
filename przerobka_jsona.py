import csv
import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

rates = data[0]["rates"]

with open("output.csv", "w", newline="") as csvfile:
    fieldnames = ["currency", "code", "bid", "ask"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()

    for rate in rates:
        writer.writerow(rate)


        
        
"""
# Obliczenia do 2 części:
currencies = {}
with open("output.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=";")
    for row in reader:
        currencies[row["code"]] = row["ask"]
# print(currencies)
"""
