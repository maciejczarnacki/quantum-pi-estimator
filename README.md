# Quantum $\pi$: Estimating $\pi$ Using Quantum Randomness

A project prepared as an independent study in the field of Quantum Computing, developed through the Department of Physics at A.J.C. Bose College. 

## Abstract
This project implements a quantum-enhanced Monte Carlo simulation to estimate the value of $\pi \approx 3.14159$. By generating truly random coordinates using quantum superposition and measurement via the Qiskit framework, it simulates "dart throws" onto a unit square containing a quarter-circle. The proportion of darts landing inside the circle, scaled by 4, yields an approximation of $\pi$. Unlike classical methods relying on pseudo-random number generators (PRNGs), this approach harnesses quantum indeterminacy for unbiased randomness.

## Key Features
* **Quantum Random Number Generation (QRNG):** Uses Hadamard gates on multiple qubits to produce uniform binary strings. 
* **Configurable Parameters:** Allows user-defined point volumes and precision parameters.
* **Hybrid Processing:** Maps measured quantum bitstrings to binary fractions, achieving a functional uniform coordinate system.

## Methodology
Instead of altering the underlying Monte Carlo mathematics, this approach replaces the classical PRNG with a QRNG. Qubits are initialized into a state of uniform superposition using a Hadamard gate. The function applies a single-qubit unitary transformation with the matrix representation:

$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

Measuring this superposition forces a purely probabilistic wave-function collapse, yielding a fundamentally unpredictable, true random bit.

## Dependencies
* Python 3
* `qiskit`
* `qiskit_aer` (AerSimulator for local emulation)
* `numpy`
* `matplotlib`

## Future Work
* **Deployment on Real Quantum Hardware:** Executing the QRNG circuit on IBM Quantum hardware to quantify cumulative gate and readout error.
* **Error Mitigation:** Implementing Zero-Noise Extrapolation (ZNE) or Readout Error Mitigation (REM) to correct asymmetry. 
* **Circuit Batching:** Exploiting Qiskit's multi-shot job capabilities to reduce the execution time bottleneck. 
* **Quantum Amplitude Estimation (QAE):** Replacing classical Monte Carlo post-processing with QAE to achieve quadratic quantum speedup with $O(1/N)$ error scaling.
