import random
from datetime import timedelta

import pytest

from iss.satellite import ObserverMeridian


def test_time_window():
    """
    Test that the two values returned by the time window are days apart
    """
    days = random.randint(1, 1000)

    observer = ObserverMeridian(35.227, -80.846)

    start, end = observer.time_window(days)

    assert end - start == timedelta(days=days)