#!/usr/bin/env python3
"""
looking for available starships!
"""
import requests


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
            # check if passengers is a digit and meets the capacity requirement
            if (
                ship["passengers"].isdigit()
                and int(ship["passengers"]) >= passengerCount
            ):
                ships.append(ship["name"])  # add ship name if criteria met

        url = data["next"]  # get URL for the next page

    return ships  # return the list of suitable starships
