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
from .utils import parameter_check

__all__ = ["csys"]


def _transform(matrix):
    """
    Latitude and longitude conversion component

    :param matrix:
    :return:
    """
    return np.array([
        np.sum([
            300.0 + matrix[:, 0] + 2.0 * matrix[:, 1] + 0.1 * matrix[:, 0] * matrix[:, 0] +
            0.1 * matrix[:, 0] * matrix[:, 1] + 0.1 * np.sqrt(np.abs(matrix[:, 0])),
            (20.0 * np.sin(6.0 * matrix[:, 0] * np.pi) + 20.0 * np.sin(2.0 * matrix[:, 0] * np.pi)) * 2.0 / 3.0,
            (20.0 * np.sin(matrix[:, 0] * np.pi) + 40.0 * np.sin(matrix[:, 0] / 3.0 * np.pi)) * 2.0 / 3.0,
            (150.0 * np.sin(matrix[:, 0] / 12.0 * np.pi) + 300.0 * np.sin(matrix[:, 0] / 30.0 * np.pi)) * 2.0 / 3.0
        ], axis=0),
        np.sum([
            -100.0 + 2.0 * matrix[:, 0] + 3.0 * matrix[:, 1] + 0.2 * matrix[:, 1] * matrix[:, 1] +
            0.1 * matrix[:, 0] * matrix[:, 1] + 0.2 * np.sqrt(np.abs(matrix[:, 0])),
            (20.0 * np.sin(6.0 * matrix[:, 0] * np.pi) + 20.0 * np.sin(2.0 * matrix[:, 0] * np.pi)) * 2.0 / 3.0,
            (20.0 * np.sin(matrix[:, 1] * np.pi) + 40.0 * np.sin(matrix[:, 1] / 3.0 * np.pi)) * 2.0 / 3.0,
            (160.0 * np.sin(matrix[:, 1] / 12.0 * np.pi) + 320 * np.sin(matrix[:, 1] * np.pi / 30.0)) * 2.0 / 3.0
        ], axis=0)
    ]).T


@parameter_check(ndim=2)
def bd09_to_gcj02(bd_matrix):
    """
    Baidu BD09 coordinates to National Bureau of Metrology and Measurement

    :param bd_matrix:
    :return:
    """
    x, y, = bd_matrix[:, 0] - 0.0065, bd_matrix[:, 1] - 0.006
    z = (np.sqrt(x * x + y * y)) - (0.00002 * np.sin(y * (np.pi * 3000.0 / 180.0)))
    theta = np.arctan2(y, x) - 0.000003 * np.cos(x * (np.pi * 3000.0 / 180.0))

    return np.array([
        z * np.cos(theta),
        z * np.sin(theta)
    ]).T


@parameter_check(ndim=2)
def gcj02_to_bd09(gcj_matrix):
    """
    National Bureau of Surveying and Measurement to Baidu BD09 coordinates

    :param gcj_matrix:
    :return:
    """
    z = np.sqrt(np.square(gcj_matrix[:, 0]) + np.square(gcj_matrix[:, 1])) + 0.00002 * np.sin(
        gcj_matrix[:, 1] * (np.pi * 3000.0 / 180.0))
    theta = np.arctan2(gcj_matrix[:, 1], gcj_matrix[:, 0]) + 0.000003 * np.cos(
        gcj_matrix[:, 0] * (np.pi * 3000.0 / 180.0))

    return np.array([
        z * np.cos(theta) + 0.0065,
        z * np.sin(theta) + 0.006
    ]).T


@parameter_check(ndim=2)
def gcj02_to_wgs84(gcj_matrix):
    """
    National Bureau of Survey and Measurement Coordinates to WGS-84 Coordinates

    :param gcj_matrix:
    :return:
    """
    transform_gcj_matrix = _transform(
        np.array(
            [gcj_matrix[:, 0] - 105.0,
             gcj_matrix[:, 1] - 35.0]
        ).T
    )
    rad_lat = gcj_matrix[:, 1] / 180.0 * np.pi
    magic = 1 - 0.00669342162296594323 * np.square(np.sin(rad_lat))
    sqrt_magic = np.sqrt(magic)

    return np.array([
        gcj_matrix[:, 0] - (
                (transform_gcj_matrix[:, 0] * 180.0) / (6378245.0 / sqrt_magic * np.cos(rad_lat) * np.pi)),
        gcj_matrix[:, 1] - ((transform_gcj_matrix[:, 1] * 180.0) / (
                (6378245.0 * (1 - 0.00669342162296594323)) / (magic * sqrt_magic) * np.pi))
    ]).T


