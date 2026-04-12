import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
# function to convert binary fraction to decimal
def bin_to_dec(x):
    val = 0
    for i, bit in enumerate(x):
        if bit=='1':
            val+=1/(2**(i+1))
    return val
# function to generate the bits (bitstring) in such a way that the division of the box's edge signify the bits
# so the number of bits is equal to the no of division of edge
def generate_bit(leng,simulator):
    qc =QuantumCircuit(leng,leng)
    qc.h(range(leng))
    qc.measure(range(leng),range(leng))
    job=simulator.run(transpile(qc,simulator),shot=1, memory= True)
    result = job.result()
    x =result.get_memory()[0]
    return x
#Configuration by user input 
NUMPOINT=input("Input the number of darts to be simulated")
PRECISION=input("Input the no of division to be divided the edge of the board")
simulator = AerSimulator
x_points = []
y_points = []
inside_circle = 0
print(f"Generating {NUMPOINT} quantum random points...")
#generating random points 
for i,in range(NUMPOINT):
    #generating random points on X axis :
    x_plot=generate_bit(PRECISION,simulator)
    x_dec=bin_to_dec(x_plot)
    #generating random points on Y axis :
    y_plot=generate_bit(PRECISION,simulator)
    y_dec=bin_to_dec(y_plot)
    x_points.append(x_plot)
    y_points.append(y_plot)
    # Checking the points inside the circle
    if(x_dec**2 + y_dec**2) <=1:
        k+=1
simulated_pi=4*(k/NUMPOINT)
# OUTPUT
print(f"--- RESULT ---")
print(f"TOTAL POINTS: {NUMPOINT}")
print(f"POINTS INSIDE THE CIRCLE: {k}")
print(f"SIMULATED PI VALUE: {simulated_pi}")
print(f"REAL PI VALUE: {np.pi}")
print(f"ERROR : {abs(simulated_pi - np.pi)}")

# --- Visualization ---
plt.figure(figsize=(6,6))
circle = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=2)
plt.gca().add_patch(circle)

# Plot points
colors = ['green' if (x**2 + y**2) <= 1 else 'red' for x, y in zip(x_points, y_points)]
plt.scatter(x_points, y_points, c=colors, s=10)

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("X (Quantum Random)")
plt.ylabel("Y (Quantum Random)")
plt.title(f"Estimating Pi using Quantum Randomness\nEst: {simulated_pi}")
plt.show()