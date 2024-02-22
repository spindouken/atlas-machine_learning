#!/usr/bin/env python3
"""
looking for available starships!
"""
import requests


def parse_passenger_capacity(passenger_str):
    """
    parses the passenger capacity string to an integer
    Returns 0 if the string cannot be directly converted
    """
    try:
        # if string includes commas, remove them before conversion
        return int(passenger_str.replace(",", ""))
    except ValueError:
        return 0  # return 0 if conversion fails


def availableShips(passengerCount):
    """
    returns the list of ships that can hold a given number of passengers
    If no ship available, returns an empty list
    """
    url = "https://swapi.dev/api/starships/"  # API for starships
    ships = []  # initialize list to hold names of suitable starships

    while url:  # loop until there are no more pages to fetch
        response = requests.get(url)  # send GET request to the API
        data = response.json()  # parse response as JSON

        for ship in data["results"]:  # loop over ships
            passengers = parse_passenger_capacity(ship["passengers"])
            if passengers >= passengerCount:
                ships.append(ship["name"])

        url = data["next"]  # get URL for the next page

    return ships  # return the list of suitable starships
