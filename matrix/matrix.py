#!/usr/bin/env python
"""
    This script calculate matrix determinant

"""


from itertools import permutations
from math import factorial
import numpy as np
import os


class Matrix(object):
    """Class that encapsulate methods to contain matrix and perform
    operations on it
    """
    def __init__(self, dimension=4, matrix_file=''):
        self.dimension = dimension
        self._determinant = None

        if file != '':
            self.matrix = self._read_matrix_from_file(matrix_file)
        else:
            self.matrix = self._generate_random_matrix()

    def show_matrix(self):
        """Just shows input matrix that we have"""
        print str(self.matrix)

    def _read_matrix_from_file(self, file_path):
        """Read matrix from file"""
        assert os.path.isfile(file_path), 'File path `%s` is not exist' % \
                                          (file_path,)
        matrix = np.loadtxt(file_path, dtype='i', delimiter=',')
        assert len(matrix[0]) == len(matrix), \
            'Matrix read from file is not square matrix. Interrupt execution'
        assert len(matrix[0]) > 0, \
            'Matrix read from file is zero-length matrix. Interrupt execution'
        self.dimension = len(matrix)
        return matrix

    def _generate_random_matrix(self):
        """Create random filled matrix with given dimension"""
        return np.random.random_integers(-5, 5, (self.dimension, self.dimension))

    @staticmethod
    def calculate_inversion(permutation):
        """Calculate inversion of given permutation"""
        inversion = 0
        for index in range(0,len(permutation)):
            inversion += len(filter(lambda x: x < permutation[index],
                                    permutation[index+1:]))
        return inversion

    def _calculate_determinant(self):
        """Main calculations located there"""
        permutation = permutations(range(self.dimension))
        e = 0
        for iteration in xrange(factorial(self.dimension)):
            term = 1
            permut = permutation.next()
            for i in range(self.dimension):
                term *= self.matrix[i][permut[i]]
            e += (-1)**self.calculate_inversion(permut)*term
        self._determinant = e
        return self._determinant

    def det(self):
        if self._determinant is None:
            return self._calculate_determinant()
        else:
            return self._determinant

if __name__ == "__main__":
    x = Matrix(dimension=5, matrix_file='m.txt')
    x.show_matrix()
    print x.det()

