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

def metroplot(ax, img, **kwargs):
    s0 = img.shape[0]
    s1 = img.shape[1]
    for i in range(s0):
        for j in range(s1):
            if not img[i,j]:
                continue

            c = 0
            for ii in [i-1,i,i+1]:
                for jj in [j-1,j,j+1]:
                    if ii == i and jj == j:
                        continue
                    if ii < 0 or ii >= s0:
                        continue
                    if jj < 0 or jj >= s1:
                        continue
                    if img[ii,jj]:
                        if ii != i and jj != j:
                            if img[ii,j] or img[i,jj]:
                                continue
                        ax.plot([j+0.5,(jj-j)/2+j+0.5],
                                [i+0.5,(ii-i)/2+i+0.5],
                                color='k')
                        c += 1
            if c == 0:
                ax.plot([j+0.5], [i+0.5], marker='.', color='k')

    ax.set_aspect('equal')

    ax.set_xlim([0, s1])
    ax.set_ylim([0, s0])

    ax.set_xticks(np.arange(0, s1+1, 4))
    ax.set_xticks(np.arange(0, s1+1, 1), minor=True)
    ax.set_yticks(np.arange(0, s0+1, 4))
    ax.set_yticks(np.arange(0, s0+1, 1), minor=True)
    ax.grid(axis='both')
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    ax.tick_params(axis='both', which='both',
                   top=False, bottom=False, labelbottom=False,
                   left=False, right=False, labelleft=False)
