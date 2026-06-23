from qiskit import QuantumCircuit
from  qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
qcc=QuantumCircuit(2,2)

# Create oracle and superposition
qcc.h([0,1])
qcc.cz(0,1)

# diffusion function 
qcc.h([0,1])
qcc.x([0,1])
qcc.h(1)
qcc.cz(0,1)
qcc.h(1)
qcc.x([0,1])
qcc.h([0,1])

qcc.measure([0,1],[0,1])
print(qcc.draw())

simulator=AerSimulator()
results=simulator.run(qcc,shots=100).result()
counts=results.get_counts()
print("The results  of the measurement are",counts)

plot_histogram(counts)
plt.title("Results")
plt.show()

best=max(counts,key=counts.get)
maze_states={
    "00":"A",
    "01":"B",
    "10":"C",
    "11":"D"

}
print("The states of the maze are",maze_states)
print("The best state or the solution state is ",maze_states[best])