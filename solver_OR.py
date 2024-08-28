# written by Narges Chinichian, Aug 2024
# solution to example Operations Research problem in the lecture by Shahriar Shahriari
# The lecture could be watched here: https://www.youtube.com/watch?v=NJLWW6K1oz4

import pulp

# Define the type of the problem
problem = pulp.LpProblem("Simple LP Problem", pulp.LpMaximize)

# Define the decision variables
x1 = pulp.LpVariable('x1', lowBound=0) #type one gallons
x2 = pulp.LpVariable('x2', lowBound=0) #type two gallons

# Define the objective function
problem += 25 * x1 + 20 * x2, "Objective"

# Define the constraints
problem += x1 + 2 * x2 <= 6 #division does not work in LP, we need to multiply our inequalities from the video by 3
problem += 2 * x1 + x2 <= 9
problem += x2 <= 2
problem += -1 * x1 + x2 <= 1
#sign constrants are included in the lowBound


# Solve the problem using CBC
problem.solve(pulp.PULP_CBC_CMD())


# to solve the problem using other solvers uncomment one of the following blocks and comment the CBC one above:
"""
cplex solver from IBM
for cplex, you need to have cplex on your system first, see here: https://www.ibm.com/docs/en/icos/20.1.0?topic=2010-installing-cplex-optimization-studio
then you need to give the location of the solver on your system as an input below:
we call that path_to_cplex
"""
# path_to_cplex = '/Applications/CPLEX_Studio_Community2211/cplex/bin/arm64_osx/cplex' #adjust this path for your installation
# problem.solve(pulp.CPLEX_CMD(path=path_to_cplex))

"""
gurobi solver
for this you need to install gurobi and activate a license [academic license is free]. 
See below for more information:
https://support.gurobi.com/hc/en-us/articles/4534161999889-How-do-I-install-Gurobi-Optimizer
"""
# problem.solve(pulp.GUROBI_CMD())

# Print the results
print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"x1 = {pulp.value(x1)}")
print(f"x2 = {pulp.value(x2)}")




