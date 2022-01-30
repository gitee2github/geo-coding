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
# Create: 2022-1-13


import geocoding


class TestCoders(object):
    def test_baidu(self):
        result = geocoding.coders.baidu(
            locations=["34.542206,111.114859"],
            key="NmEa3KGWumDMGNupPOGG6m9xxBGoLTRx"
        )
        print(result)
        result = geocoding.coders.baidu(
            addresses=["天安门"],
            key="k936lbWYFPwG1LEoKb9faZ8MEizFwh60"
        )
        print(result)

    def test_gaode(self):
        result = geocoding.coders.gaode(
            locations=["116.397499,39.908722", "111.114859,34.542206"],
            addresses=["天安门"],
            key="db459b3dbc90afaef32dec46d228077e"
        )
        print(result)
