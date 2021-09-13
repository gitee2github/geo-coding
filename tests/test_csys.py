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

import geocoding


class TestCSYS(object):
    def test_gcj02_to_wgs84(self):
        assert geocoding.csys.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="gcj02",
            target="wgs84"
        )

    def test_wgs84_to_gcj02(self):
        assert geocoding.csys.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="wgs84",
            target="gcj02"
        )

    def test_bd09_to_gcj02(self):
        assert geocoding.csys.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="bd09",
            target="gcj02"
        )

    def test_gcj02_to_bd09(self):
        assert geocoding.csys.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="gcj02",
            target="bd09"
        )

    def test_bd09_to_wgs84(self):
        assert geocoding.csys.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="bd09",
            target="wgs84"
        )

    def test_wgs84_to_bd09(self):
        assert geocoding.csys.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="wgs84",
            target="bd09"
        )

    def test_wgs84_to_mercator(self):
        assert geocoding.csys.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="wgs84",
            target="mercator"
        )

    def test_mercator_to_wgs84(self):
        assert geocoding.csys.convert(
            geom=(
                (12958029.887478903, 4853615.260825298),
                (12934401.323682614, 4857524.133866013),
                (13513540.751895629, 3655179.550619312)
            ),
            base="mercator",
            target="wgs84"
        )

    def test_bd09_to_mercator(self):
        assert geocoding.csys.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="bd09",
            target="mercator"
        )

    def test_mercator_to_bd09(self):
        assert geocoding.csys.convert(
            geom=(
                (12958029.887478903, 4853615.260825298),
                (12934401.323682614, 4857524.133866013),
                (13513540.751895629, 3655179.550619312)
            ),
            base="mercator",
            target="bd09"
        )

    def test_gcj02_to_mercator(self):
        assert geocoding.csys.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="gcj02",
            target="mercator"
        )

    def test_mercator_to_gcj02(self):
        assert geocoding.csys.convert(
            geom=(
                (12958029.887478903, 4853615.260825298),
                (12934401.323682614, 4857524.133866013),
                (13513540.751895629, 3655179.550619312)
            ),
            base="mercator",
            target="gcj02"
        )
