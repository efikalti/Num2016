#! /usr/bin/env python

from math import exp, pow, sin


def equation(x, rounded=True):
    fx = exp( pow( sin(x), 3 ) ) + pow( x, 6 ) - 2 * pow( x, 4 ) - pow( x , 3 ) -1
    if rounded:
        fx = float(format(fx, '.4f'))
    return fx


def partition(left, right, num, current):
    current += 1
    if num == current:
        return

    fl = equation(left)
    fr = equation(right)

    if fl == 0 :
        print "Partition method required " , current, "repetitions."
        return left
    elif fr == 0 :
        print "Partition method required " , current, "repetitions."
        return right

    if fl * fr < 0:
        middle = (left + right) / 2.0
        fm = equation(middle)
        if fm == 0 :
            print "Partition method completed after " , current, "repetitions."
            return middle
        elif fm * fl < 0:
            return partition(left, middle, num, current)
        else:
            return partition(middle, right, num, current)


def frange(start, end=None, inc=None):
    "A range function, that does accept float increments"

    if end == None:
        end = start + 0.0
        start = 0.0
    else: start += 0.0 # force it to be a float

    if inc == None:
        inc = 1.0

    count = int((end - start) / inc)
    if start + count * inc != end:
        # need to adjust the count.
        # AFAIKT, it always comes up one short.
        count += 1

    L = [None,] * count
    for i in xrange(count):
        L[i] = start + i * inc

    return L


if __name__ == '__main__':
    r = frange(-2, 2, 0.01)
    for i in r:
        if equation(i) < 0 :
            break
    if i == 2 :
        print "Equation has no root in the range [", -2, ",", 2 , "]"
    else:
        print "Starting Partition method to find the root of the equations in the range[", i, ",", 2 , "]"
        root = partition(i, 2, 50, 0)
        print "Root of the equations to 5 decimal points is ", root
        print "Value of the equations for x =", root, "is", equation(root, False)
