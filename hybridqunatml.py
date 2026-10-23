import pennylane as qml
from pennylane import numpy as np


dev=qml.device("default.qubit",wires=2)

qml.qnode(dev,interface="torch")
def circuit(x,theta):
    qml.RY(x[0],0)
    qml.RY(x[1],1)
    qml.RY(theta[0],0)
    qml.RY(theta[1],0)
    qml.RY(theta[2],1)
    qml.RY(theta[3],1)
    qml.CNOT([0,1])
    return [qml.exp(qml.PauliX(0)),qml.exp(qml.PauliX(1))]


weight_shapes={"weights":(4,)}

qlayer=qml.qnn.TorchLayer(qnode,weight_shapes)
