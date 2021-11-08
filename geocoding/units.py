#!/usr/bin/python3
# -*- coding: utf-8 -*-
# geo-coding is licensed under the Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#     http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
# PURPOSE.
# See the Mulan PSL v2 for more details.
# Create: 2021-7-13

import numpy as np

__all__ = ["units"]


class Units(object):
    """
    The geocoding.units module provides useful functions for performing angle
    and distance unit conversion.

    For convenience, we provide some short aliases
    (for example, km() is an alias for kilometers())

    """

    def __init__(self):
        self.rad = self.radians
        self.arcmin = self.arcminutes
        self.arcsec = self.arcseconds
        self.km = self.kilometers
        self.m = self.meters
        self.mi = self.miles
        self.ft = self.feet
        self.nm = self.nautical

    # Time
    @staticmethod
    def seconds(years=None, weeks=None, days=None, hours=None, minutes=None, seconds=None):
        """
        Convert time to seconds.

        Parameters
        ----------
        years
        weeks
        days
        hours
        minutes
        seconds

        Returns
        -------

        """
        if years is not None:
            return np.array(years) * 31536000.
        if weeks is not None:
            return np.array(weeks) * 604800.
        if days is not None:
            return np.array(days) * 86400.
        if hours is not None:
            return np.array(hours) * 3600.
        if minutes is not None:
            return np.array(minutes) * 60.
        if seconds is not None:
            return np.array(seconds)

        return None

    def years(self, years=None, weeks=None, days=None, hours=None, minutes=None, seconds=None):
        """
        Convert time to years.

        Parameters
        ----------
        years
        weeks
        days
        hours
        minutes
        seconds

        Returns
        -------

        """
        seconds = self.seconds(
            years=years,
            weeks=weeks,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds
        )
        if seconds is None:
            return None
        return seconds * 3.1710e-8

    def weeks(self, years=None, weeks=None, days=None, hours=None, minutes=None, seconds=None):
        """
        Convert time to weeks.

        Parameters
        ----------
        years
        weeks
        days
        hours
        minutes
        seconds

        Returns
        -------

        """
        seconds = self.seconds(
            years=years,
            weeks=weeks,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds
        )
        if seconds is None:
            return None
        return seconds * 1.6534e-6

    def days(self, years=None, weeks=None, days=None, hours=None, minutes=None, seconds=None):
        """
        Convert time to days.

        Parameters
        ----------
        years
        weeks
        days
        hours
        minutes
        seconds

        Returns
        -------

        """
        seconds = self.seconds(
            years=years,
            weeks=weeks,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds
        )
        if seconds is None:
            return None
        return seconds * 0.0000116

    def hours(self, years=None, weeks=None, days=None, hours=None, minutes=None, seconds=None):
        """
        Convert time to hours.

        Parameters
        ----------
        years
        weeks
        days
        hours
        minutes
        seconds

        Returns
        -------

        """
        seconds = self.seconds(
            years=years,
            weeks=weeks,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds
        )
        if seconds is None:
            return None
        return seconds * 0.0002778

    def minutes(self, years=None, weeks=None, days=None, hours=None, minutes=None, seconds=None):
        """
        Convert time to minutes.

        Parameters
        ----------
        years
        weeks
        days
        hours
        minutes
        seconds

        Returns
        -------

        """
        seconds = self.seconds(
            years=years,
            weeks=weeks,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds
        )
        if seconds is None:
            return None
        return seconds * 0.0166667

    # Angles
    @staticmethod
    def degrees(degrees=None, radians=None, arcminutes=None, arcseconds=None):
        """
        Convert angle to degrees.

        Parameters
        ----------
        degrees
        radians
        arcminutes
        arcseconds

        Returns
        -------

        """

        if degrees is not None:
            return np.array(degrees)

        if radians is not None:
            return np.degrees(radians)

        if arcminutes is not None:
            return np.array(arcminutes) / 60.

        if arcseconds is not None:
            return np.array(arcseconds) / 3600.

        return None

    @staticmethod
    def radians(degrees=None, radians=None, arcminutes=None, arcseconds=None):
        """
        Convert angle to radians.

        Parameters
        ----------
        radians
        degrees
        arcminutes
        arcseconds

        Returns
        -------

        """
        if degrees is not None:
            return np.radians(degrees)

        if radians is not None:
            return np.array(radians)

        if arcminutes is not None:
            return np.radians(np.array(arcminutes) / 60.)

        if arcseconds is not None:
            return np.radians(np.array(arcseconds) / 3600.)

        return None

    @staticmethod
    def arcminutes(degrees=None, radians=None, arcminutes=None, arcseconds=None):
        """
        Convert angle to arcminutes.

        Parameters
        ----------
        arcminutes
        degrees
        radians
        arcseconds

        Returns
        -------

        """
        if degrees is not None:
            return np.array(degrees) * 60.

        if radians is not None:
            return np.degrees(radians) * 60.

        if arcminutes is not None:
            return np.array(arcminutes)

        if arcseconds is not None:
            return np.array(arcseconds) / 60.

        return None

    @staticmethod
    def arcseconds(degrees=None, radians=None, arcminutes=None, arcseconds=None):
        """
        Convert angle to arcseconds.

        Parameters
        ----------
        arcseconds
        degrees
        radians
        arcminutes

        Returns
        -------

        """
        if degrees is not None:
            return np.array(degrees) * 3600.

        if radians is not None:
            return np.degrees(radians) * 3600.

        if arcminutes is not None:
            return np.array(arcminutes) * 60.

        if arcseconds is not None:
            return np.array(arcseconds)

        return None

    # Lengths
    @staticmethod
    def kilometers(kilometers=None, meters=None, miles=None, feet=None, nautical=None):
        """
        Convert distance to kilometers.

        Parameters
        ----------
        kilometers
        meters
        miles
        feet
        nautical

        Returns
        -------

        """
        if kilometers is not None:
            return np.array(kilometers)

        if meters is not None:
            return np.array(meters) / 1000.

        if miles is not None:
            return np.array(miles) * 1.609344

        if feet is not None:
            return np.array(feet) * 0.0003048

        if nautical is not None:
            return np.array(nautical) * 1.852

        return None

    def meters(self, kilometers=None, meters=None, miles=None, feet=None, nautical=None):
        """
        Convert distance to meters.

        Parameters
        ----------
        kilometers
        meters
        miles
        feet
        nautical

        Returns
        -------

        """
        kilometers = self.kilometers(
            kilometers=kilometers,
            meters=meters,
            miles=miles,
            feet=feet,
            nautical=nautical
        )
        if kilometers is None:
            return None
        return kilometers * 1000.

    def miles(self, kilometers=None, meters=None, miles=None, feet=None, nautical=None):
        """
        Convert distance to miles.

        Parameters
        ----------
        miles
        kilometers
        meters
        feet
        nautical

        Returns
        -------

        """
        kilometers = self.kilometers(
            kilometers=kilometers,
            meters=meters,
            miles=miles,
            feet=feet,
            nautical=nautical
        )
        if kilometers is None:
            return None
        return kilometers * 0.6213712

    def feet(self, kilometers=None, meters=None, miles=None, feet=None, nautical=None):
        """
        Convert distance to feet.

        Parameters
        ----------
        feet
        kilometers
        meters
        miles
        nautical

        Returns
        -------

        """
        kilometers = self.kilometers(
            kilometers=kilometers,
            meters=meters,
            miles=miles,
            feet=feet,
            nautical=nautical
        )
        if kilometers is None:
            return None
        return kilometers * 3280.839895

    def nautical(self, kilometers=None, meters=None, miles=None, feet=None, nautical=None):
        """
        Convert distance to nautical miles.

        Parameters
        ----------
        nautical
        kilometers
        meters
        miles
        feet

        Returns
        -------

        """
        kilometers = self.kilometers(
            kilometers=kilometers,
            meters=meters,
            miles=miles,
            feet=feet,
            nautical=nautical
        )
        if kilometers is None:
            return None
        return kilometers * 0.5399568


units = Units()
