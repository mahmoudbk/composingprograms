def square(x):
    return x*x

def successor(x):
    return x+1

def compose(f,g):
    def h(x):
        return f(g(x))

    return h
composed = compose(successor,square)
print(composed(2))
#>>>5