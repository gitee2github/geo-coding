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
# Create: 2021-12-03


import geocoding


class TestDistances(object):
    def test_geo_distance(self):
        for metric in ("euclidean", "manhattan", "chebyshev", "cosine"):
            for unit in ("km", "m"):
                dist = geocoding.distances.geo_distance(
                    origins=[
                        [12956625.454742264, 4852490.997620595],
                        [12932999.198054729, 4856454.854034764]
                    ],
                    destinations=[
                        [13512293.128253603, 3654686.554857535],
                        [13512293.128253603, 3654686.554857535]
                    ],
                    unit=unit,
                    metric=metric,
                    digit=0
                )
                print(f"{metric}-{unit}: {dist}")
