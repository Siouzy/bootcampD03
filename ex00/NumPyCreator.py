import numpy as np


class NumPyCreator:
    def from_list(self, lst):
        return np.asarray(lst)

    def from_tuple(self, tpl):
        return np.asarray(tpl)

    def from_iterable(self, itr):
        return np.asarray(itr)

    def from_shape(self, shape, value=0):
        return np.full(shape, value)

    def random(self, shape):
        return np.array(np.random.random_sample(size=shape))

    def identity(self, n):
        return np.identity(n)
