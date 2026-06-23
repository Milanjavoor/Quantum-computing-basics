# Quantum Computing Mini Projects with Qiskit

## Overview

This repository contains beginner-friendly quantum computing projects built using Qiskit and Python. These projects were created as part of my journey into quantum computing and quantum algorithms.

The goal of these projects is to understand fundamental quantum concepts such as:

* Qubits
* Superposition
* Quantum Gates
* Measurement
* Entanglement
* Quantum Arithmetic

---

## Project 1: Quantum Coin Toss & Bell State Explorer

### Quantum Coin Toss

This project simulates a fair coin toss using a quantum computer.

A Hadamard gate is applied to a qubit, placing it into a superposition state:

|0⟩ → (|0⟩ + |1⟩)/√2

When measured, the qubit collapses randomly to either:

* 0 (Heads)
* 1 (Tails)

The circuit is executed 1000 times to visualize the probability distribution using a histogram.

### Concepts Learned

* Qubits
* Superposition
* Hadamard Gate (H)
* Quantum Measurement
* Probability Distributions

---

### Bell State Explorer

The second part of the project creates a Bell State, one of the most important examples of quantum entanglement.

Circuit:

1. Apply Hadamard gate to qubit 0.
2. Apply CNOT gate between qubit 0 and qubit 1.
3. Measure both qubits.

This creates the Bell state:

(|00⟩ + |11⟩)/√2

The results demonstrate quantum entanglement because both qubits always produce correlated outcomes.

### Concepts Learned

* Entanglement
* Bell States
* CNOT Gate
* Multi-Qubit Systems
* Quantum Correlations

---

## Project 2: Quantum Binary Calculator

This project implements a simple 1-bit quantum binary adder.

Inputs:

* A = 0 or 1
* B = 0 or 1

Outputs:

* Sum
* Carry

Example:

A = 1

B = 1

Output:

Sum = 0

Carry = 1

### Quantum Gates Used

#### CNOT (CX)

Used to calculate:

Sum = A XOR B

#### Toffoli Gate (CCX)

Used to calculate:

Carry = A AND B

### Concepts Learned

* Quantum Logic Gates
* Quantum Arithmetic
* Binary Addition
* Quantum Circuit Design
* Measurement and Classical Registers

---

## Technologies Used

* Python
* Qiskit
* Qiskit Aer Simulator
* Matplotlib

---

## Installation

Install dependencies:

```bash
pip install qiskit qiskit-aer matplotlib

```

Quantum Sudoku Solver using Grover's Algorithm

A beginner-friendly quantum computing project built with Qiskit that demonstrates how Grover's Search Algorithm can solve a simplified Sudoku puzzle. The project encodes Sudoku constraints into a quantum oracle and uses amplitude amplification through Grover's diffusion operator to increase the probability of measuring valid solutions.

This implementation showcases fundamental quantum computing concepts such as superposition, phase inversion, quantum oracles, and amplitude amplification, providing an intuitive introduction to quantum search and constraint satisfaction problems.
---
🔐 Quantum Password Generator using Qiskit

A practical quantum computing project built with Qiskit that generates secure passwords using quantum-generated randomness. Instead of relying on classical pseudo-random number generators, this project leverages qubits in superposition and quantum measurement to produce unpredictable random bits, which are then converted into strong passwords containing letters, numbers, and special characters.

This implementation demonstrates fundamental quantum computing concepts such as superposition, measurement, quantum random number generation (QRNG), and the real-world application of quantum randomness in cybersecurity and password security.
## Features
- Quantum Random Number Generation (QRNG)
- Custom password length selection
- Supports uppercase and lowercase letters
- Includes numbers and special characters
- Built using Qiskit and Aer Simulator
- Demonstrates real-world quantum computing applications

## Technologies Used
- Python
- Qiskit
- Qiskit Aer

## Quantum Concepts Demonstrated
- Qubits
- Superposition
- Hadamard Gates
- Quantum Measurement
- Quantum Random Number Generation (QRNG)

## Running the Projects

### Coin Toss & Bell State Explorer

