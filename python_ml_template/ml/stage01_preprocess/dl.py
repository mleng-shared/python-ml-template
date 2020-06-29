"""
Manages downloading raw data for later preprocessing.
"""

import sklearn.datasets


def load_dataset():
    return sklearn.datasets.load_iris(as_frame=True)['data']
