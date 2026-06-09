from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
def adder(a,b):
    qc=QuantumCircuit(3,2)
    if a==1:
        qc.x(0)
    if b==1:
        qc.x(1)
#ccx gate calculates the carry out for the full adder
    qc.ccx(0,1,2)

#cx calculates the sum of a and b
    qc.cx(0,1)

    qc.measure(1,0)#sum

    qc.measure(2,1)#carry
    simulator=AerSimulator()
    complied=transpile(qc,simulator)
    RESULTS=simulator.run(complied,shots=1).result()
    counts=RESULTS.get_counts()
    output=list(counts.keys())[0]
    sumbit=output[1]
    carry=output[0]
    print("A =",a)
    print("B=",b)
    print("the required sum is ",sumbit)

    print("the required carryout is ",carry)
m=int(input("enter first number A:"))    
s=int(input("enter second number B"))
adder(m,s)
