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
import time
from .utils import parameter_check, RequestsRetrying
from . import units
from . import csys

__all__ = ["distances"]


@parameter_check(ndim=2)
def euclidean_distance(origins, destinations):
    """
    In mathematics, Euclidean distance or Euclidean metric is the "ordinary" (ie straight line)
    distance between two points in Euclidean space. Using this distance,
    the Euclidean space becomes the metric space.
    The associated norm is called the Euclidean norm.
    The earlier literature called it the Pythagorean metric.

    Parameters
    ----------
    origins
    destinations

    Returns
    -------

    """
    return np.linalg.norm(origins - destinations, axis=1)


@parameter_check(ndim=2)
def manhattan_distance(origins, destinations):
    """
    Taxi geometry or Manhattan Distance is a vocabulary created by Herman Minkowski
    in the 19th century. It is a geometric term used in geometric measurement spaces
    to indicate that two points are in a standard coordinate system.
    The sum of absolute wheelbases.

    Parameters
    ----------
    origins
    destinations

    Returns
    -------

    """
    return np.linalg.norm(origins - destinations, axis=1, ord=1)


@parameter_check(ndim=2)
def chebyshev_distance(origins, destinations):
    """
    In mathematics, the Chebyshev distance or L∞ metric is a metric in vector space.
    The distance between two points is defined as the maximum value of the absolute
    value of the difference between the coordinate values.
    From a mathematical point of view, Chebyshev distance is a metric
    derived from uniform norm (or called supremum norm),
    and it is also a kind of injective metric space.

    Parameters
    ----------
    origins
    destinations

    Returns
    -------

    """
    return np.linalg.norm(origins - destinations, axis=1, ord=np.inf)


@parameter_check(ndim=2)
def cosine(origins, destinations):
    """
    The cosine of the angle in geometry can be used to measure the difference
    between two vector directions. Machine learning uses this concept to
    measure the difference between sample vectors.
    The range of the angle cosine is [-1,1]. The larger the angle cosine,
    the smaller the angle between the two vectors,
    and the smaller the angle cosine, the larger the angle between the two vectors.
    When the directions of the two vectors coincide,
    the angle cosine takes the maximum value 1,
    and when the directions of the two vectors are completely opposite,
    the angle cosine takes the minimum value -1.

    Parameters
    ----------
    origins
    destinations

    Returns
    -------

    """
    return np.array([
        np.dot(o, d) / (np.linalg.norm(o) * np.linalg.norm(d))
        for o, d in zip(origins, destinations)
    ])


@parameter_check(ndim=2)
def driving_distance(origins, destinations, aks, tactics=11):
    """
    Calculate road distance and travel time from two points

    Parameters
    ----------
    origins
    destinations
    aks
    tactics  
        =10 do not take high speed; 
        = 11 conventional route; 
        = 12 distance is shorter; 
        = 13 distance is shorter

    Returns
    -------

    """
    BAIDU_DRIVING_BASE_API = "http://api.map.baidu.com/routematrix/v2/driving?output=json"
    requestsRetrying = RequestsRetrying()
    dists, durations, timestamps = [], [], []
    for o, d in zip(origins, destinations):
        dist, duration, timestamp = None, None, None
        for ak in aks:
            url = BAIDU_DRIVING_BASE_API + f"&origins={o[1]},{o[0]}&destinations={d[1]},{d[0]}&tactics={tactics}&ak={ak}"
            try:
                response = requestsRetrying.get_retrying(url=url, timeout=2)
                if response.get("status") != 0:
                    raise ValueError
            except AssertionError as e:
                response = {}

            if response:
                dist = response["result"][0]["distance"]["value"]
                duration = response["result"][0]["duration"]["value"]
                timestamp = int(time.time())
                break
        dists.append(dist)
        durations.append(duration)
        timestamps.append(timestamp)

    return (
        np.array(dists, dtype=np.float),
        np.array(durations, dtype=np.float),
        timestamps
    )


