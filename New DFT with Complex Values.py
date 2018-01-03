import math
import random

PI = 3.141592653589793
P2 = 2*PI                   # never gets used?
K1 = PI/8
K2 = 1/PI

C = [[0 for index in range(16)] for column in range(2)]
S = [[0 for index in range(16)] for column in range(2)]
KC = [[0 for index in range(16)] for column in range(2)]
KS = [[0 for index in range(16)] for column in range(2)]

def generate_triangle_wave():
    for I in range(16):
        K3 = I*K1
        C[0][I] = (math.cos(K3) +
                  (math.cos(3*K3)/9) +
                  (math.cos(5*K3)/25) +
                  (math.cos(7*K3)/49))
        KC[0][I] = C[0][I]
    for I in range(1, 8, 2):
        KC[1][I] = 1/pow(I, 2)

def generate_circle():
    for I in range(16):
        K3 = I*K1
        C[0][I] = math.sin(K3)
        S[0][I] = math.cos(K3)
        KC[0][I] = C[0][I]
        KS[0][I] = S[0][I]
    KS[1][0] = 1

def generate_ellipse1_1():
    for I in range(16):
        K3 = I*K1
        C[0][I] = math.sin(K3)
        S[0][I] = 2 * math.cos(K3)
        KC[0][I] = C[0][I]
        KS[0][I] = S[0][I]
    KS[1][0] = 1.5
    KS[1][15] = 0.5

def generate_ellipse1_2():
    for I in range(16):
        K3 = I*K1
        S[0][I] = 2* math.sin(K3)
        C[0][I] = math.cos(K3)
        KC[0][I] = C[0][I]
        KS[0][I] = S[0][I]
    KC[1][0] = -0.5
    KC[1][15] = 1.5

def print_column_headings():
    print("FREQ \t\t F(COS) \t\t F(SIN) \t\t Y(COS) \t\t Y(SIN)")
    print()

def transform_or_reconstruct(M, N, K5, K6):
    for J in range(16):
        for I in range(16):
            # these two-d arrays seems like ridiculous ways of holding the data.
            # shouldn't the input funciton rather be Input[real, imaginary]?  Would be clearer...
            C[M][J] += (C[N][I] * math.cos(J * I * K1)) + (K6 * S[N][I] * math.sin(J * I * K1))
            S[M][J] += (-1 * K6 * C[N][I] * math.sin(J * I * K1)) + (S[N][I] * math.cos(J * I * K1))
        C[M][J] /= K5
        S[M][J] /= K5

def print_out_final_values(M):
    rndamt = 4
    for A in range(16):
        print(str(A) + "\t\t" +
              str(round(C[M][A], rndamt)) + "\t\t\t" +
              str(round(S[M][A], rndamt)) + "\t\t\t" +
              str(round(KC[M][A], rndamt)) + "\t\t\t" +
              str(round(KS[M][A], rndamt)))
    print()

def forward_transform():
    M = 1
    N = 0
    K5 = 16.0
    K6 = -1.0
    print_column_headings()
    for J in range(16):
        C[1][J] = 0
        S[1][J] = 0
    transform_or_reconstruct(M, N, K5, K6)
    print_out_final_values(M)

def inverse_transform():
    M = 0
    N = 1
    K5 = 1  # no division
    K6 = 1  # positive instead of negative
    print_column_headings()
    for I in range(16):
        C[0][I] = 0
        S[0][I] = 0
    transform_or_reconstruct(M, N, K5, K6)
    print_out_final_values(M)


generate_triangle_wave()
forward_transform()
inverse_transform()
