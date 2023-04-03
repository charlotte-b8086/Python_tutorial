#adding argparse so can run from command line
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-tol", "--tolerance", type=float, help="Tolerance level for Newton's approximation method.")
parser.add_argument("-x0",  "--xinitial", type=float, help="Initial x estimate for Newton's method.")

#define the function we are working with and its derivative
def func(K):
    return (L/K)*(1-np.exp(-1*K*(t+a)))-F
def func_deriv(K):
    return (-1*L/K**2)*(1-np.exp(-1*K*(t+a)))+(L/K)*(t+a)*np.exp(-1*K*(t+a))

#parameters for graphing
L = 1.0
t = 1.0
a = 1.0
F = 1.0

K = np.linspace(1, 10, 1000)

plt.plot(K,func(K))

#use newton's method to estimate value of K in F by finding where previously defined function is 0
def newtons(Tol, x_0 = 1.0):
    x_old = x_0
    x_new = x_old + Tol + 1
    while np.abs(x_new-x_old) >= Tol:
        (x_old, x_new) = (x_new, x_new - func(x_new)/func_deriv(x_new))
    print('The estimate for K is {:f}.'.format(x_new))

#to run from the command line
if __name__ == '__main__':
    args = parser.parse_args()
    if args.xinitial is None:
        newtons(args.tolerance)
    else:
        newtons(args.tolerance, args.xinitial)