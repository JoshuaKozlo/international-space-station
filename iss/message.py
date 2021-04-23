"""
Functions here are purely for generating the messages to be output to the terminal
"""

from datetime import datetime


def location(lat, lon, t):

    return f"The ISS current location at {t.strftime('%I:%M %p')} UTC is {lat} {lon}"


def overhead(lat, lon, t, duration):

    return f"The ISS will be overhead {lat} {lon} at {t.strftime('%I:%M %p')} UTC for {duration}"


def people(crafts):
    msg = ""

    for craft, people in crafts:
        msg += f"There are {len(people)} aboard the {craft}. They are {', '.join(people)}.\n"

    return msg