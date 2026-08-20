import numpy as np

def derivative(fun):
    """returns derivative of function"""
    eps = 0.00001
    return lambda x: (fun(x+eps) - fun(x)) / eps

    
def optimize(start, fun):
    """returns value of Newton's method"""
    xt = start
    xt2 = xt-derivative(fun)(xt)/derivative(derivative(fun))(xt)
    while abs(xt2 - xt) > 0.0001:
        xt = xt2
        xt2 = xt-derivative(fun)(xt)/derivative(derivative(fun))(xt)
    return xt2


def multivariate(grad, hess, x0, tol=1e-6, max_iter=100):
    x = np.asarray(x0, dtype=float)
    for _ in range(max_iter):
        step = np.linalg.solve(hess(x), grad(x))   # H^-1 @ grad, without inverting
        x_new = x - step
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    return x