import numpy as np
from pytest import raises, fail

from depynd.markov_networks import select

X = np.random.multivariate_normal(np.zeros(2), np.eye(2), 10)
x = np.random.normal(0, 1, 10)


class TestSelect:
    def test_dimension(self):
        try:
            select(X)
        except ValueError:
            fail()
        with raises(ValueError):
            select(x)

    def test_length(self):
        with raises(ValueError):
            select(X[:, :1])
        with raises(ValueError):
            select(X[:1])
