#---------------------------------------------- Hybrid Quantum - Classical Neural Netowk ----------------------------------------------------
import pennylane as qml 
import torch
import torch.nn as nn
def build_qnode(n_qubits,n_layers):
    dev=qml.device("default.qubit",wires=n_qubits)
    @qml.qnode(dev,interface="torch",diff_method="backprop")
    def circuit(inputs,weights):
        wires=range(n_qubits)
        for layer in range(n_layers):
            # Create angle embedding for the inputs
            qml.AngleEmbedding(inputs,wires=wires,
                               rotation="Y")
            # form a layer using three rotation gates , and trainable weights 
            qml.StronglyEntanglingLayers(weights[layer:layer+1],
                                         wires=wires,ranges=[layer%(n_qubits-1)+1])
        return [ qml.expval(qml.PauliX(w)) for w in wires]
    return circuit

class HybridQNN(nn.Module):
    def __init__(self,n_layers,n_qubits):
        super().__init__()
        self.circuit=build_qnode(n_qubits,n_layers)
        self.quantum=qml.qnn.TorchLayer(self.circuit,
                                        {"weights":(n_layers,n_qubits,3)})
        self.head=nn.Linear(n_qubits,1)
    def forward(self,x):
        quantum_out=self.quantum(x)
        return self.head(quantum_out).squeeze(-1)
    
    




