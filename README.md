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

---

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

## Learning Journey

These projects are part of my hands-on learning journey in quantum computing, quantum algorithms, machine learning, cybersecurity, and software development.

Feedback and suggestions are welcome.
