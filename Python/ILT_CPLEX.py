import cplex
from cplex.exceptions import CplexError
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import time
import matplotlib.pyplot as plt


num_vars = 1000
c = np.random.rand(num_vars)
A = np.random.rand(num_vars, num_vars)
b = np.random.rand(num_vars)

problem = cplex.Cplex()
problem.objective.set_sense(problem.objective.sense.maximize)

problem.variables.add(obj=c)

for i in range(num_vars):
    problem.linear_constraints.add(lin_expr=[cplex.SparsePair(ind=list(range(num_vars)), val=A[i])], rhs=[b[i]])

start_time = time.time()
problem.solve()
no_parallel_time = time.time() - start_time
print("Solution time without parallel:", no_parallel_time)

problem.parameters.threads.set(0)
start_time = time.time()
problem.solve()
parallel_time = time.time() - start_time
print("Solution time with parallel:", parallel_time)

# Visualize the results
x = np.array(problem.solution.get_values())
fig, ax = plt.subplots()
ax.bar(range(num_vars), x)
ax.set_title("Graphical Representation of The Solution")
ax.set_xlabel("Variable Index")
ax.set_ylabel("Variable Value")
plt.show()