class Distances(object):
    def __init__(self):
        self.GEO_FUNCTIONS = {
            "euclidean": euclidean_distance,
            "manhattan": manhattan_distance,
            "chebyshev": chebyshev_distance,
            "cosine": cosine
        }
        self.DISTANCE_UNITS = {
            "km": units.km,
            "m": units.m,
            "mi": units.mi,
            "ft": units.ft,
            "nm": units.nm,
        }
        self.TIME_UNITS = {
            "y": units.years,
            "w": units.weeks,
            "d": units.days,
            "h": units.hours,
            "m": units.minutes,
            "s": units.seconds,
        }
        self.TRIP_FUNCTIONS = {
            "driving": driving_distance
        }
        self.BAIDU_AKS = ["k936lbWYFPwG1LEoKb9faZ8MEizFwh60"]

    def geo_distance(self,
                     origins: list,
                     destinations: list,
                     type_: str = "bd09",
                     metric: str = "euclidean",
                     unit: str = "m",
                     digit: int = None,
                     ):
        """

        Parameters
        ----------
        origins
        metric
        destinations
        unit
        type_
        digit

        Returns
        -------

        """
        if not isinstance(origins, (np.ndarray, list, tuple)):
            raise ValueError("origins parameter must be list/tuple/Numpy type!")
        if not isinstance(destinations, (np.ndarray, list, tuple)):
            raise ValueError("destinations parameter must be list/tuple/Numpy type!")
        if not isinstance(metric, str) or metric not in self.GEO_FUNCTIONS.keys():
            raise ValueError(
                f"metric parameter is must str type and only support "
                f"{'/'.join(list(self.DISTANCE_UNITS.keys()))}!"
            )
        if not isinstance(unit, str) or unit not in self.DISTANCE_UNITS.keys():
            raise ValueError(
                f"unit parameter is must str type and only support "
                f"{'/'.join(list(self.DISTANCE_UNITS.keys()))}!"
            )
        origins = np.array(
            csys.convert(
                geom=origins,
                base=type_,
                target="mercator"
            ),
            dtype=np.float
        )
        destinations = np.array(
            csys.convert(
                geom=destinations,
                base=type_,
                target="mercator"
            ),
            dtype=np.float
        )

        dists = self.DISTANCE_UNITS[unit](
            meters=self.GEO_FUNCTIONS[metric](origins, destinations)
        )

        if isinstance(digit, int):
            dists = np.round(dists, digit)

        return np.where((np.isinf(dists) | np.isnan(dists)), None, dists).tolist()

    def trip_distance(self,
                      origins: list,
                      destinations: list,
                      metric: str = "driving",
                      digit: int = None,
                      return_duration: bool = False,
                      return_timestamp: bool = False,
                      unit: str = "m",
                      duration_unit: str = "s",
                      **kwargs
                      ):
        """

        Parameters
        ----------
        origins
        destinations
        metric
        digit
        return_duration
        return_timestamp
        unit
        duration_unit

        Returns
        -------

        """
        if not isinstance(origins, (np.ndarray, list, tuple)):
            raise ValueError("origins parameter must be list/tuple/Numpy type!")
        if not isinstance(destinations, (np.ndarray, list, tuple)):
            raise ValueError("destinations parameter must be list/tuple/Numpy type!")
        if not isinstance(metric, str) or metric not in self.TRIP_FUNCTIONS.keys():
            raise ValueError(
                f"metric parameter is must str type and only support "
                f"{'/'.join(list(self.DISTANCE_UNITS.keys()))}!"
            )
        if not isinstance(unit, str) or unit not in self.DISTANCE_UNITS.keys():
            raise ValueError(
                f"unit parameter is must str type and only support "
                f"{'/'.join(list(self.DISTANCE_UNITS.keys()))}!"
            )
        if not isinstance(duration_unit, str) or duration_unit not in self.TIME_UNITS.keys():
            raise ValueError(
                f"duration_unit parameter is must str type and only support "
                f"{'/'.join(list(self.TIME_UNITS.keys()))}!"
            )

        origins = np.array(origins, dtype=np.float)
        destinations = np.array(destinations, dtype=np.float)

        dists, durations, times = self.TRIP_FUNCTIONS[metric](
            origins, destinations, kwargs.get("aks", self.BAIDU_AKS)
        )

        dists = self.DISTANCE_UNITS[unit](meters=dists)
        durations = self.TIME_UNITS[duration_unit](seconds=durations)

        if isinstance(digit, int):
            dists = np.round(dists, digit)
            durations = np.round(durations, digit)

        dists = np.where((np.isinf(dists) | np.isnan(dists)), None, dists).tolist()
        durations = np.where((np.isinf(durations) | np.isnan(durations)), None, durations).tolist()

        if return_duration and return_timestamp:
            return dists, durations, times
        elif not return_duration and return_timestamp:
            return dists, times
        elif return_duration and not return_timestamp:
            return dists, durations
        else:
            return dists,


distances = Distances()
