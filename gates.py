import numpy as np

# importing Qiskit
from qiskit import IBMQ, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, assemble, transpile
from qiskit.circuit.library import MCXGate
from mtable import addcmm_matrix


def traversal(n) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    for i in range(n):
        qc.h(i)
    qc.name = "H*%i" % n
    return qc


def cnots(n):
    qc = QuantumCircuit(n*2)
    for i in range(n):
        qc.cnot(i+n, i)
    qc.name = "CNOT*%i" % n
    return qc


def xs(n):
    qc = QuantumCircuit(n)
    for i in range(n):
        qc.x(i)
    qc.name = "X * n"
    return qc


def shift12():
    qc = QuantumCircuit(2)
    qc.cnot(0, 1)
    qc.x(0)
    qc.name = "shift 2 1"
    return qc


def shift1(n):
    qc = QuantumCircuit(n)
    for i in range(n-1, 0, -1):
        qc.mcx(list(range(0, i)), i)
    qc.x(0)
    qc.name = "Shift1%i" % n
    return qc


def toffoli23():
    qc = QuantumCircuit(6)
    qc.ccx(5, 2, 1)
    qc.ccx(4, 3, 1)
    qc.mcx([4, 2, 0], 1)
    qc.ccx(4, 2, 0)
    qc.name = "Toffoli2_3"
    return qc


def toffoli7():
    qc = QuantumCircuit(7)
    qc.ccx(5, 2, 1)
    qc.ccx(4, 3, 1)
    qc.mcx([4, 2, 0], 1)
    qc.ccx(4, 2, 0)
    qc.name = "Toffoli7"
    return qc



def mul8():
    qc = QuantumCircuit(8,8)
    qc.append(traversal(6), range(2,8))
    qc.append(cnots(2), range(4))
    qc.append(xs(2), range(2))
    qc.append(shift1(2), range(2))
    qc.append(toffoli23(), [0,1,4,5,6,7])
    qc.barrier()
    for i in range(8):
        qc.measure(i, i)
    return qc


def mul4():
    qc = QuantumCircuit(4,4)
    qc.append(traversal(3), range(1,4))
    qc.cx(1,0)
    qc.x(0)
    qc.x(0)
    qc.ccx(3,2,0)
    qc.barrier()
    for i in range(4):
        qc.measure(i,i)
    return qc


def mul16():
    qc = QuantumCircuit(16,16)
    qc.append(traversal(12),range(4,16))
    qc.append(cnots(4),range(8))
    qc.append(xs(4),range(4))
    qc.append(shift1(4), range(4))
    qc.unitary(addcmm_matrix(4), list(range(4))+list(range(8,16)), "GToffoli")
    qc.barrier()
    for i in range(16):
        qc.measure(i,i)
    return qc


def toffoli123():
    qc = QuantumCircuit(6)
    qc.mcx([0, 3, 4, 5], 2)
    qc.mcx([0, 1, 3, 5], 2)
    qc.mcx([1, 4, 5], 2)
    qc.mcx([0, 3, 5], 1)
    qc.ccx(5, 4, 1)
    qc.ccx(5, 3, 0)
    qc.name = "GToffoli 1 2 3"
    return qc


def toffoli124():
    qc = QuantumCircuit(7)

    qc.mcx([0, 4, 5, 6, 2], 3)
    qc.mcx([0, 1, 4, 6, 2], 3)
    qc.mcx([1, 5, 6, 2], 3)
    qc.mcx([0, 4, 5, 6], 2)
    qc.mcx([0, 1, 4, 6], 2)
    qc.mcx([1, 5, 6], 2)
    qc.mcx([0, 4, 6], 1)
    qc.ccx(6, 5, 1)
    qc.ccx(6, 4, 0)
    qc.name = "GToffoli 1 2 4"
    return qc


def toffoli125():
    qc = QuantumCircuit(8)

    qc.mcx([0, 5, 6, 7, 2, 3], 4)
    qc.mcx([0, 1, 5, 7, 2, 3], 4)
    qc.mcx([1, 6, 7, 2, 3], 4)
    qc.mcx([0, 5, 6, 7, 2], 3)
    qc.mcx([0, 1, 5, 7, 2], 3)
    qc.mcx([1, 6, 7, 2], 3)
    qc.mcx([0, 5, 6, 7], 2)
    qc.mcx([0, 1, 5, 7], 2)
    qc.mcx([1, 6, 7], 2)
    qc.mcx([0, 5, 7], 1)
    qc.ccx(7, 6, 1)
    qc.ccx(7, 5, 0)
    qc.name = "GToffoli 1 2 5"
    return qc


def mul9():
    qc = QuantumCircuit(9,9)
    qc.append(traversal(6), range(3,9))
    qc.append(cnots(3), range(6))
    qc.append(xs(3), range(3))
    qc.append(shift1(3), range(3))
    qc.append(toffoli123(), [0, 1, 2, 6, 7, 8])
    qc.barrier()
    for i in range(9):
        qc.measure(i, i)
    qc.name = 'Multiplication 1,2-3'
    return qc


def mul124():
    qc = QuantumCircuit(11, 11)
    qc.append(traversal(7), range(4, 11))
    qc.append(cnots(4), range(8))
    qc.append(xs(4), range(4))
    qc.append(shift1(4), range(4))
    qc.append(toffoli124(), [0, 1, 2, 3, 8, 9, 10])
    qc.barrier()
    for i in range(11):
        qc.measure(i, i)
    qc.name = 'Multiplication 1,2-4'
    return qc


def mul125():
    qc = QuantumCircuit(13, 13)
    qc.append(traversal(8), range(5, 13))
    qc.append(cnots(5), range(10))
    qc.append(xs(5), range(5))
    qc.append(shift1(5), range(5))
    qc.append(toffoli125(), [0, 1, 2, 3, 4, 10, 11, 12])
    qc.barrier()
    for i in range(13):
        qc.measure(i, i)
    qc.name = 'Multiplication 1,2-5'
    return qc


def mul125_diff():
    qc = QuantumCircuit(13, 13)
    qc.append(traversal(7), list(range(5, 9)) + list(range(10, 13)))
    qc.x(9)
    qc.append(cnots(5), range(10))
    qc.append(xs(5), range(5))
    qc.append(shift1(5), range(5))
    qc.append(toffoli125(), [0, 1, 2, 3, 4, 10, 11, 12])
    qc.barrier()
    for i in range(13):
        qc.measure(i, i)
    qc.name = 'Multiplication 1,2-5 Diff'
    return qc


def qot():
    qc = QuantumCircuit(5,4)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.ccx(3, 1, 0)
    qc.x(1)
    qc.ccx(2, 1, 0)
    qc.x(1)
    qc.barrier()
    for i in range(4):
        qc.measure(i,i)
    qc.name = 'QOT'
    return qc

# def mul126():
#     qc = QuantumCircuit(15, 15)
#     qc.append(traversal(9), range(6, 15))
#     qc.append(cnots(6), range(12))
#     qc.append(xs(6), range(6))
#     qc.append(shift1(6), range(6))
#     qc.append(toffoli126(), [0, 1, 2, 3, 4, 5, 12, 13, 14])
#     qc.barrier()
#     for i in range(15):
#         qc.measure(i, i)
#     qc.name = 'Multiplication 1,2-6'
#     return qc

def costume_ccx():
    qc = QuantumCircuit(3)
    qc.sx()
