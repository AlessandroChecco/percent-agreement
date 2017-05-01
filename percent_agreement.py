# #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Percent agreement by Alessandro Checco.

agreement(mat)
Compute the percent agreement of a list of documents rated by a possibly different number of raters.

Arguments:
    mat: a list of document ratings. It is a list of lists, where the inner list is a set of ratings.

Returns:
    The percent agreement of the set of documents.

Example:
    For two documents with three ratings for the first document and 4 ratings for the second document:

        $ mat = [[1,1,2],[4,4,4,3]]
        $ agreement(mat)

.. Alessandro Checco CC copyright
   http://http://github.com/AlessandroChecco

"""
import numpy as np
import scipy.misc
import sys, ast
def agreement(mat):
    """agreement(mat)
    Compute the percent agreement of a list of documents rated by a possibly different number of raters.

    Arguments:
        mat: a list of document ratings. It is a list of lists, where the inner list is a set of ratings.

    Returns:
        The percent agreement of the set of documents.

    Example:
        For two documents with three ratings for the first document and 4 ratings for the second document:

            $ mat = [[1,1,2],[4,4,4,3]]
            $ agreement(mat)
    """
    return  np.mean([scipy.misc.comb(np.unique(x,return_counts=True)[1],2).sum()/len(x) for x in mat])
    
if __name__ == "__main__":
    import sys
    print("Computing agreement of",sys.argv[1])
    print(agreement(ast.literal_eval(sys.argv[1])))
