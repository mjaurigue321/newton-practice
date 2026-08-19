def derivative(fun):
    """returns derivative of function"""
    eps = 0.00001
    return lambda x: (fun(x+eps) - fun(x)) / eps

    
def optimize(start, fun):
    """returns value of Newton's method"""
    xt = start
    xt2 = xt-derivative(fun)(xt)/derivative(derivative(fun))(xt)
    while abs(xt2 - xt) > 0.01:
        xt = xt2
        xt2 = xt-derivative(fun)(xt)/derivative(derivative(fun))(xt)
    return xt2