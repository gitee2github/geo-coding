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
# Create: 2021-7-6

from decorator import decorator
import requests
import numpy as np
import threading
from retrying import retry


@decorator
def parameter_check(func, ndim=2, *args, **kwargs):
    """
    Decorator tool to check the parameters of the input matrix

    Parameters
    ----------
    func
    ndim
    args
    kwargs

    Returns
    -------

    """
    geom, *_ = args

    if not isinstance(geom, np.ndarray):
        raise ValueError("matrix parameter is not Numpy type!")
    if not geom.ndim == ndim:
        raise ValueError("matrix parameter must 2-d array")

    return func(*args, **kwargs)


class RequestsRetrying(object):
    """
    A request wrapper class with a retry mechanism added, singleton pattern

    version 0.0.1 only provides the GET method
    """
    _instance_lock = threading.Lock()

    @retry(stop_max_attempt_number=3)
    def get_retrying(self, url, headers=None, cookies=None, files=None,
                     auth=None, timeout=None, allow_redirects=True, proxies=None,
                     hooks=None, stream=None, verify=None, cert=None, json=None):
        response = requests.get(
            url, headers=headers, cookies=cookies, files=files,
            auth=auth, timeout=timeout, allow_redirects=allow_redirects, proxies=proxies,
            hooks=hooks, stream=stream, verify=verify, cert=cert, json=json
        ).json()
        return response

    def __new__(cls, *args, **kwargs):
        if not hasattr(RequestsRetrying, "_instance"):
            with RequestsRetrying._instance_lock:
                if not hasattr(RequestsRetrying, "_instance"):
                    RequestsRetrying._instance = object.__new__(cls)
        return RequestsRetrying._instance
