import cplex

def solve_optimization():
    problem = cplex.Cplex()
    problem.set_problem_type(cplex.Cplex.problem_type.MILP)

    # Define the objective function
    problem.objective.set_sense(problem.objective.sense.maximize)
    problem.variables.add(names=["XA", "XB", "XC"], obj=[30, 8, 15], types=[problem.variables.type.integer] * 3)

    # Define the constraints
    constraints = [
        [["XA", "XB", "XC"], [5, 10, 20]],  # Plant time constraint
        [["XA", "XB", "XC"], [18, 12, 5]],  # Raw material Y constraint
        [["XA", "XB", "XC"], [20, 5, 10]],  # Raw material Z constraint
        [["XC"], [1]]  # Constraint to ensure XC is at least 1
    ]
    rhs = [150, 216, 200, 1]
    senses = ["L", "L", "L", "G"]  # Less than or equal constraints, and the new constraint as greater than or equal

    problem.linear_constraints.add(lin_expr=constraints, senses=senses, rhs=rhs)

    problem.solve()

    # Show results
    print("Solution status:", problem.solution.get_status(), ":", problem.solution.get_status_string())
    print("Solution value:", problem.solution.get_objective_value())
    solution_values = problem.solution.get_values()
    print("Values of decision variables:")
    for i, name in enumerate(["XA", "XB", "XC"]):
        print(f"{name}: {solution_values[i]}")

if __name__ == "__main__":
    solve_optimization()
