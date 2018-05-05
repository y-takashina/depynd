from depynd.feature_selection import mrmr, mifs


def select(X, y, lamb=0.0, method='mifs'):
    """Select effective features in X on predinting y using
    Parameters
    ----------
    X : array_like, shape (n_samples, d)
        Features.
    y : array_like, shape (n_samples)
        Target. Can be either continuous or discrete.
    lamb: float, default 0.0
        Threshold for independence tests.
    method: str, default 'mifs'
        Method used for feature selection. Either 'mifs' or
        'mrmr' can be chosen.
    Returns
    -------
    indices : list
        Indices for the selected features.
    """
    if method == 'mifs':
        return mifs(X, y, lamb=lamb, method='knn', options=None)
    elif method == 'mrmr':
        return mrmr(X, y, lamb=lamb, method='knn', options=None)
    else:
        raise NotImplementedError('Method %s is not implemented. Use mifs or mrmr.' % method)
