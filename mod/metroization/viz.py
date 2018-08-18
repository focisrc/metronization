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

import ehtplot

from matplotlib         import pyplot as plt
from skimage.morphology import skeletonize

from .core import *

def inspect(img, mgrid, threshold):

    fig, axes = plt.subplots(2,3, figsize=(12,8))

    axes[0][0].imshow(img, origin='lower', cmap='afmhot_10u', interpolation=None)
    axes[0][0].set_title('0. Original')

    img = img > scale_threshold(img, threshold=threshold)
    axes[0][1].imshow(img, origin='lower', cmap='gray_r', interpolation=None)
    axes[0][1].set_title('1. Robust Thresholding')

    img = skeletonize(img)
    axes[0][2].imshow(img, origin='lower', cmap='gray_r', interpolation=None)
    axes[0][2].set_title('2. Skeleton')

    img = rebin(img, [mgrid, mgrid]) > 0
    axes[1][0].imshow(img, origin='lower', cmap='gray_r', interpolation=None)
    axes[1][0].set_title('3. Max Pooling')

    img = skeletonize(img)
    axes[1][1].imshow(img, origin='lower', cmap='gray_r', interpolation=None)
    axes[1][1].set_title('4. Reskeleton')

    metroplot(axes[1][2], img)
    axes[1][2].set_title('5. Metroize')
