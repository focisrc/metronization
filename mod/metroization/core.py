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

import numpy as np

from skimage.morphology import skeletonize

from .utils import rebin, scale_threshold
from .viz   import metroplot
from .tda   import tda

def metroize(img, ngrid, threshold=0.5, plot=False, axes=None):

    if axes is not None:
        plot = True

    if plot:
        if axes is None:
            import ehtplot
            from matplotlib import pyplot as plt
            fig, axes = plt.subplots(2,3, figsize=(12,8))

        axes[0][0].imshow(img.T, origin='lower', cmap='afmhot_10u', interpolation=None)
        axes[0][0].set_title('0. Original')

    img = img > scale_threshold(img, threshold=threshold)
    if plot:
        axes[0][1].imshow(img.T, origin='lower', cmap='gray_r', interpolation=None)
        axes[0][1].set_title('1. Robust Thresholding')

    img = skeletonize(img)
    if plot:
        axes[0][2].imshow(img.T, origin='lower', cmap='gray_r', interpolation=None)
        axes[0][2].set_title('2. Skeleton')

    img = rebin(img, [ngrid, ngrid]) > 0
    if plot:
        axes[1][0].imshow(img.T, origin='lower', cmap='gray_r', interpolation=None)
        axes[1][0].set_title('3. Max Pooling')

    img = skeletonize(img)
    if plot:
        axes[1][1].imshow(img.T, origin='lower', cmap='gray_r', interpolation=None)
        axes[1][1].set_title('4. Reskeleton')

        metroplot(axes[1][2], img)
        axes[1][2].set_title('5. Metroize')

    return np.array(np.where(img)).T

def topo(img, ngrid, plength, hlength, plot=False, axes=None):

    if axes is not None:
        plot = True

    if plot:
        if axes is None:
            from matplotlib import pyplot as plt
            fig, axes = plt.subplots(1,2, figsize=(12,6))
            axes[0].axvline(x=plength)
            axes[1].axvline(x=hlength)

    out = {}

    for i, t in enumerate(np.linspace(0, 1, 10, endpoint=False)):
        pts    = metroize(img, ngrid, t).astype(float)
        p, h   = tda(pts, plot=plot, axes=axes, color=f'C{i}', alpha=0.5)
        out[t] = (np.count_nonzero(p > plength),
                  np.count_nonzero(h > hlength))

    return out
