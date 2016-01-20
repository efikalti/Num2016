#! /usr/bin/env python

import numpy as np
from random import randint
from math import pow, sqrt

A = list()
A = [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     [0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
     [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
     [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
     [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0]]


def calculate_An(A):
    # Calculate matrix An which contains the sum of every row of A.
    An = list()
    for row in A:
        An.append(sum(row))
    return An


def calculate_G(A, q=0.15,):
    An = calculate_An(A)
    n = (len(A))
    # Initialize G matrix with zeros. Default size is 15x15.
    G = [[0.0 for x in range(n)] for x in range(n)]

    # Calculate value for G
    for i in range(n):
        for j in range(n):
            G[i][j] = ( q/n ) + ( ( A[j][i] * ( 1 - q ) ) / An[j] )
    return G


def power_method(G, bi=None, current=0, max=5):
    n = len(G)
    current += 1
    # If the bi is None this is the first iteration and we need to choose a random column as bi
    if bi == None:
        k = randint(0, n)
        bi = [0.0 for x in range(0, n)]
        for i in range(0, n):
            bi[i] = G[k][i]
    # Set bi to a temp vector for the calculations
    bi_tmp = list()
    for i in range(0, n):
        bi_tmp.append(bi[i])

    #
    for i in range(0, n):
        bi_tmp[i] = np.dot(G[i], bi)

    i_max = 0
    i = 0
    while i_max == 0:
        if bi_tmp[i] != 0:
            i_max = bi_tmp[i]
    if i_max == 0:
        # If all values are zeros return previous bi vector.
        return bi

    # Set bi_tmp to bi and divide by the selected value
    bi = bi_tmp
    for i in range(0, n):
        bi[i] = bi[i] / i_max


    # Check if you reached max number or repetitions.
    if current == max:
        return bi

    return power_method(G, bi, current)


def print_matrix(A, name=""):
    print "matrix", name, ":"
    for row in A:
        print row
    print


def max_eigenvector(G):
    # Calculate biggest eigenvector of Google matrix with power method.
    x = power_method(G)
    n = len(x)

    # Normalize vector x
    # Find the sum of vector x
    sum_x  = sum(x)
    if sum_x != 0:
        for i in range(0, n):
            x[i] = x[i] / sum_x
    else:
        print "The sum of the vector is 0."

    # Print max eigenvector and sum of it.
    print "Max eigenvector of Google matrix:"
    print x
    print "with value sum:", sum(x)
    print


if __name__ == '__main__':
    print_matrix(A, "A")

    n = len(A)


    # EX. 2
    # Calculate Google matrix
    G = calculate_G(A)

    print_matrix(G, "Google")

    # Calculate and print max eigenvector of G.
    max_eigenvector(G)


    # EX. 3
    # Create second matrix A with three more connections for page 3
    A2 = [[0.0 for x in range(0, n)] for x in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            if A[i][j] == 1.0:
                A2[i][j] = 1.0
    A2[10][2] = 1.0
    A2[5][2] = 1.0
    A2[12][2] = 1.0

    print_matrix(A2, "A2")
    # Calculate G matrix for A2.
    G2 = calculate_G(A2)

    print_matrix(G2, "Google2")

    # Calculate and print max eigenvector of G2.
    max_eigenvector(G2)


    # EX. 4
    # Calculate G matrix for A2 with q = 0.01
    G_001 = calculate_G(A2, q=0.01)

    print_matrix(G_001, "Google2, q=0.01")

    # Calculate and print max eigenvector of G2.
    max_eigenvector(G_001)

    # Calculate G matrix for A2 with q = 0.7
    G_07 = calculate_G(A2, q=0.7)

    print_matrix(G_07, "Google2, q=0.7")

    # Calculate and print max eigenvector of G2.
    max_eigenvector(G_07)


    # EX. 5
    # Create third matrix A with different connections for A[8,11], A[12,11]
    A3 = [[0.0 for x in range(0, n)] for x in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            if A[i][j] == 1.0:
                A3[i][j] = 1.0
    A3[8][11] = 2.0
    A3[12][11] = 2.0

    print_matrix(A3, "A3")
    # Calculate G matrix for A3.
    G3 = calculate_G(A3)

    print_matrix(G3, "Google3")

    # Calculate and print max eigenvector of G3.
    max_eigenvector(G3)


    # EX. 6
    # Create fourth matrix A without page 11
    A4 = [[0.0 for x in range(0, n-1)] for x in range(0, n-1)]
    print_matrix(A4, "A4")
    for i in range(0, n):
        if i != 10:
            for j in range(0, n):
                if j != 10:
                    if A[i][j] == 1.0:
                        k = i
                        l = j
                        if i > 10:
                            k -= 1
                        if j > 10:
                            l -= 10
                        A4[k][l] = 1.0

    print_matrix(A4, "A4")
    # Calculate G matrix for A4.
    G4 = calculate_G(A4)

    print_matrix(G4, "Google4")

    # Calculate and print max eigenvector of G4.
    max_eigenvector(G4)
