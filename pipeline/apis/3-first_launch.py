#!/usr/bin/env python3
"""
I gotta have that launch data!
"""
import requests
from datetime import datetime, timezone, timedelta


def get_name_by_id(endpoint, id):
    """
    fetches the name or other details of an entity (rocket or launchpad) by id
    """
    # crafting URL to ask SpaceX about either rockets or launchpads
    api_url = f"https://api.spacexdata.com/v4/{endpoint}/{id}"
    response = requests.get(api_url)  # api request
    if response.ok:  # if everything went well
        data = response.json()  # get the response as JSON
        return data
    return {}  # if something went wrong, return an empty dictionary


def get_first_launch_info():
    """
    gets information about specific SpaceX launch
    """
    api_url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(api_url)  # api request
    launches = response.json()  # get the response as JSON

    first_launch = next(  # get the first launch that matches the given name
        (
            launch
            for launch in launches  # loop through all launches
            if launch["name"] == "Galaxy 33 (15R) & 34 (12R)"  # check if match
        ),
        None,  # if no match, return None
    )
    if first_launch:  # if a match was found
        launch_name = first_launch["name"]  # get the name of the launch
        launch_date_unix = first_launch["date_unix"]  # get the launch date
        rocket_id = first_launch["rocket"]  # get the rocket id
        launchpad_id = first_launch["launchpad"]  # get the launchpad id

        rocket_info = get_name_by_id("rockets", rocket_id)  # get rocket info
        launchpad_info = get_name_by_id("launchpads", launchpad_id)

        # making sure we know when it happened in local time
        launch_date_local = datetime.fromtimestamp(
            launch_date_unix, tz=timezone.utc
        ).astimezone(timezone(timedelta(hours=-4)))
        formatted_date = launch_date_local.strftime(
            "%Y-%m-%dT%H:%M:%S%z"
        )  # adjust time formatting as desired

        return ("{launch_name} ({formatted_date}) {rocket_name} - "
                "{launchpad_name} ({launchpad_locality})"
                ).format(
                    launch_name=launch_name,
                    formatted_date=formatted_date,
                    rocket_name=rocket_info.get(
                        'name', 'Rocket name not available'
                        ),
                    launchpad_name=launchpad_info.get(
                        'name', 'Launchpad name not available'
                        ),
                    launchpad_locality=launchpad_info.get(
                        'locality', 'Launchpad locality not available'
                        )
                )
    else:
        return "Launch not found"


if __name__ == "__main__":
    launch_info = get_first_launch_info()
    print(launch_info)
