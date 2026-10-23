import pennylane as qml
from pennylane import numpy as np


dev=qml.device("default.qubit",wires=2)

qml.qnode(dev)
def circuit(x,theta):
    qml.RY(x[0],0)
    qml.RY(x[1],1)
