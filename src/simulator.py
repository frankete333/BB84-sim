from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import random

# Reduce number of qubits to a more manageable amount for better performance
number_of_qubits = 1000
is_channel_compromised = True
e_read_probability = 1
A_bit_values = []
A_hadamard_applied = []

B_bit_values = []
B_hadamard_applied = []

qc = QuantumCircuit(number_of_qubits, number_of_qubits)

for i in range(number_of_qubits):
  # Decido si el qubit es 0 o 1
  if random.randint(0, 1) <= 0.5:
    A_bit_values.append(False)
  else:
    A_bit_values.append(True)
    qc.x(i)

  # Decido si aplicar hadamard
  if random.randint(0, 1) <= 0.5:
    A_hadamard_applied.append(True)
    qc.h(i)
  else:
    A_hadamard_applied.append(False)

# Simulo el canal comprometido
if is_channel_compromised:
  for i in range(number_of_qubits):
    if random.randint(0, 1) <= e_read_probability:
      if random.randint(0, 1) <= 0.5:
        qc.h(i)
      qc.measure(i, i)

# B lee los qubits de A y aplica hadamard
for i in range(number_of_qubits):
  if random.randint(0, 1) <= 0.5:
    B_hadamard_applied.append(True)
    qc.h(i)
  else:
    B_hadamard_applied.append(False)
  qc.measure(i, i)

simulator = AerSimulator(method='stabilizer', max_parallel_experiments=1)
job = simulator.run(qc, shots=1)
result = job.result()

counts = result.get_counts()
measurement_result = list(counts.keys())[0]

for i in range(number_of_qubits):
  bit_value = int(measurement_result[-(i+1)])
  B_bit_values.append(bool(bit_value))

matching_hadamard_applied = 0
matching_results_when_hadamard_not_applied = 0

A_matching_hadamard_results = []
B_matching_hadamard_results = []

for i in range(number_of_qubits):
  if A_hadamard_applied[i] == B_hadamard_applied[i]:
    A_matching_hadamard_results.append(A_bit_values[i])
    B_matching_hadamard_results.append(B_bit_values[i])

cont_of_matching_hadamard_applied = len(A_matching_hadamard_results)

indices = list(range(cont_of_matching_hadamard_applied))
random_indices = random.sample(indices, int(cont_of_matching_hadamard_applied/2))
remaining_indices = list(set(indices) - set(random_indices))

matching_results = 0
wrong_results = 0
for i in random_indices:
  if A_matching_hadamard_results[i] == B_matching_hadamard_results[i]:
    matching_results += 1
  else:
    wrong_results += 1

print(f"Matching results: {matching_results}")
print(f"Wrong results: {wrong_results}")
print(f"Total qubits with matching basis: {cont_of_matching_hadamard_applied}")











