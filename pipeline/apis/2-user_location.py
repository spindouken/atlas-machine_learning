#!/usr/bin/env python3
"""
prints the location of a specific user
"""
import requests
import sys
import datetime


def print_user_location(api):
    """
    prints the location of a specific user

    The user is passed as first argument of the script
        with the full API URL
        example:
        ./2-user_location.py https://api.github.com/users/holbertonschool
    If the user doesn’t exist, prints Not found
    If the status code is 403,
        prints Reset in X min where X is the number of minutes from now
        and the value of X-Ratelimit-Reset
    """
    response = requests.get(api)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_timestamp = response.headers.get("X-Ratelimit-Reset")
        reset_time = datetime.fromtimestamp(int(reset_timestamp))
        now = datetime.now()
        difference = reset_time - now
        print("Reset in {} min".format(difference.seconds // 60))
    else:
        location = response.json().get("location")
        print(location)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        useraddress = sys.argv[1]
        print_user_location(useraddress)
    else:
        print("No API URL provided. Please provide an API URL as an argument.")
