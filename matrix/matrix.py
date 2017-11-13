#!/usr/bin/env python
"""
    This script calculate matrix determinant

"""

import numpy.random as nm


class Matrix(object):
    """Class matrix container"""
    def __init__(self, dimension=5):
        self.matrix = nm.random_integers(-5, 5, (dimension, dimension))

    def show_matrix(self):
        """Just shows what we have"""
        print str(self.matrix)

    def calculate_inversion(self, permutation):
        """Calculate inversion of given permutation"""
        inversion = 0
        for index in range(0,len(permutation)):
            inversion += len(filter(lambda x: x < permutation[index], permutation[index+1:]))
        return inversion

if __name__ == "__main__":
    x = Matrix()
    x.show_matrix()
    perm = nm.random_integers(0, 5, 5)
    print perm
    print x.calculate_inversion(perm)
