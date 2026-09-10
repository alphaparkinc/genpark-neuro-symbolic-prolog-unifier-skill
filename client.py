class RobinsonUnifier:
    """
    First-Order Logic Robinson Unification Engine.
    Unifies terms: constants (strings), variables (?X, ?Y), and compound terms (functor, [args]).
    """
    def is_var(self, term):
        return isinstance(term, str) and term.startswith("?")

    def unify(self, x, y, theta=None):
        if theta is None:
            theta = {}
        if theta is False:
            return False
        elif x == y:
            return theta
        elif self.is_var(x):
            return self.unify_var(x, y, theta)
        elif self.is_var(y):
            return self.unify_var(y, x, theta)
        elif isinstance(x, tuple) and isinstance(y, tuple):
            if len(x) != len(y) or x[0] != y[0]:
                return False
            for arg_x, arg_y in zip(x[1:], y[1:]):
                theta = self.unify(arg_x, arg_y, theta)
                if theta is False:
                    return False
            return theta
        return False

    def unify_var(self, var, x, theta):
        if var in theta:
            return self.unify(theta[var], x, theta)
        elif self.is_var(x) and x in theta:
            return self.unify(var, theta[x], theta)
        else:
            theta[var] = x
            return theta
