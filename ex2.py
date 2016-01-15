#! /usr/bin/env python

from math import pow
from random import uniform


def equation(x, rounded=True):
    fx = 54 * pow( x, 6 ) + 45 *  pow( x, 5 ) - 102 *  pow( x, 4 ) - 69 *  pow( x, 3 ) + 35 *  pow( x, 2 )  + 16 * x - 4
    if rounded:
        fx = float(format(fx, '.4f'))
    return fx

def first_derivative(x, rounded=True):
    fx = 324 *  pow( x, 5 ) + 225 *  pow( x, 4 ) - 408 *  pow( x, 3 ) - 207 *  pow( x, 2 ) + 70 * x + 16
    if rounded:
        fx = float(format(fx, '.4f'))
    return fx

def second_derivative(x, rounded=True):
    fx = 2 * ( 810 * pow( x, 4 ) + 450 * pow( x, 3 ) - 612 * pow( x, 2 ) - 207 * x + 35)
    if rounded:
        fx = float(format(fx, '.4f'))
    return fx

def modified_partition(left, right, current=0):
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
    while True:
        random = uniform(left, right)
        fm = equation(random)
        if fm == 0 :
            print "Partition method completed after " , current, "repetitions."
            return random
        elif fm * fl < 0:
            return modified_partition(left, random, current)
        elif fm * fr < 0:
            return modified_partition(random, right, current)
        current += 1

def modified_Newton_Raphson(xi, current=0):
    current += 1

    fxi = equation(xi)
    fxi1 = first_derivative(xi)
    fxi2 = second_derivative(xi)

    x = xi - ( 1 / ( ( fxi1 / fxi ) - ( fxi1 / ( 2 * fxi2 ) ) ) )

    fx = equation(x)

    if fx == 0:
        print "Newton-Raphson method required " , current, "repetitions."
        return x

    return modified_Newton_Raphson(x, current)


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


def modified_secant(x0, x1, x2, oldest=0, current=0):
    current += 1

    fx0 = equation(x0)
    fx1 = equation(x1)
    fx2 = equation(x2)

    r = fx2 / fx1
    q = fx0 / fx1
    s = fx2 / fx0

    x = x2 - ( r * ( r - q ) * ( x2 - x1 ) + ( 1 - r ) * s * ( x2 - x0 ) ) / ( ( q - 1) * ( r - 1 ) * ( s - 1 ) )

    fx = equation(x)

    if fx == 0:
        print "Secant method required " , current, "repetitions."
        return x

    if oldest == 0 :
        oldest = 1
        x0 = x
    elif oldest == 1:
        oldest = 2
        x1 = x
    else:
        oldest == 0
        x2 = x

    return modified_secant(x0, x1, x2, oldest, current)


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
        print "Starting modified Partition method to find the root of the equations in the range[", 1, ",", 2 , "]"
        root = modified_partition(1, 2)
        message(root)
        print "Starting modified Partition method to find the root of the equations in the range[", 0.4, ",", 1 , "]"
        root = modified_partition(0.4, 1)
        message(root)
        print "Starting modified Partition method to find the root of the equations in the range[", 0, ",", 0.3 , "]"
        root = modified_partition(0, 0.3)
        message(root)
        print "Starting modified Partition method to find the root of the equations in the range[", -2, ",", -1 , "]"
        root = modified_partition(-2, -1)
        message(root)
        print "Starting modified Partition method to find the root of the equations in the range[", -0.9, ",", 0 , "]"
        root = modified_partition(-1, 0)
        message(root)


        # Newton-Raphson method
        x0 = Newton_Raphson_initial_point(left, right)

        print "Starting modified Newton-Raphson method to find the root of the equations in the range[", left, ",", right , "], with x0 = ", x0
        root = modified_Newton_Raphson(x0)
        message(root)

        x0 = Newton_Raphson_initial_point(root+2, right)
        print "Starting modified Newton-Raphson method to find the root of the equations in the range[", root+2, ",", right , "], with x0 = ", x0
        root = modified_Newton_Raphson(x0)
        message(root)

        x0 = Newton_Raphson_initial_point(0, right)
        print "Starting modified Newton-Raphson method to find the root of the equations in the range[", 0, ",", right , "], with x0 = ", x0
        root = modified_Newton_Raphson(x0)
        message(root)

        x0 = Newton_Raphson_initial_point(-1, 0)
        print "Starting modified Newton-Raphson method to find the root of the equations in the range[", -1, ",", 0 , "], with x0 = ", x0
        root = modified_Newton_Raphson(x0)
        message(root)

        x0 = Newton_Raphson_initial_point(1, right)
        print "Starting modified Newton-Raphson method to find the root of the equations in the range[", 1, ",", right , "], with x0 = ", x0
        root = modified_Newton_Raphson(x0)
        message(root)


        # Secant method
        print "Starting modified Secant method to find the root of the equations with starting values ", left, ",", 0 , ",", right, "."
        root = modified_secant(left, 0, right)
        message(root)
        print "Starting modified Secant method to find the root of the equations with starting values ", left, ",", -1 , ",", 0, "."
        root = modified_secant(left, -1, 0)
        message(root)
        print "Starting modified Secant method to find the root of the equations with starting values ", 0, ",", 1 , ",", right, "."
        root = modified_secant(0, 1, right)
        message(root)
        print "Starting modified Secant method to find the root of the equations with starting values ", -1.5, ",", -1.4 , ",", -1.2, "."
        root = modified_secant(-1.5, -1.4, -1.2)
        message(root)
        print "Starting modified Secant method to find the root of the equations with starting values ", 1, ",", 1.2 , ",", 1.5, "."
        root = modified_secant(1, 1.2, 1.5)
        message(root)
