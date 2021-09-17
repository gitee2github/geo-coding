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
        There are 23 provinces, 5 autonomous regions, 4 municipalities,
        and 2 special administrative regions,
        totaling 34 provincial-level administrative regions.

        The number does not necessarily correspond exactly.
        The data source is GADM: Global Administrative Divisions Database.
        The data on China’s borders provided by it may not conform to China’s
        territorial claims, and the data on provincial, city, and district boundaries
        may not necessarily be the latest version.
        Care must be taken when publishing images that
        use this type of data in official journals.

        :return:

            <class 'pandas.core.frame.DataFrame'>
            Int64Index: 34 entries, 0 to 33
            Data columns (total 8 columns):
             #   Column              Non-Null Count  Dtype
            ---  ------              --------------  -----
             0   GID                 34 non-null     int64
             1   PHONETICIZE_0       34 non-null     object
             2   PHONETICIZE_1       34 non-null     object
             3   TYPE                34 non-null     object
             4   SIMPLIFIED_NAME_0   34 non-null     object
             5   TRADITIONAL_NAME_0  34 non-null     object
             6   EN_ABBREVIATION     34 non-null     object
             7   GEOMETRY            34 non-null     object
            dtypes: int64(1), object(7)
            memory usage: 2.4+ KB
            None

        """
        return pd.read_hdf(
            os.path.join(self.CURRENT_PATH, "CHINA_ADMINISTRATIVE_REGION.h5"),
            key="PROVINCIAL"
        )

    def china_prefecture_level_administrative_region(self):
        """
        There are 293 prefecture-level cities, 7 regions, 30 autonomous prefectures,
        and 3 leagues, totaling 333 prefecture-level divisions.

        The number does not necessarily correspond exactly.
        The data source is GADM: Global Administrative Divisions Database.
        The data on China’s borders provided by it may not conform to China’s
        territorial claims, and the data on provincial, city, and district boundaries
        may not necessarily be the latest version.
        Care must be taken when publishing images that
        use this type of data in official journals.

        :return:

            <class 'pandas.core.frame.DataFrame'>
            Int64Index: 340 entries, 0 to 339
            Data columns (total 9 columns):
             #   Column              Non-Null Count  Dtype
            ---  ------              --------------  -----
             0   GID                 340 non-null    int64
             1   PHONETICIZE_0       340 non-null    object
             2   PHONETICIZE_1       340 non-null    object
             3   TYPE                340 non-null    object
             4   SIMPLIFIED_NAME_0   340 non-null    object
             5   TRADITIONAL_NAME_0  340 non-null    object
             6   SIMPLIFIED_NAME_1   340 non-null    object
             7   TRADITIONAL_NAME_1  340 non-null    object
             8   GEOMETRY            340 non-null    object
            dtypes: int64(1), object(8)
            memory usage: 26.6+ KB
            None

        """
        return pd.read_hdf(
            os.path.join(self.CURRENT_PATH, "CHINA_ADMINISTRATIVE_REGION.h5"),
            key="PREFECTURE"
        )

    def china_county_level_administrative_region(self):
        """
        There are 977 municipal districts, 1303 counties, 393 county-level cities,
        120 autonomous counties, 49 banners, 3 autonomous banners, 1 special zone,
        and 1 forest area, totaling 2,847.

        The number does not necessarily correspond exactly.
        The data source is GADM: Global Administrative Divisions Database.
        The data on China’s borders provided by it may not conform to China’s
        territorial claims, and the data on provincial, city, and district boundaries
        may not necessarily be the latest version.
        Care must be taken when publishing images that
        use this type of data in official journals.

        :return:

            <class 'pandas.core.frame.DataFrame'>
            Int64Index: 2084 entries, 0 to 2083
            Data columns (total 11 columns):
             #   Column              Non-Null Count  Dtype
            ---  ------              --------------  -----
             0   GID                 2084 non-null   int64
             1   PHONETICIZE_0       2084 non-null   object
             2   PHONETICIZE_1       2073 non-null   object
             3   TYPE                2084 non-null   object
             4   SIMPLIFIED_NAME_0   2084 non-null   object
             5   TRADITIONAL_NAME_0  2084 non-null   object
             6   SIMPLIFIED_NAME_1   2084 non-null   object
             7   TRADITIONAL_NAME_1  2084 non-null   object
             8   SIMPLIFIED_NAME_2   2084 non-null   object
             9   TRADITIONAL_NAME_2  2084 non-null   object
             10  GEOMETRY            2084 non-null   object
            dtypes: int64(1), object(10)
            memory usage: 195.4+ KB
            None

        """
        return pd.read_hdf(
            os.path.join(self.CURRENT_PATH, "CHINA_ADMINISTRATIVE_REGION.h5"),
            key="COUNTY"
        )


datasets = DataSets()
