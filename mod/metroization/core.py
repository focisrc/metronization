# Copyright (C) 2018 Chi-kwan Chan
# Copyright (C) 2018 Steward Observatory
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

import numpy as np

from skimage.morphology import skeletonize

def rebin(img, shape=[32, 32]):
    reshape = (shape[0], img.shape[0]//shape[0],
               shape[1], img.shape[1]//shape[1])
    return img.reshape(reshape).max(-1).max(1)

def scale_threshold(img, threshold=0.5):
    threshold *= np.sum(img)
    s = np.sort(img.flatten())
    i = np.searchsorted(np.cumsum(s), threshold, side="left")
    return s[i]

def metroize(img, mgrid=32, threshold=0.5):
    threshold = scale_threshold(img, threshold=threshold)
    img = skeletonize(img > threshold)
    img = skeletonize(rebin(img, [mgrid, mgrid]) > 0)
    return img
