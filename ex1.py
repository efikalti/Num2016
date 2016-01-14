#! /usr/bin/env python

from math import exp, pow, sin, cos


def equation(x, rounded=True):
    fx = exp( pow( sin(x), 3 ) ) + pow( x, 6 ) - 2 * pow( x, 4 ) - pow( x , 3 ) -1
    if rounded:
        fx = float(format(fx, '.4f'))
    return fx

def first_derivative(x, rounded=True):
    sinx = sin(x)
    fx = 3 * exp( pow ( sinx , 3 ) ) * pow ( sinx , 2 ) * cos(x) + 6 * pow( x , 5 ) - 8 * pow( x , 3 ) - 3 * pow( x , 2 )
    if rounded:
        fx = float(format(fx, '.4f'))
    return fx

def second_derivative(x, rounded=True):
    sinx = sin(x)
    esin3x = exp( pow ( sinx , 3 ) )
    fx = - 3 * esin3x * pow ( sinx , 3 ) + 3 * esin3x * ( 3 * esin3x + 2 ) * sinx * pow( cos(x) , 2) + 6 * x * ( 5 * pow( x , 3) - 4 * x -1)
    if rounded:
        fx = float(format(fx, '.4f'))
    return fx

def partition(left, right, current=0):
    current += 1

    fl = equation(left)
    fr = equation(right)

    if fl == 0 :
        print "Partition method required " , current, "repetitions."
        return left
    elif fr == 0 :
        print "Partition method required " , current, "repetitions."
        return right

    #if fl * fr < 0:
    middle = (left + right) / 2.0
    fm = equation(middle)
    if fm == 0 :
        print "Partition method completed after " , current, "repetitions."
        return middle
    elif fm * fl < 0:
        return partition(left, middle, current)
    else:
        return partition(middle, right, current)

def Newton_Raphson(xi, current=0):
    current += 1

    fxi = equation(xi)
    fxi1 = first_derivative(xi)

    x = xi - ( fxi / fxi1 )

    fx = equation(x)

    if fx == 0:
        print "Newton-Raphson method required " , current, "repetitions."
        return x

    return Newton_Raphson(x, current)


def Newton_Raphson_initial_point(left, right):
    r = frange(left, right, 0.01)
    for i in r:
        fx= equation(i)
        fx2 = second_derivative(i)

        if fx * fx2 > 0 :
            return i

    fl = equation(left)
    fl2 = second_derivative(left)
    fr = equation(right)
    fr2 = second_derivative(right)

    if fl * fl2 > 0 :
        return left
    elif fr * fr2 > 0 :
        return right


def secant(x0, x1, current=0):
    current += 1

    fx0 = equation(x0)
    fx1 = equation(x1)

    x = x1 - ( fx1 * ( x1 - x0 ) ) / ( fx1 - fx0 )

    fx = equation(x)

    if fx == 0:
        print "Secant method required " , current, "repetitions."
        return x

    return secant(x1, x, current)


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


def message(root):
    print "Root of the equations to 5 decimal points is ", root
    print "Value of the equations for x =", root, "is", equation(root, False)
    print "-----------------------------------------------------------------"

if __name__ == '__main__':
    left = -2
    right = 2

    r = frange(left, right, 0.01)
    for i in r:
        if equation(i) < 0 :
            break
    if i == 2 :
        print "Equation has no root in the range [", left, ",", right , "]"
    else:

        # Partition method
        print "Starting Partition method to find the root of the equations in the range[", left, ",", right , "]"
        root = partition(left, right)
        message(root)
        print "Starting Partition method to find the root of the equations in the range[", left, ",", root+1 , "]"
        root = partition(left, root+1)
        message(root)
        print "Starting Partition method to find the root of the equations in the range[", root+1, ",", right , "]"
        root = partition(root+1, right)
        message(root)

        # Newton-Raphson method
        x0 = Newton_Raphson_initial_point(left, right)

        print "Starting Newton-Raphson method to find the root of the equations in the range[", left, ",", right , "], with x0 = ", x0
        root = Newton_Raphson(x0)
        message(root)

        x0 = Newton_Raphson_initial_point(root+2, right)
        print "Starting Newton-Raphson method to find the root of the equations in the range[", root+2, ",", right , "], with x0 = ", x0
        root = Newton_Raphson(x0)
        message(root)

        x0 = Newton_Raphson_initial_point(0, right)
        print "Starting Newton-Raphson method to find the root of the equations in the range[", 0, ",", right , "], with x0 = ", x0
        root = Newton_Raphson(x0)
        message(root)

        # Secant method
        print "Starting Secant method to find the root of the equations in the range[", left, ",", right , "]"
        root = secant(left, right)
        message(root)
        print "Starting Secant method to find the root of the equations in the range[", left, ",", 0 , "]"
        root = secant(left, 0)
        message(root)
        print "Starting Secant method to find the root of the equations in the range[", left, ",", -1 , "]"
        root = secant(left, -1)
        message(root)
