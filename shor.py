from qiskit.visualization import plot_histogram
from math import gcd
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QFT
import matplotlib.pyplot as plt
def mod(a,power,n):
    return pow(a,power,n)
def shor_quantum(a,n):
    n_count=4
    qc=QuantumCircuit(n_count+4,n_count)
    for i in range(n_count):
        qc.h(i)
    for i in range(n_count):
        expo=2**i
        for _ in range(expo):
            qc.cx(i,n_count)
    qc.append(QFT(n_count,inverse=True),range(n_count))
    qc.measure(range(n_count),range(n_count))
    simulator=AerSimulator()
    compiled=transpile(qc,simulator)
    results=simulator.run(compiled,shots=1024).result()
    count=results.get_counts()
    print(qc.draw())
    return count
def getfact(a,n,count):
    for i in count:
        decimal=int(i,2)
        if decimal==0:
            continue
        r=(2**len(i))//decimal
        if r%2!=0:
            continue
        factor1=gcd(pow(a,r//2)-1,n)
        factor2=gcd(pow(a,r//2)+1,n)
        if factor1>1 and factor2>1:
            return factor1,factor2
    return None
def msdhoni(n):
    a=2
    if gcd(a,n)!=1:
        return gcd(a,n)
    print("running shor's algorithm for n =",n)
    count=shor_quantum(a,n)
    print("The measurement results are :",count)
    factors=getfact(a,n,count)
    if factors:
        print("The required factors are:",factors)
    else:
        print("Failed to find the required factors")
    plot_histogram(count)
    plt.title("Results")
    plt.show()
msdhoni(15)
    
    


    


