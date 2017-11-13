#!/usr/bin/env python
"""
    This script calculate matrix determinant

"""

import numpy.random as nm
from itertools import permutations
from math import factorial


class Matrix(object):
    """Class matrix container"""
    def __init__(self, dimension=4):
        self.dimension = dimension
        self.matrix = nm.random_integers(-5, 5, (dimension, dimension))
        self.determinant = None

    def show_matrix(self):
        """Just shows input matrix that we have"""
        print str(self.matrix)

    def calculate_inversion(self, permutation):
        """Calculate inversion of given permutation"""
        inversion = 0
        for index in range(0,len(permutation)):
            inversion += len(filter(lambda x: x < permutation[index], permutation[index+1:]))
        return inversion

    def calculate_determinant(self):
        """Main calculations located there"""
        permutation = permutations(range(self.dimension))
        e = 0
        for iteration in range(factorial(self.dimension)):
            term = 1
            permut = permutation.next()
            for i in range(self.dimension):
                term *= self.matrix[i][permut[i]]
            e += (-1)**self.calculate_inversion(permut)*term
        self.determinant = e
        print e


if __name__ == "__main__":
    x = Matrix()
    x.show_matrix()
    x.calculate_determinant()
