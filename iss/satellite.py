from datetime import datetime, timedelta, timezone

from skyfield.api import load, wgs84


class ObserverMeridian:
    """
    An observer at a particular location.
    Methods provide passover times for a satellite
    """

    def __init__(self, lat, lon, altitude_degrees=30.0):
        self.lat = lat
        self.lon = lon
        self.altitude_degrees = altitude_degrees

    def rise_and_set_time(self, satellite):
        """
        Accepts a satellite, returns the next rise and set time for that satellite
        as a tuple of datetimes
        """

        # create skyfield latlon
        loc = wgs84.latlon(self.lat, self.lon)

        # create timescale
        ts = load.timescale()
        t0, t1 = ts.from_datetimes(self.time_window(1))

        # get events where satellite reaches altitude at location in time window
        times, _ = satellite.find_events(
            loc, t0, t1, altitude_degrees=self.altitude_degrees
        )

        # get rise and sent time for first event
        rise_time = times[0].utc_datetime()
        set_time = times[2].utc_datetime()

        return (rise_time, set_time)

    def time_window(self, days):
        """
        Accpets a number of days, returns a time window from now until days away
        as a tuple of datetimes
        """
        now = datetime.now(timezone.utc)

        return (now, now + timedelta(days=days))
