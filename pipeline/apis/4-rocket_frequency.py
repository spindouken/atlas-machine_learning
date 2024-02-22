#!/usr/bin/env python3
"""
using the (unofficial) SpaceX API
"""
import requests


def fetch_rocket_name_by_id(rocket_id):
    """
    fetches the name of the rocket given its ID
    """
    rocket_url = "https://api.spacexdata.com/v4/rockets/{}".format(rocket_id)
    response = requests.get(rocket_url)  # send GET request for rocket details
    rocket_data = response.json()  # parse the JSON response into a dictionary
    return rocket_data.get("name")  # return the name of the rocket


def fetch_spacex_launches():
    """
    displays the number of launches per rocket
    """
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    launches = response.json()

    rocket_launch_counts = {}

    for launch in launches:  # loop through all launches
        rocket_id = launch["rocket"]  # get the rocket ID
        rocket_name = fetch_rocket_name_by_id(
            rocket_id  # get the rocket name from the ID
        )  # get the rocket name from the ID
        if rocket_name:  # if the rocket name is not None
            if rocket_name in rocket_launch_counts:  # if rocket is in dict
                rocket_launch_counts[rocket_name] += 1  # increment the count
            else:
                rocket_launch_counts[rocket_name] = 1  # add rocket to the dict

    # sorting by number of launches (descending)
    #    and then by rocket name (ascending)
    sorted_rockets = sorted(rocket_launch_counts.items(),
                            key=lambda x: (-x[1], x[0]))

    for rocket in sorted_rockets:
        print("{}: {}".format(rocket[0], rocket[1]))


if __name__ == "__main__":
    fetch_spacex_launches()
