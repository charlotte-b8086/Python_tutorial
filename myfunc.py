'''Going to work on definining and manipulating a function!
The function will graph a sine, cosine, or tangent function.'''
import numpy as np
import matplotlib.pyplot as plt

#Define A, B, omega
#print('Please enter information about the type of trigonometric function you would like to graph.\n')
A = float(input("What do you want your amplitude to be? "))
print("\n")
B = float(input("What do you want your vertical shift to be? "))
print("\n")
omega = float(input("What do you want your period parameter to be? "))
print("\n")
trig = input("What type of trig function do you want to plot? ")
print("\n")


def basic_plot(A, B, omega, trig=None):
    '''Plot B + A*trig(omega t) on a fixed interval -10 < t < 10
    where trig can be cos sin or tan'''
    x_vals = np.arange(-10,10,0.1)
    if trig is None:
        basic_plot(A, B, omega, 'sine')
        return
    elif 'tan' in trig:
        plt.plot(x_vals, B + A *np.tan(omega * x_vals))
        plt.title('A Tangent Curve')
    elif 'cos' in trig:
        plt.plot(x_vals, B + A *np.cos(omega * x_vals))
        plt.title('A Cosine Curve')
    elif 'sin' in trig:
        plt.plot(x_vals, B + A *np.sin(omega * x_vals))
        plt.title('A Sine Curve')
    else:
        raise ValueError("Unrecognized Trig Function.\nPlease re-run the script to graph a sine, cosine, or tangent function.")

    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.show()

def cute_plot(A, B, omega, trig=None):
    '''Plot a comic version of B + A*trig(omega t) on a fixed interval -10 < t < 10
    where trig can be cos sin or tan'''
    with plt.xkcd():
        basic_plot(A, B, omega, trig)

#Call the function
cuteness = input("Do you want to create a cute plot? ")
print("\n")
if 'y' in cuteness:
    cute_plot(A, B, omega, trig='sin')
else:
    basic_plot(A, B, omega, trig='sin')