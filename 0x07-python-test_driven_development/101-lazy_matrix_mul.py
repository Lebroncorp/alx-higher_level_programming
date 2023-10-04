#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using the module NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    m_a is !st matrix list and m_b 2nd matrix list"""

    return (np.matmul(m_a, m_b))
