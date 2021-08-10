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

import sys

sys.path.append("../")

from geocoding import converter


class TestConverter(object):
    def test_gcj02_to_wgs84(self):
        assert converter.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="gcj02",
            target="wgs84"
        )

    def test_wgs84_to_gcj02(self):
        assert converter.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="wgs84",
            target="gcj02"
        )

    def test_bd09_to_gcj02(self):
        assert converter.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="bd09",
            target="gcj02"
        )

    def test_gcj02_to_bd09(self):
        assert converter.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="gcj02",
            target="bd09"
        )

    def test_bd09_to_wgs84(self):
        assert converter.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="bd09",
            target="wgs84"
        )

    def test_wgs84_to_bd09(self):
        assert converter.convert(
            geom=(
                (116.403963, 39.915119),
                (116.191704, 39.942046),
                (121.394202, 31.172559)
            ),
            base="wgs84",
            target="bd09"
        )
