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
# Create: 2021-11-1

import geocoding


class TestUnits(object):
    def test_km(self):
        print(geocoding.units.km(kilometers=10))
        print(geocoding.units.km(meters=10))
        print(geocoding.units.km(miles=10))
        print(geocoding.units.km(feet=10))
        print(geocoding.units.km(nautical=10))

    def test_m(self):
        print(geocoding.units.m(kilometers=10))
        print(geocoding.units.m(meters=10))
        print(geocoding.units.m(miles=10))
        print(geocoding.units.m(feet=10))
        print(geocoding.units.m(nautical=10))

    def test_mi(self):
        print(geocoding.units.mi(kilometers=10))
        print(geocoding.units.mi(meters=10))
        print(geocoding.units.mi(miles=10))
        print(geocoding.units.mi(feet=10))
        print(geocoding.units.mi(nautical=10))

    def test_ft(self):
        print(geocoding.units.ft(kilometers=10))
        print(geocoding.units.ft(meters=10))
        print(geocoding.units.ft(miles=10))
        print(geocoding.units.ft(feet=10))
        print(geocoding.units.ft(nautical=10))

    def test_nm(self):
        print(geocoding.units.nm(kilometers=10))
        print(geocoding.units.nm(meters=10))
        print(geocoding.units.nm(miles=10))
        print(geocoding.units.nm(feet=10))
        print(geocoding.units.nm(nautical=10))

    def test_rad(self):
        print(geocoding.units.rad(degrees=10))
        print(geocoding.units.rad(radians=10))
        print(geocoding.units.rad(arcminutes=10))
        print(geocoding.units.rad(arcseconds=10))

    def test_arcmin(self):
        print(geocoding.units.arcmin(degrees=10))
        print(geocoding.units.arcmin(radians=10))
        print(geocoding.units.arcmin(arcminutes=10))
        print(geocoding.units.arcmin(arcseconds=10))

    def test_arcsec(self):
        print(geocoding.units.arcsec(degrees=10))
        print(geocoding.units.arcsec(radians=10))
        print(geocoding.units.arcsec(arcminutes=10))
        print(geocoding.units.arcsec(arcseconds=10))

    def test_years(self):
        print(geocoding.units.years(years=10))
        print(geocoding.units.years(weeks=10))
        print(geocoding.units.years(days=10))
        print(geocoding.units.years(hours=10))
        print(geocoding.units.years(minutes=10))
        print(geocoding.units.years(seconds=10))

    def test_weeks(self):
        print(geocoding.units.weeks(years=10))
        print(geocoding.units.weeks(weeks=10))
        print(geocoding.units.weeks(days=10))
        print(geocoding.units.weeks(hours=10))
        print(geocoding.units.weeks(minutes=10))
        print(geocoding.units.weeks(seconds=10))

    def test_days(self):
        print(geocoding.units.days(years=10))
        print(geocoding.units.days(weeks=10))
        print(geocoding.units.days(days=10))
        print(geocoding.units.days(hours=10))
        print(geocoding.units.days(minutes=10))
        print(geocoding.units.days(seconds=10))

    def test_hours(self):
        print(geocoding.units.hours(years=10))
        print(geocoding.units.hours(weeks=10))
        print(geocoding.units.hours(days=10))
        print(geocoding.units.hours(hours=10))
        print(geocoding.units.hours(minutes=10))
        print(geocoding.units.hours(seconds=10))

    def test_minutes(self):
        print(geocoding.units.minutes(years=10))
        print(geocoding.units.minutes(weeks=10))
        print(geocoding.units.minutes(days=10))
        print(geocoding.units.minutes(hours=10))
        print(geocoding.units.minutes(minutes=10))
        print(geocoding.units.minutes(seconds=10))

    def test_seconds(self):
        print(geocoding.units.seconds(years=10))
        print(geocoding.units.seconds(weeks=10))
        print(geocoding.units.seconds(days=10))
        print(geocoding.units.seconds(hours=10))
        print(geocoding.units.seconds(minutes=10))
        print(geocoding.units.seconds(seconds=10))
