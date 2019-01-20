import math
import matplotlib.pyplot as plt

""" BASIC CODE:
10 REM *** DFT 1.0 - GENERATE SQUARE WAVE ***
12 INPUT "NUMBER OF TERMS";N
20 PI = 3.14159265358#
30 FOR I = 0 TO 2*PI STEP PI/8
32 Y=0
40 FOR J=l TO N STEP 2: Y=Y+SIN(J*I) /J: NEXT J
50 PRINT Y
60 NEXT I
70 END
"""

number_of_frequencies = 128
points_in_cycle = 160
PI = 3.1415926535

vector = []

for i in range(points_in_cycle):
    y = 0
    for j in range(1, number_of_frequencies, 2):
        y = y + (math.sin(j*(i*PI/8)) / j)
    vector.append(y)
print(vector)
plt.plot(vector)
plt.show()
