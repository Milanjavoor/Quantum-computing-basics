from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
qc=QuantumCircuit(4,4)
qc.h([0,1,2,3])

#-------------------------- Oracle formation ------------------------------------------------------------------------------------------------------------------------------

qc.cz(0,1)
qc.cz(0,2)
qc.cz(1,3)
qc.cz(2,3)

#----------------------------- Diffusion -----------------------------------------------------------------------------------------------------------------------------------

qc.h([0,1,2,3])
qc.x([0,1,2,3])
qc.h(3)
qc.mcx([0,1,2],3)
qc.h(3)
qc.x([0,1,2,3])
qc.h([0,1,2,3])

qc.measure(range(4),range(4))
print(qc)

simulator=AerSimulator()
compiled=transpile(qc,simulator)
results=simulator.run(compiled,shots=1000).result()
count=results.get_counts()
print(count)
print(results)
plot_histogram(count)
plt.title("Results")
plt.show()

