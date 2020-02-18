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

import numpy    as np
import dionysus as d

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

def tda(pts, plot=False, verbose=False):

    f = d.fill_rips(pts, 2, 10)
    p = d.homology_persistence(f)
    dgms = d.init_diagrams(p, f)

    if plot:
        from matplotlib import pyplot as plt
        fig, axes = plt.subplots(1,2, figsize=(12,6))
        d.plot.plot_bars(dgms[0], ax=axes[0])
        try:
            d.plot.plot_bars(dgms[1], ax=axes[1])
        except:
            print("Metroize output not TDA-able")

    points = pull(dgms[0], verbose=verbose)
    holes  = pull(dgms[1], verbose=verbose)

    return points, holes