```bash
python quantum_coin_bell.py
```

### Quantum Binary Calculator

```bash
python quantum_calculator.py
```

---

## Sample Output

### Quantum Coin Toss

```text
{'0': 501, '1': 499}
```

### Bell State Explorer

```text
{'00': 492, '11': 508}
```

### Quantum Calculator

```text
A = 1
B = 1
Sum = 0
Carry = 1
```

---

## Future Improvements

* 2-Bit Quantum Adder
* 4-Bit Quantum Adder
* Quantum Subtractor
* Quantum Random Number Generator
* Quantum Calculator GUI using Tkinter
* Deutsch-Jozsa Algorithm Visualizer
* Grover's Search Algorithm Simulator

---
Quantum Shor Algorithm Simulation (Educational)

This project is a beginner-friendly simulation inspired by Shor's Algorithm using Qiskit. The implementation demonstrates key quantum computing concepts such as superposition, quantum circuits, the Quantum Fourier Transform (QFT), measurement, and classical post-processing for factor extraction.

The program creates a quantum circuit, applies Hadamard gates to generate superposition, performs controlled operations, applies the inverse QFT, and analyzes measurement results to attempt factorization of a composite number. The output is visualized using a histogram of quantum measurement outcomes.

Note: This project is intended for educational purposes and does not implement the full modular exponentiation stage required for a complete and correct implementation of Shor's Algorithm. Instead, it serves as a learning tool for understanding the structure and workflow of quantum factoring algorithms.

Technologies Used
Python
Qiskit
Qiskit Aer Simulator
NumPy
Matplotlib
Learning Objectives
Understanding quantum circuits
Working with qubits and superposition
Applying the Quantum Fourier Transform (QFT)
Simulating quantum algorithms with Qiskit
Exploring the principles behind Shor's Algorithm and quantum factorization
# 📈 Quantum Portfolio Optimization using QAOA-Inspired Circuits

A beginner-friendly quantum finance project built with Qiskit that demonstrates how quantum computing can be applied to portfolio optimization. The project represents investment decisions using qubits, where each qubit corresponds to buying or skipping a stock. By leveraging quantum superposition, all possible portfolio combinations are explored simultaneously.

The implementation uses QAOA-inspired cost and mixer layers to evaluate portfolio quality based on expected returns and risk values. After quantum simulation and measurement, the most probable portfolio is selected as the optimal investment strategy.

This project introduces fundamental concepts in quantum optimization, including superposition, quantum state encoding, cost functions, mixer operations, amplitude manipulation, and the foundations of the Quantum Approximate Optimization Algorithm (QAOA), one of the most promising algorithms for near-term quantum computing applications in finance and optimization.
## 🚀 Features
- Portfolio optimization using quantum-inspired techniques
- QAOA-style cost and mixer layers
- Simultaneous exploration of multiple portfolio combinations
- Risk vs Return analysis
- Portfolio state visualization using histograms
- Quantum circuit simulation with Qiskit Aer
# 🧩 Quantum Maze Solver using Grover's Algorithm

A beginner-friendly quantum computing project built with Qiskit that demonstrates how Grover's Search Algorithm can be used to solve a simple maze search problem. Maze cells are encoded as quantum states, and the target cell is marked using a quantum oracle. Grover's diffusion operator then amplifies the probability of the correct solution, allowing the quantum computer to identify the goal cell with high probability after measurement.

## 🚀 Features
- Quantum maze search simulation
- Grover's Algorithm implementation
- Oracle and diffusion operators
- Quantum state visualization using histograms
- Qiskit Aer simulation backend

## 🛠️ Technologies Used
- Python
- Qiskit
- Qiskit Aer
- Matplotlib

## 🧠 Quantum Concepts Demonstrated
- Qubits
- Superposition
- Quantum Measurement
- Quantum Oracles
- Amplitude Amplification
- Grover's Search Algorithm

## Learning Journey

These projects are part of my hands-on learning journey in quantum computing, quantum algorithms, machine learning, cybersecurity, and software development.

Feedback and suggestions are welcome.
