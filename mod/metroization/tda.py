# Copyright (C) 2020 Pierre Christian
# Copyright (C) 2020 Steward Observatory
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

from matplotlib import pyplot as plt

import dionysus as d

from .core import *

def pull(dgm, verbose=True):

    try:
        births = np.array([pt.birth for pt in dgm])
        deaths = np.array([pt.death for pt in dgm])
    except:
        births = np.array([])
        deaths = np.array([])

    if verbose:
        print(births)
        print(deaths)
        print(deaths - births)

    return deaths - births

def tda(img, plot=True, verbose=True):

    X, Y = np.meshgrid(np.arange(img.shape[0]),
                       np.arange(img.shape[1]), indexing='ij')
    pts = np.vstack((X[img], Y[img])).T.astype('float')

    f = d.fill_rips(pts, 2, 10)
    p = d.homology_persistence(f)
    dgms = d.init_diagrams(p, f)

    if plot:
        fig, axes = plt.subplots(1,4, figsize=(18,4))
        metroplot(axes[0], img)
        axes[1].scatter(pts[:,0], pts[:,1])
        axes[1].set_xlim(-0.5, img.shape[0]-0.5)
        axes[1].set_ylim(-0.5, img.shape[1]-0.5)
        axes[1].set_aspect('equal')
        d.plot.plot_bars(dgms[0], ax=axes[2])
        try:
            d.plot.plot_bars(dgms[1], ax=axes[3])
        except:
            print("Metroize output not TDA-able")

    points = pull(dgms[0], verbose=verbose)
    holes  = pull(dgms[1], verbose=verbose)

    return points, holes
