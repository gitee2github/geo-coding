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
                for type_ in ("wgs84", "bd09", "gcj02"):
                    dist = geocoding.distances.geo_distance(
                        origins=[[116.403963, 39.915119], [116.403963, 39.915119]],
                        destinations=[[116.191704, 39.942046], [121.394202, 31.172559]],
                        unit=unit,
                        metric=metric,
                        type_=type_,
                        digit=0
                    )
                    print(f"{metric}-{unit}-{type_}: {dist}")

    def test_trip_distance(self):
        import itertools

        is_duration = is_timestamp = (True, False)
        units = ("km", "m")
        duration_units = ("h", "m", "s")

        for rd, rt, u, du in itertools.product(
                is_duration,
                is_timestamp,
                units,
                duration_units
        ):
            dist, *args = geocoding.distances.trip_distance(
                origins=[[116.403963, 39.915119], [116.403963, 39.915119]],
                destinations=[[116.191704, 39.942046], [121.394202, 31.172559]],
                return_duration=rd,
                return_timestamp=rt,
                digit=2,
                unit=u,
                duration_unit=du,
                aks=["k936lbWYFPwG1LEoKb9faZ8MEizFwh60"]
            )
            print(
                f"condition: {(rd, rt, u, du)}, distance: {dist}, duration/timestamp: {args}"
            )
