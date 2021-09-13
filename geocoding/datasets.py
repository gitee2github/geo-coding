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

import os
import pandas as pd

__all__ = ["datasets"]


class DataSets(object):
    def __init__(self):
        self.CURRENT_PATH = os.path.join(os.path.dirname(__file__), "libs")

    def china_provincial_level_administrative_region(self):
        """

        :return:
        """
        return pd.read_json(
            os.path.join(self.CURRENT_PATH, "CHINA_PROVINCIAL_LEVEL_ADMINISTRATIVE_REGION.json")
        )

    def china_prefecture_level_administrative_region(self):
        """

        :return:
        """
        pass

    def china_county_level_administrative_region(self):
        """

        :return:
        """
        pass


datasets = DataSets()
