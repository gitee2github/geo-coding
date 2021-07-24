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

"""The setup script."""
import os
from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst", "r", encoding="utf-8") as history_file:
    history = history_file.read()

dir_ = os.path.dirname(os.path.abspath(__file__))
requirements = open(os.path.join(dir_, "requirements.txt"), "r", encoding="utf-8").read().splitlines()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="61Duke",
    author_email='61duke@isrc.iscas.ac.cn',
    python_requires='>=3.*.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mulan PSL v2',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="",
    entry_points={
        'console_scripts': [
            '*=geocoding.cli:main',
        ],
    },
    install_requires=requirements,
    license="Mulan PSL v2",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='geocoding',
    name='geocoding',
    packages=find_packages(include=['geo-coding', 'geocoding.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://gitee.com/weihaitong/geo-coding',
    version='0.0.1',
    zip_safe=False,
)
