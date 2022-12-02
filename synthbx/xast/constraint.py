from synthbx.xast.literal import Literal
from synthbx.xast.cmp import Cmp
from synthbx.xast.variable import Variable
from synthbx.xast.constant import Constant


class Constraint(Literal):
    def __init__(self, cmp, var, const):
        self.cmp = Cmp(cmp)
        self.var = var
        self.const = const

    def __str__(self):
        return f'{self.var} {self.cmp.value} {self.const}'

    def __eq__(self, other):
        if isinstance(other, Literal):
            return self.__str__() == other.__str__()
        else:
            raise TypeError()

    def __lt__(self, other):
        if isinstance(other, Constraint):
            return self.__str__() < other.__str__()
        else:
            raise TypeError()

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())
