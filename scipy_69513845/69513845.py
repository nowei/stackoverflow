import scipy.optimize as opt
from math import exp 

eq_list = ["x + y**2 = 4", "exp(x) + x*y = 3"]
eq_list_altered = []
for eq in eq_list:
    start, end = eq.split('=')
    eq_list_altered.append(start + '-' + end)

def f(variables) :
    (x,y) = variables
    res = []
    for eq in eq_list_altered:
        res.append(eval(eq))
    return res

solution = opt.fsolve(f, (0.1, 1))
print(solution)