# Copyright 2017 Patrick Kunzmann.
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.

from ..sequence import Sequence
from ..seqtypes import DNASequence, ProteinSequence
from ..alphabet import Alphabet
import numpy as np
import os.path

__all__ = ["SubstitutionMatrix"]


class SubstitutionMatrix(object):
    
    def __init__(self, alphabet1, alphabet2, matrix):
        self._alph1 = alphabet1
        self._alph2 = alphabet2
        if isinstance(matrix, dict):
            matrix_dict = matrix
            self._matrix = np.zeros(( len(alphabet1), len(alphabet2) ),
                                    dtype="i4")
            for i in range(len(alphabet1)):
                for j in range(len(alphabet2)):
                    sym1 = alphabet1.decode(i)
                    sym2 = alphabet2.decode(j)
                    self._matrix[i,j] = int(matrix_dict[sym1, sym2])
        elif isinstance(matrix, np.ndarray):
            self._matrix = np.copy(matrix)
        else:
            raise TypeError("Matrix must be either a dictionary "
                            "or an 2-D ndarray")
    
    def get_alphabet1(self):
        return self._alph1
    
    def get_alphabet2(self):
        return self._alph2
    
    def get_matrix(self):
        return np.copy(self._matrix)
    
    def get_score_by_code(self, code1, code2):
        return self._matrix[code1, code2]
    
    def get_score(self, symbol1, symbol2):
        code1 = self._alph1.encode(symbol1)
        code2 = self._alph1.encode(symbol2)
        return self._matrix[code1, code2]
    
    def shape(self):
        return (len(alphabet1), len(alphabet2))
    
    def __str__(self):
        string = "{:>3}".format("")
        for symbol in self._alph2:
            string += " {:>3}".format(str(symbol))
        string += "\n"
        for i, symbol in enumerate(self._alph1):
            string += "{:>3}".format(str(symbol))
            for j in range(len(self._alph2)):
                string += " {:>3}".format(int(self._matrix[i,j]))
            string += "\n"
        return string
    
    @staticmethod
    def std_protein_matrix():
        return _matrix_blosum62
    
    @staticmethod
    def std_nucleotide_matrix():
        return _matrix_nuc


# Preformatted BLOSUM62 and NUC substitution matrix from NCBI

_matrix_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                          "matrix_data")

_matrix = np.load(os.path.join(_matrix_dir, "blosum62.npy"))
_alph = ProteinSequence.alphabet 
_matrix_blosum62 = SubstitutionMatrix(_alph, _alph, _matrix)

_matrix = np.load(os.path.join(_matrix_dir, "nuc.npy"))
_alph = DNASequence.alphabet 
_matrix_nuc = SubstitutionMatrix(_alph, _alph, _matrix)
