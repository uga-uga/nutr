# This file is part of nutr.

# nutr is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# nutr is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with nutr.  If not, see <https://www.gnu.org/licenses/>.

# Copyright (C) 2020 Udo Friman-Gayer

from pathlib import Path
import os
os.chdir('@ANGCORR_PYTHON_DIR@')
from time import time

from asymmetry_plot import AngularCorrelation, AsymmetryPlotter
import state as st
import transition as tr

t_start = time()

ang_cor = AngularCorrelation(
    st.State(0, st.POSITIVE),
    [
        [tr.Transition(tr.MAGNETIC, 2, tr.ELECTRIC, 4, 0.), st.State(2, st.POSITIVE)],
        [tr.Transition(tr.EM_UNKNOWN, 2, tr.EM_UNKNOWN, 4, 0.), st.State(2, st.PARITY_UNKNOWN)],
    ],
    [0., 'delta_1']
)

arctan_deltas, asy_45, asy_90 = ang_cor.asymmetry_grid(n_delta_steps=101)

asy_plo = AsymmetryPlotter(ang_cor, arctan_deltas, asy_45, asy_90, scale_asymmetries=True)

output_file_single_2d = Path('@PROJECT_BINARY_DIR@') / 'test_plot_02_mixing_single_asy_2d.pdf'
asy_plo.plot_single_2d(r'$\delta_2$', [r'$\delta_1 = 0$', r'$\delta_2$'], False, output_file_single_2d)

output_file_single_3d = Path('@PROJECT_BINARY_DIR@') / 'test_plot_02_mixing_single_asy_3d.pdf'
asy_plo.plot_single_3d(r'$\delta_2$', output_file_single_3d)

output_file_contour = Path('@PROJECT_BINARY_DIR@') / 'test_plot_02_mixing_single_asy_contour.pdf'
asy_plo.plot_double_contour([r'$\delta_1 = 0$', r'$\delta_2$'], output_file_contour)

print('Created output files \n\'{}\',\n\'{}\',\n and \'{}\'.\nExecution took {:4.2f} seconds.'.format(output_file_single_2d, output_file_single_3d, output_file_contour, time() - t_start))