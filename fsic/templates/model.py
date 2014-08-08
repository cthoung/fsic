# -*- coding: utf-8 -*-
"""
___NAME___
___MODULE_DOCSTRING___

"""


import argparse
import os

import numpy as np
from pandas import Series, DataFrame

from fsic import __version__ as version

from fsic.model.model import Model


try:
    from IPython import get_ipython
except:
    def get_ipython():
        return None


class ___MODEL___(Model):
    """___SHORT_DESCRIPTION___

    ___LONG_DESCRIPTION___

    """

    def initialise(self, span, default=0):
        """Initialise the model for solution.

        Parameters
        ==========
        span : list
            The index to set the span of the model (used as the index for
            individual variable Series objects)
        default : float
            Value to initialise variable Series objects with

        Notes
        =====
        Variable-initialisation statements take the form (using the variable C_d
        as an example):
            self.C_d = Series(default, index=span, dtype=np.float64)

        """
        # Store `span` and initialise `iter`
        self.span = span
        self.iter = Series(default, index=span, dtype=np.float64)
        # Initialise model variables
        ___INITIALISE___

    def solve_equations(self, period):
        """Solve the model equations for `period`.

        Parameters
        ==========
        period : Series index
            The identifier of the period to solve

        Notes
        =====
        Equation statements take the form (usng the variable C_s as an example):
            self.C_s[period] = self.C_d[period]

        """
        ___SOLVE_EQUATIONS___

    def get_endogenous_variable_values(self, period):
        """Return the current values of the endogenous variables.

        Parameters
        ==========
        period : Series index
            The identifier of the period to solve

        Returns
        =======
        values : pandas Series
            Endogenous variable values for the current `period`

        Notes
        =====
        Endogenous variable value-extraction statements take the form (using the
        variable C_d as an example):
            values['C_d'] = self.C_d[period]

        """
        values = {}
        ___GET_ENDOGENOUS_VARIABLE_VALUES___
        return Series(values)

    def get_results(self):
        """Return the results from the model solution.

        Parameters
        ==========
        N/A

        Returns
        =======
        results : DataFrame
            Solution results

        Notes
        =====
        The code to form a results DataFrame takes the following form:
            results = DataFrame({
                'C_d': self.C_d,
                'C_s': self.C_s,})

        """
        ___GET_RESULTS___
        results['iter'] = self.iter
        return results


parser = argparse.ArgumentParser(
    description='___SHORT_DESCRIPTION___.',
    fromfile_prefix_chars='@')
parser.add_argument(
    '-V', '--version',
    action='version',
    version=version)

parser.add_argument(
    '-v', '--verbose',
    action='store_true',
    help='print detailed solution output')

parser.add_argument(
    '-o', '--output',
    nargs='+',
    metavar='OUTPUT',
    default=None,
    type=str,
    required=False,
    help='list of output files for model results')


if __name__ == '__main__' and get_ipython() == None:
    args = parser.parse_args()
    # Write results
    if args.output is not None:
        results = model.get_results()
        for o in args.output:
            if o.endswith('.csv'):
                results.to_csv(o)
            else:
                ext = os.path.splitext(o)[1]
                raise ValueError(
                    'Unrecognised output file extension: \'%s\'' % (ext))
