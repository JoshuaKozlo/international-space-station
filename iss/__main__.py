import sys
from datetime import datetime

from iss import message, models, repo
from iss.satellite import ObserverMeridian


def loc():
    """
    Gets the International Space Station coordinates and prints it

    Example:
    python -m iss loc
    """

    # get iss location from api
    coord = repo.get_iss_location()

    msg = message.location(coord.lat, coord.lon, datetime.now())
    print(msg)


def passover():
    """
    Gets the International Space Station passover time at specific coordinates provided via command-line arguements
    and prints it

    Example:
    python -m iss pass 35.2333925 -80.8428828
    """

    # get lat & lon as 2nd and 3rd command-line arguements
    try:
        lat, lon = sys.argv[2:4]
        coord = models.Coordinates(lat=lat, lon=lon)
    except:
        raise ValueError("Enter a valid lat and lon")

    # get satellites tle from server
    satellites = repo.get_satellites()
    iss = satellites["ISS (ZARYA)"]

    # create observer
    observer = ObserverMeridian(coord.lat, coord.lon)
    rise_time, set_time = observer.rise_and_set_time(iss)

    duration = set_time - rise_time

    msg = message.overhead(coord.lat, coord.lon, rise_time, duration)
    print(msg)


def people():
    """
    Gets all the people in space by craft and prints

    Example:
    python -m iss people
    """
    people = repo.get_people_in_space()

    msg = message.people(people)
    print(msg)


# get first command line arguement
task = sys.argv[1]

if task == "loc":
    loc()

elif task == "pass":
    passover()

elif task == "people":
    people()
else:
    raise ValueError("Invalid arguement: loc, pass, people")
