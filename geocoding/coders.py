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

from urllib.request import urlopen
from urllib.parse import quote
import json

__all__ = ["coders"]


class Coders(object):
    """
    Every geolocation service you might use (eg Baidu Maps, Google Maps) has its own class
    in geocoding.coders that abstracts the service's API.
    Each geocoder defines methods for geographic queries,
    parsing a location from a string,
    and can also parse a pair of coordinates into an address.
    Each geocoder accepts during initialization any credentials or
    settings it needs to interact with its service, such as API keys or locales.
    """

    def baidu(self, locations=None, addresses=None, key=""):
        """
        Geocoding using Baidu Maps API.

        File address:
        http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding

        Parameters
        ----------
        locations: latitude and longitude coordinate string
        addresses: location string
        key: AK

        Returns
        -------
        >>> import geocoding
        >>> geocoding.coders.baidu(
        >>>    locations=["34.542206,111.114859"],
        >>>    key="NmEa3KGWumDMGNupPOGG6m9xxBGoLTRx"
        >>> )
        {
            '34.542206,111.114859': {
                'address': '河南省三门峡市灵宝市',
                'country': '中国',
                'province': '河南省',
                'city': '三门峡市',
                'town': '',
                'district': '灵宝市',
                'street': '',
                'streetNumber': '',
                'lng': '34.542206',
                'lat': '111.114859'
            }
        }
        >>> import geocoding
        >>> geocoding.coders.baidu(
        >>>    addresses=["天安门"],
        >>>    key="k936lbWYFPwG1LEoKb9faZ8MEizFwh60"
        >>> )
        {
            '天安门': {
                'address': '天安门',
                'lng': 116.40396298757886,
                'lat': 39.91511908708907
            }
        }
        """
        results = {}

        def __request(url):
            """
            BAIDU api request processing

            Parameters
            ----------
            url

            Returns
            -------

            """
            try:
                res = json.loads(urlopen(url=url).read().decode())
                if res.get("status") != 0:
                    raise ConnectionError(f"Error: URL({url}): {res.get('message')}!")
            except Exception as e:
                res = {}
                print(e)
            return res

        if locations:
            # accept multi-locations
            for location in locations:
                if location in results.keys():
                    continue

                url = 'http://api.map.baidu.com/reverse_geocoding/v3/?location=' + location + "&output=json&ak=" + key
                response = __request(url=url)
                results[location] = {
                    "address": response.get("result", {}).get("formatted_address"),
                    "country": response.get("result", {}).get("addressComponent", {}).get("country"),
                    "province": response.get("result", {}).get("addressComponent", {}).get("province"),
                    "city": response.get("result", {}).get("addressComponent", {}).get("city"),
                    "town": response.get("result", {}).get("addressComponent", {}).get("town"),
                    "district": response.get("result", {}).get("addressComponent", {}).get("district"),
                    "street": response.get("result", {}).get("addressComponent", {}).get("street"),
                    "streetNumber": response.get("result", {}).get("addressComponent", {}).get("street_number"),
                    "lng": location.split(",")[0],
                    "lat": location.split(",")[1]
                }
        if addresses:
            # accept multi-addresses
            for address in addresses:
                if address in results.keys():
                    continue

                url = 'http://api.map.baidu.com/geocoder/v2/?address=' + quote(address) + "&output=json&ak=" + key
                response = __request(url=url)
                results[address] = {
                    "address": address,
                    "lng": response.get("result", {}).get("location", {}).get("lng"),
                    "lat": response.get("result", {}).get("location", {}).get("lat")
                }
        return results

    def gaode(self, locations=None, addresses=None, key=""):
        """
        Geocoding using GaoDe Maps API.

        File address:
        https://lbs.amap.com/api/webservice/guide/api/georegeo

        Parameters
        ----------
        locations: latitude and longitude coordinate string
        addresses: location string
        key: AK

        Returns
        -------
        >>> import geocoding
        >>> geocoding.coders.gaode(
        >>>    locations=["116.397499,39.908722", "111.114859,34.542206"],
        >>>    addresses=["天安门"],
        >>>    key="db459b3dbc90afaef32dec46d228077e"
        >>> )
        {
            '116.397499,39.908722': {
                'address': '北京市东城区东华门街道天安门',
                'country': '中国',
                'province': '北京市',
                'city': [],
                'district': '东城区',
                'town': '东华门街道',
                'street': '南河沿大街',
                'streetNumber': '69号',
                'lng': '39.908722',
                'lat': '116.397499'
            },
            '111.114859,34.542206': {
                'address': '河南省三门峡市灵宝市阳店镇曲家山',
                'country': '中国',
                'province': '河南省',
                'city': '三门峡市',
                'district': '灵宝市',
                'town': '阳店镇',
                'street': [],
                'streetNumber': [],
                'lng': '34.542206',
                'lat': '111.114859'
            },
            '天安门': {
                'address': '北京市东城区天安门',
                'country': '中国',
                'province': '北京市',
                'city': '北京市',
                'district': '东城区',
                'town': [],
                'street': None,
                'streetNumber': None,
                'lng': '39.908722',
                'lat': '116.397499'
            }
        }
        """
        results = {}

        def _base_request(url):
            try:
                res = json.loads(urlopen(url=url).read().decode())
                if res.get("status") != "1":
                    raise ConnectionError(f"Error: URL({url}): {res.get('info')}!")
            except Exception as e:
                res = {}
                print(e)
            return res

        if locations:
            for location in locations:
                if location in results.keys():
                    continue

                url = 'http://restapi.amap.com/v3/geocode/regeo?extensions=all&location=' + location + "&output=json&key=" + key
                response = _base_request(url=url)
                results[location] = {
                    "address": response.get("regeocode", {}).get("formatted_address"),
                    "country": response.get("regeocode", {}).get("addressComponent", {}).get("country"),
                    "province": response.get("regeocode", {}).get("addressComponent", {}).get("province"),
                    "city": response.get("regeocode", {}).get("addressComponent", {}).get("city"),
                    "district": response.get("regeocode", {}).get("addressComponent", {}).get("district"),
                    "town": response.get("regeocode", {}).get("addressComponent", {}).get("township"),
                    "street": response.get("regeocode", {}).get("addressComponent", {}).get("streetNumber", {}).get(
                        "street"),
                    "streetNumber": response.get("regeocode", {}).get("addressComponent", {})
                        .get("streetNumber", {}).get("number"),
                    "lng": location.split(",")[1],
                    "lat": location.split(",")[0]
                }
        if addresses:
            for address in addresses:
                if address in results.keys():
                    continue
                url = 'http://restapi.amap.com/v3/geocode/geo?address=' + quote(address) + "&key=" + key
                response = _base_request(url=url)
                if not response.get("geocodes"):
                    lat_lng = []
                else:
                    lat_lng = response["geocodes"][0].get("location", "").split(",")

                if len(lat_lng) == 2:
                    lat, lng = lat_lng
                else:
                    lat = lng = None

                results[address] = {
                    "address": response["geocodes"][0].get("formatted_address") if response.get("geocodes") else None,
                    "country": response["geocodes"][0].get("country") if response.get("geocodes") else None,
                    "province": response["geocodes"][0].get("province") if response.get("geocodes") else None,
                    "city": response["geocodes"][0].get("city") if response.get("geocodes") else None,
                    "district": response["geocodes"][0].get("district") if response.get("geocodes") else None,
                    "town": response["geocodes"][0].get("township") if response.get("geocodes") else None,
                    "street": response["geocodes"][0].get("building", {}).get("street") if response.get(
                        "geocodes") else None,
                    "streetNumber": response["geocodes"][0].get("building", {}).get("number") if response.get(
                        "geocodes") else None,
                    "lng": lng,
                    "lat": lat
                }
        return results


coders = Coders()
