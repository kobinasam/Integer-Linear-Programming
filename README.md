# Integer-Linear-Programming
An integer linear programming with thousand variables to compare the running time between parallels and without parallels using Gurobi

First create a new environment and model using the GRBEnv and GRBModel classes. Then we create a thousand binary variables x using the addVars method, set the objective function to minimize the sum of these variables using the setObjective method, and add constraints using the addConstr method.

To set the number of threads for without parallel and parallel optimization, we use the GRB.IntParam.Threads parameter from the environment, and we optimize the model using the optimize method.

Finally, we print the optimal solution for both parallel and without parallel optimization to compare the run time using the get method.
