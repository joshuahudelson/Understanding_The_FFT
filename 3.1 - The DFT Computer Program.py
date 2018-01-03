"""
Translation from BASIC to Python of DFT program from "Understanding the FFT"
by Anders E. Zonst, pages 52-53 (figure 3.1).
"""

import math
import random

# Generate/Analyze Waveform

PI = 3.141592653589793
P2 = 2*PI
K1 = PI/8
K2 = 1/PI

Y = [0]*16
FC = [0]*16
FS = [0]*16
KC = [0]*16
KS = [0]*16
Z = [0]* 16  # for reconstructing with inverse DFT

def print_headings():
    print("FREQ \t\t F(COS) \t F(SIN) \t Y(COS) \t Y(SIN)")

def generate_input_function(function_name):
    if (function_name == "triangle wave"):
        """ Sum odd cosines, divided by squares, making a triangle wave.
        """
        for I in range (16):
            K3 = I*K1
            Y[I] = math.cos(K3)
            Y[I] += math.cos(3 * K3) / 9
            Y[I] += math.cos(5 * K3) / 25
            Y[I] += math.cos(7 * K3) / 49
        for I in range (1, 8, 2):
            KC[I] = 1/pow(I, 2)
    elif (function_name == "phase-shifted sine"):
        """ page 61.
        """
        K4 = 3 * PI/8        # phase-shift = 67.5 degrees
        KC[1] = math.cos(K4)
        KS[1] = math.sin(K4)
        for I in range(16):
            K3 = I*K1
            Y[I] = math.cos(K3 + K4)
    elif ((function_name)  == "random harmonics"):
        for I in range (9):
            KC[I] = random.random()
            KS[I] = random.random()
        for I in range(16):
            for J in range(9):
                K4 = I * J * K1
                Y[I] += (KC[J] * math.cos(K4)) + (KS[J] * math.sin(K4))
    elif ((function_name) == "perfect triangle"):
        K2 = (PI * PI)/8
        K3 = K2/4
        for I in range(8):
            Y[I]  = K2 - (K3 * I)
        for I in range(8, 16):
            Y[I] = (K3*I) - (3 * K2)

def do_DFT():
    """ Iterate through frequencies, sum components.
    """
    for J in range (16):                # J = frequency
        for I in range(16):             # I = data point
            FC[J] += Y[I] * math.cos(J * I * K1)
            FS[J] += Y[I] * math.sin(J * I * K1)
        FC[J] /= 16
        FS[J] /= 16

def print_outputs():
    rndamt = 4
    for Z in range(16):
        print(str(Z) + "\t\t "+ str(round(FC[Z], rndamt)) +
                       "\t\t" + str(round(FS[Z], rndamt)) +
                       "\t\t" + str(round(KC[Z], rndamt)) +
                       "\t\t" + str(round(KS[Z], rndamt)))
    user_input = "Y" #input("More?")
    if (user_input == "Y"):
        pass
    else:
        print("Done.")

def do_inverse_DFT():
    for J in range(16):             # frequency component
        for I in range(16):         # data point
            Z[I] = Z[I] + (FC[J] * math.cos(J * I * K1)) + (FS[J] * math.sin(J * I * K1))


def print_inverse_outputs():
    rndamt = 4
    print()
    print("T \t\t Z[I] \t\t Y[I]")
    for A in range(16):
        print(str(round(A, rndamt)) + "\t\t" +
              str(round(Z[A], rndamt)) + "\t\t" +
              str(round(Y[A], rndamt)))

print_headings()
generate_input_function("random harmonics")
do_DFT()
print_outputs()
do_inverse_DFT()
print_inverse_outputs()
