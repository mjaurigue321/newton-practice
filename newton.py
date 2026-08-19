def derivative(fun):
    eps = 0.00001
    return lambda x: (fun(x+eps) - fun(x)) / eps

    
def optimize(start, fun):
    xt = start
    xt2 = xt-derivative(fun)(xt)/derivative(derivative(fun))(xt)
    while abs(xt2 - xt) > 0.0001:
        xt = xt2
        xt2 = xt-derivative(fun)(xt)/derivative(derivative(fun))(xt)
    return xt2
