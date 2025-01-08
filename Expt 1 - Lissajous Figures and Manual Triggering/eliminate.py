# from sympy import symbols, Eq, sin, cos, eliminate

# wt = symbols('wt')
# x = 2 * sin(wt)
# y = cos(wt)
# eq1 = Eq(x, 2 * sin(wt))
# eq2 = Eq(y, cos(wt))
# eq = eliminate([eq1, eq2], [wt])
# print(eq)

from sympy import symbols, Eq, sin, cos, solve

# Define the symbols
wt = symbols('wt')
x = symbols('x')
y = symbols('y')

# Define the equations
eq1 = Eq(x, 2 * sin(wt))
eq2 = Eq(y, cos(wt))

# Solve eq2 for wt (to get an expression for wt in terms of y)
sol_wt = solve(eq2, wt)

# Substitute the expression for wt into eq1
eq_sub = eq1.subs(wt, sol_wt[0])

# Simplify the resulting equation
result = solve(eq_sub, x**2 + 2*y**2)

print(result)

