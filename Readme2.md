# Quantum Machine Learning — Part 1

This project marks the **beginning of my Quantum Machine Learning (QML) series**, where I explore how quantum computing concepts can be combined with machine learning to solve practical problems.

## About This Project

In this first part, I explore the fundamentals of **quantum feature maps** and their use in a simple **binary classification problem** using **PennyLane**.

The project starts with basic quantum circuits and gradually progresses toward using quantum circuits to transform classical data and produce predictions.

## What This Project Covers

* Creating quantum devices using PennyLane
* Encoding classical features into qubits using `RY` rotations
* Creating quantum entanglement using `CNOT` gates
* Measuring quantum states using expectation values
* Building quantum feature maps
* Working with multiple qubits
* Using quantum circuits for binary classification
* Converting quantum measurement results into class labels
* Working with NumPy datasets

## Technologies Used

* Python
* PennyLane
* NumPy

## Basic Workflow

```text
Classical Data
      ↓
Encode Features into Qubits
      ↓
Apply Quantum Gates
      ↓
Create Entanglement
      ↓
Measure Quantum State
      ↓
Expectation Value
      ↓
Binary Classification
      ↓
Class 0 / Class 1
```

## Learning Goal

The goal of this project is to build a strong foundation in **Quantum Machine Learning** before moving toward more advanced concepts such as:

* Variational Quantum Circuits
* Quantum Kernels
* Variational Quantum Classifiers
* Quantum Neural Networks
* Hybrid Quantum-Classical Models
* Quantum Optimization
* Quantum Machine Learning with real datasets

This project is the **first step in a larger QML learning journey**, progressing from fundamental quantum circuits toward practical hybrid quantum-classical machine learning applications.
# Quantum Machine Learning — Part 2: Trainable Quantum Classifier

This project is **Part 2 of my Quantum Machine Learning (QML) series**.

In Part 1, I explored quantum feature maps, data encoding, entanglement, and basic quantum classification using PennyLane. In this part, I move toward a **trainable quantum model** by introducing trainable parameters, gradients, a cost function, and gradient descent optimization.

## Project Overview

The goal of this project is to understand how a quantum circuit can behave like a machine learning model whose parameters are adjusted during training.

The workflow is:

**Classical Data → Quantum Encoding → Trainable Quantum Circuit → Measurement → Prediction → Cost → Gradient → Parameter Update**

## Concepts Covered

* PennyLane quantum circuits
* QNodes
* Angle embedding
* `RY` rotation gates
* CNOT entanglement
* Trainable quantum parameters
* Strongly Entangling Layers
* Expectation values
* Jacobians and gradients
* Mean Squared Error
* Gradient Descent
* Binary classification
* Quantum circuit optimization

## How the Model Works

The input features are encoded into qubits using Y-axis rotations:

```python
qml.AngleEmbedding(inputs, wires=wires, rotation="Y")
```

Trainable parameters are then applied through:

```python
qml.StronglyEntanglingLayers(...)
```

The circuit measures each qubit using the expectation value of the Pauli-X operator:

```python
qml.expval(qml.PauliX(w))
```

These expectation values are used as the model's output.

## Training Process

The model uses a cost function based on Mean Squared Error:

```python
np.mean((predixt - y) ** 2)
```

PennyLane calculates the gradient of the quantum circuit with respect to its trainable parameters.


# Quantum Machine Learning — Part 2: Trainable Quantum Classifier

This project is **Part 2 of my Quantum Machine Learning (QML) series**.

In Part 1, I explored quantum feature maps, data encoding, entanglement, and basic quantum classification using PennyLane. In this part, I move toward a **trainable quantum model** by introducing trainable parameters, gradients, a cost function, and gradient descent optimization.

## Project Overview

The goal of this project is to understand how a quantum circuit can behave like a machine learning model whose parameters are adjusted during training.

The workflow is:

**Classical Data → Quantum Encoding → Trainable Quantum Circuit → Measurement → Prediction → Cost → Gradient → Parameter Update**

## Concepts Covered

* PennyLane quantum circuits
* QNodes
* Angle embedding
* `RY` rotation gates
* CNOT entanglement
* Trainable quantum parameters
* Strongly Entangling Layers
* Expectation values
* Jacobians and gradients
* Mean Squared Error
* Gradient Descent
* Binary classification
* Quantum circuit optimization

## How the Model Works

The input features are encoded into qubits using Y-axis rotations:

```python
qml.AngleEmbedding(inputs, wires=wires, rotation="Y")
```

Trainable parameters are then applied through:

```python
qml.StronglyEntanglingLayers(...)
```

The circuit measures each qubit using the expectation value of the Pauli-X operator:

```python
qml.expval(qml.PauliX(w))
```

These expectation values are used as the model's output.

## Training Process

The model uses a cost function based on Mean Squared Error:

```python
np.mean((predixt - y) ** 2)
```

PennyLane calculates the gradient of the quantum circuit with respect to its trainable parameters.

The parameters are then updated using:

```python
qml.GradientDescentOptimizer(stepsize=0.1)
```

The training loop repeatedly performs:

1. Forward pass
2. Cost calculation
3. Gradient calculation
4. Parameter update
5. Repeat

After training, the optimized parameters are used to make predictions.

## Prediction

The final quantum output is converted into a binary prediction:

```python
return 1 if output >= 0 else -1
```

This demonstrates how a continuous quantum expectation value can be converted into a classification result.

## Technologies

* Python
* PennyLane
* NumPy

## Learning Goal

The main purpose of this project is to understand the transition from a **fixed quantum circuit** to a **trainable quantum machine learning model**.

This project builds the foundation for more advanced QML concepts such as:

* Variational Quantum Classifiers (VQC)
* Quantum Neural Networks (QNN)
* Quantum Kernels
* Hybrid Quantum-Classical Neural Networks
* Parameterized Quantum Circuits
* Quantum optimization
* Real-world quantum machine learning datasets

## Series Progress

### Part 1

Quantum Feature Maps & Basic Classification

### Part 2

Trainable Quantum Classifier & Gradient Optimization ← **This Project**

### Upcoming

Variational Quantum Circuits → Quantum Kernels → QNNs → Hybrid Models → Real-World QML




## Author

**Milan Javoor**

Part of my ongoing exploration of **Quantum Computing, Quantum Machine Learning, Artificial Intelligence, and Deep Learning**.
