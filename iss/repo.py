"""
This module - Repository handles all requests to external api's / resources
"""

import itertools
from collections import defaultdict

import requests
from skyfield.api import load

from iss import models


def get_iss_location():
    """
    Gets the ISS location for the api and returns a validated set of Coordinates
    """

    ISS_LOCATION_NOW_URL = "http://api.open-notify.org/iss-now.json"

    iss_location = requests.get(ISS_LOCATION_NOW_URL)

    position = iss_location.json()["iss_position"]

    return models.Coordinates(**position)


def get_people_in_space():
    """
    Get the people in space from the api and returns a list of people by craft
    """
    PEOPLE_IN_SPACE_URL = "http://api.open-notify.org/astros.json"

    people_in_space = requests.get(PEOPLE_IN_SPACE_URL)

    people = people_in_space.json()["people"]
    group = defaultdict(list)

    for person in people:
        group[person["craft"]].append(person["name"])

    return list(group.items())


def get_satellites():
    """
    Gets a list of satellites from celestrak and returns a dictionary of
    skyfield EarthSatellites
    """
    STATIONS_URL = "http://celestrak.com/NORAD/elements/stations.txt"

    satellites = load.tle_file(STATIONS_URL)

    return {sat.name: sat for sat in satellites}