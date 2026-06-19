from qiskit import  QuantumCircuit
import string
from qiskit_aer import AerSimulator
def Randomnumber(numbits):
    simulator=AerSimulator()
    initial=""
    for _ in range(numbits):
        qc=QuantumCircuit(1,1)
        qc.h(0)
        qc.measure(0,0)
        results=simulator.run(qc,shots=1).result()
        count=results.get_counts()
        new=list(count.keys())[0]
        initial+=new
    return initial
def quantumnumber(max_value):
    bits=max_value.bit_length()
    while True:
        bit_string=Randomnumber(bits)
        number=int(bit_string,2)
        if number<max_value:
            return number
        
def Generate_Quantumpass(length):
    characters=(string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits)
    password=""
    for _ in range(length):
        randomindex=quantumnumber(len(characters))
        password+=characters[randomindex]
    return password
def call_function():
    len=int(input("Enter the length of the password to be generated:"))
    noun=Generate_Quantumpass(len)
    print("The requested password is:  ",noun)
call_function()

    


        
