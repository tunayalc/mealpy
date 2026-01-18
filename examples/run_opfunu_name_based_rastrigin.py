#!/usr/bin/env python
# Example: Using an `opfunu.name_based` benchmark objective function with Mealpy.
#
# Note: This script depends on an `opfunu` version that includes the added name-based
# benchmarks (e.g., install from this fork/branch instead of PyPI).

from opfunu.name_based.r_func import Rastrigin
from mealpy import FloatVar, PSO


## Define objective function (Opfunu)
f = Rastrigin(ndim=30)

problem = {
    "bounds": FloatVar(lb=f.lb, ub=f.ub, name="x"),
    "obj_func": f.evaluate,
    "minmax": "min",
    "name": "Rastrigin",
    "log_to": "console",
}

model = PSO.OriginalPSO(epoch=200, pop_size=50)
g_best = model.solve(problem, seed=10)
print(f"Best fitness: {g_best.target.fitness}")
