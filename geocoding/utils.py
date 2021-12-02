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
import numpy as np


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
