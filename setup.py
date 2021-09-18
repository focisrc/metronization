#!/usr/bin/env python3
#
# Copyright (C) 2018, 2021 Pierre Christian and Chi-kwan Chan
# Copyright (C) 2018, 2021 Fairfield University and Steward Observatory
#
# This file is part of `metroization`.
#
# `Metroization` is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# `Metroization` is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with `metroization`.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name='metroization',
    version='0.1.0',
    url='https://github.com/focisrc/metroization',
    author='Pierre Christian and Chi-kwan Chan',
    author_email='pierre.christian@gmail.com',
    description='Image-domain topological feature extraction',
    packages=find_packages('mod'),
    package_dir={'': 'mod'},
    python_requires='>=3.6', # `metroization` uses python3's f-string and typing
    install_requires=[
        'matplotlib>=2.2.3',
        'numpy>=1.15',
        'scikit-image>=0.14',
        'ehtplot',
        'dionysus',
    ],
)
