# Copyright (C) 2020 Pierre Christian
# Copyright (C) 2020 Steward Observatory
#
# This file is part of `metronization`.
#
# `Metronization` is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# `Metronization` is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with `metronization`.  If not, see <http://www.gnu.org/licenses/>.

import numpy    as np
import dionysus as d

def pull(dgm, verbose=True):

    births = np.array([pt.birth for pt in dgm])
    deaths = np.array([pt.death for pt in dgm])

    if verbose:
        print(births)
        print(deaths)
        print(deaths - births)

    return births, deaths

def tda(pts, plot=False, axes=None, verbose=False, **kwargs):

    f = d.fill_rips(pts, 2, 10)
    p = d.homology_persistence(f)
    dgms = d.init_diagrams(p, f)

    if axes is not None:
        plot = True

    if plot:
        if axes is None:
            from matplotlib import pyplot as plt
            fig, axes = plt.subplots(1,2, figsize=(12,6))

        for i in range(2):
            try:
                d.plot.plot_bars(dgms[i], ax=axes[i], **kwargs)
            except:
                print("Metronize output not TDA-able with Betti number", i)

    try:
        points = pull(dgms[0], verbose=verbose)
    except:
        points = np.array([]), np.array([])

    try:
        holes  = pull(dgms[1], verbose=verbose)
    except:
        holes  = np.array([]), np.array([])

    return points, holes

def count(births, deaths, lifespan=1,
          birth=None, lower=None,
          death=None, upper=None):

    ok = True

    if birth    is not None: ok &= births          <= birth
    if lower    is not None: ok &= births          >= lower
    if lifespan is not None: ok &= deaths - births >= lifespan
    if death    is not None: ok &= deaths          >= death
    if upper    is not None: ok &= deaths          <= upper

    return np.count_nonzero(ok)
