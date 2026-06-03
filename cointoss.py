import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
coincircuit=QuantumCircuit(1,1)
coincircuit.h(0)
coincircuit.measure(0,0)
print("the quantum circuit for the coin toss is: ")
print(coincircuit)
simulator=AerSimulator()
job=simulator.run(coincircuit,shots=1000)
results=job.result()
count=results.get_counts()
print("the results of the coin toss are")
print(count)
plot_histogram(count)
plt.show()
"""
the second part of the project is a Bell state explorer where we can create , explore 
experiment with quantum bell states in two qubit systems.
"""
bellcircuit=QuantumCircuit(2,2)
bellcircuit.h(0)
bellcircuit.cx(0,1)
bellcircuit.measure([0,1],[0,1])
print("bell state circuit:")
print(bellcircuit)
job2=simulator.run(bellcircuit,shots=1000)
results2=job2.result()
counts=results2.get_counts()
print("the results of the bell state explorer are:")
print(counts)
plot_histogram(counts)
plt.show()