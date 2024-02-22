#!/usr/bin/env python3
"""
returns list of species in the Star Wars universe that are sentient
"""
import requests


def get_json(url, session):
    """
    get JSON data from given URL with provided session

    url: URL to get data from
    session: requests.Session object for efficient HTTP requests
    return: JSON response as a dictionary if no error, otherwise None
    """
    try:
        response = session.get(url)  # make HTTP GET request to the URL
        response.raise_for_status()  # raise an exception for HTTP errors
        return response.json()  # return the JSON content of the response
    except requests.RequestException as e:
        print(f"request failed: {e}")  # print error message if request fails
        return None  # return None if an exception occurs


def sentientPlanets():
    """
    returns the list of names of the home planets of all sentient species
    """
    url = "https://swapi.dev/api/species/"  # initial URL to fetch species data
    planets = set()  # initialize an empty set to store unique planet names
    session = requests.Session()  # create a session for connection pooling

    while url:
        data = get_json(url, session)  # fetch data from the current URL
        if not data:
            break  # exit the loop if data fetching fails

        for species in data["results"]:  # loop through species in fetched data
            # check if species is classified or designated as sentient
            if (
                "sentient" in species.get("classification", "").lower()
                or "sentient" in species.get("designation", "").lower()
            ):
                planet_url = species.get("homeworld")  # get URL of homeworld
                if planet_url:
                    planet_data = get_json(
                        planet_url, session
                    )  # fetch data for the homeworld
                    if planet_data:
                        planets.add(planet_data["name"])  # add planet to set

        url = data.get("next")  # update the URL to fetch the next page

    return planets  # return the set of unique planet names