@parameter_check(ndim=2)
def wgs84_to_gcj02(wgs_matrix):
    """
    WGS-84 Coordinates to National Bureau of Survey and Measurement Coordinates

    :param wgs_matrix:
    :return:
    """
    transform_wgs_matrix = _transform(
        np.array([
            wgs_matrix[:, 0] - 105.0,
            wgs_matrix[:, 1] - 35.0]
        ).T
    )
    rad_lat = wgs_matrix[:, 1] / 180.0 * np.pi
    magic = 1.0 - 0.00669342162296594323 * np.square(np.sin(rad_lat))
    sqrt_magic = np.sqrt(magic)

    return np.array([
        wgs_matrix[:, 0] + (
                (transform_wgs_matrix[:, 0] * 180.0) / (6378245.0 / sqrt_magic * np.cos(rad_lat) * np.pi)),
        wgs_matrix[:, 1] + ((transform_wgs_matrix[:, 1] * 180.0) / (
                (6378245.0 * (1 - 0.00669342162296594323)) / (magic * sqrt_magic) * np.pi))
    ]).T


@parameter_check(ndim=2)
def bd09_to_wgs84(bd_matrix):
    """
    Baidu BD09 standard to WGS-84 coordinates

    :param bd_matrix:
    :return:
    """
    return gcj02_to_wgs84(
        bd09_to_gcj02(bd_matrix)
    )


@parameter_check(ndim=2)
def wgs84_to_bd09(wgs_matrix):
    """
    WGS-84 coordinates to Baidu BD09 coordinates

    :param wgs_matrix:
    :return:
    """
    return gcj02_to_bd09(
        wgs84_to_gcj02(wgs_matrix)
    )


@parameter_check(ndim=2)
def wgs84_to_mercator(wgs_matrix):
    """
    WGS-84 coordinates to Mercator coordinates

    :param wgs_matrix:
    :return:
    """
    return np.array([
        wgs_matrix[:, 0] * 20037508.342789 / 180.0,
        np.log(np.tan((90.0 + wgs_matrix[:, 1]) * np.pi / 360.0)) / (np.pi / 180.0) * 20037508.34789 / 180.0
    ]).T


@parameter_check(ndim=2)
def mercator_to_wgs84(mer_matrix):
    """
    Mercator coordinates WGS-84 coordinates

    :param mer_matrix:
    :return:
    """
    return np.array([
        mer_matrix[:, 0] / 20037508.34789 * 180.0,
        180.0 / np.pi * (2 * np.arctan(np.exp(mer_matrix[:, 1] / 20037508.34789 * 180.0 * np.pi / 180.0)) - np.pi / 2.0)
    ]).T


@parameter_check(ndim=2)
def bd09_to_mercator(bd_matrix):
    """
    Baidu BD09 coordinates to Mercator coordinates

    :param bd_matrix:
    :return:
    """
    return wgs84_to_mercator(
        bd09_to_wgs84(bd_matrix)
    )


@parameter_check(ndim=2)
def mercator_to_bd09(mer_matrix):
    """
    Mercator coordinates Baidu BD09 coordinates

    :param mer_matrix:
    :return:
    """
    return wgs84_to_bd09(
        mercator_to_wgs84(mer_matrix)
    )


@parameter_check(ndim=2)
def gcj02_to_mercator(gcj_matrix):
    """
    National Bureau of Survey and Measurement coordinates to Mercator coordinates

    :param gcj_matrix:
    :return:
    """
    return wgs84_to_mercator(
        gcj02_to_wgs84(gcj_matrix)
    )


@parameter_check(ndim=2)
def mercator_to_gcj02(mer_matrix):
    """
    Mercator coordinates to National Bureau of Survey and Measurement coordinates

    :param mer_matrix:
    :return:
    """
    return wgs84_to_gcj02(
        mercator_to_wgs84(mer_matrix)
    )


class CoordinateSystem(object):
    def __init__(self):
        self.FUNCTIONS = {
            ("bd09", "gcj02"): bd09_to_gcj02,
            ("bd09", "wgs84"): bd09_to_wgs84,
            ("bd09", "mercator"): bd09_to_mercator,
            ("gcj02", "bd09"): gcj02_to_bd09,
            ("gcj02", "wgs84"): gcj02_to_wgs84,
            ("gcj02", "mercator"): gcj02_to_mercator,
            ("wgs84", "bd09"): wgs84_to_bd09,
            ("wgs84", "gcj02"): wgs84_to_gcj02,
            ("wgs84", "mercator"): wgs84_to_mercator,
            ("mercator", "bd09"): mercator_to_bd09,
            ("mercator", "gcj02"): mercator_to_gcj02,
            ("mercator", "wgs84"): mercator_to_wgs84
        }

    def convert(self, geom, base: str, target: str, digit: int = None):
        """

        :param digit:
        :param geom:
        :param base:
        :param target:
        :return:
        """
        if isinstance(geom, (np.ndarray, list, tuple)):
            geom = np.array(geom, dtype=np.float)
        else:
            raise ValueError("geom parameter must be list type or Numpy type!")

        if not isinstance(base, str):
            raise ValueError("base parameter is must str type!")

        if not isinstance(target, str):
            raise ValueError("target parameter is must str type!")

        function = self.FUNCTIONS.get((base, target), None)
        res = [] if function is None else function(geom)

        if isinstance(digit, int):
            res = np.round(res, digit)

        return np.where((np.isinf(res) | np.isnan(res)), None, res).tolist()


csys = CoordinateSystem()
