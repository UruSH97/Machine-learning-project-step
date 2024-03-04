# -*- coding: utf-8 -*-
"""Vectors.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dNpy46yF3y436s71d0d8TV0Fz2iOsIMt

# Vectors

In this document, we will look at the following concepts:

- Vector as a `NumPy` array
- Adding two vectors
- Element-wise multiplication of two vectors
- Scaling vectors
- Function of vectors (element-wise)
- Dot-product between two vectors
- Shape of a vector
- Vector of zeros
- Vector of ones

## Import

First we shall import the `NumPy` package.
"""

import numpy as np

"""## Vectors as `NumPy` arrays

Consider the following vector:

$$
\boldsymbol{x} = \begin{bmatrix}
1\\
2\\
3
\end{bmatrix}
$$

This is expressed as a `NumPy` array:
"""

x = np.array([1, 2, 3])
x

"""In the cell given above, `np.array` creates a `NumPy` array using a Python list that is passed as argument. Let us check the type of the object `x`:"""

type(x)

"""The term `ndarray` refers to an n-dimensional array. The idea of dimensions will become clear when we discuss matrices. For now, our focus will be one-dimensional arrays, or vectors.

## Vector addition

Addition is one of the elementary operations that can be performed on vectors. Given two vectors

$$
x = \begin{bmatrix}
1\\
2\\
3
\end{bmatrix}, y = \begin{bmatrix}
4\\
5\\
6
\end{bmatrix}
$$

we have:

$$
\boldsymbol{z} = \boldsymbol{x} + \boldsymbol{y}= \begin{bmatrix}
5\\
7\\
9
\end{bmatrix}
$$

In `NumPy` this is expressed as:
"""

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

z = x + y
z

"""Notice that `NumPy` arrays behave differently from Python lists. The `+` operator applied to two Python lists would result in list concatenation. However, the `+` operator applied to two `NumPy` arrays results in element-wise addition.

## Element-wise multiplication

Element-wise multiplication of two vectors is called the Hadamard product. The operator corresponding to it is $\odot$. For example, given two vectors:

$$
x = \begin{bmatrix}
1\\
2\\
3
\end{bmatrix}, y = \begin{bmatrix}
4\\
5\\
6
\end{bmatrix}
$$

we have:

$$
\boldsymbol{z} = \boldsymbol{x} \odot \boldsymbol{y}= \begin{bmatrix}
4\\
10\\
18
\end{bmatrix}
$$

In `NumPy` this is expressed as:
"""

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

z = x * y
z

"""## Scaling vectors

If $\boldsymbol{x}$ is a vector, scaling it by a constant $k$ is equivalent to element-wise multiplication by $k$. For example, given

$$
\boldsymbol{x} = \begin{bmatrix}
1\\
2\\
3
\end{bmatrix}
$$

we have:

$$
y = 3 \boldsymbol{x} = \begin{bmatrix}
3\\
6\\
9
\end{bmatrix}
$$

As you might have guessed by now, in `NumPy` this is as simple as:
"""

x = np.array([1, 2, 3])
y = 3 * x
y

"""Again note that this is different from what you would expect with a Python list. The `*` operator for lists would result in replication. Besides, we can multiply a `NumPy` array by any real number, even $0$:"""

x = np.array([1, 2, 3])
y = 0 * x
y

"""## Element-wise functions of vectors

Scaling a vector $\boldsymbol{x}$ by a constant $k$ can be seen as the output of the following function:

$$
f(\boldsymbol{x}) = \begin{bmatrix}
kx_1\\
\cdots\\
kx_m
\end{bmatrix}
$$

This is nothing but the function $f(x) = kx$ applied element-wise. `NumPy` extends this feature for any arbitrary function. For example, consider the function $g(x) = x^2$. This can be applied element-wise:

$$
g(\boldsymbol{x}) = \begin{bmatrix}
x_1^2\\
\cdots\\
x_m^2
\end{bmatrix}
$$

In `NumPy`, this translates to:
"""

x = np.array([1, 2, 3, 4])
y = x ** 2
y

"""We can take up more complex functions as well. For example, let us take the case of `np.log10`, which is $\log_{10}$:"""

x = np.array([1, 10, 100, 1000, 10000, 100000])
y = np.log10(x)
y

"""Usually, we will stick to the natural logarithm or $\log_e$. This is given by `np.log`."""

x = np.array([1, np.e, np.e ** 2])
y = np.log(x)
y

"""## Dot Product

The dot product between two vectors $\mathbf{x}$ and $\mathbf{y}$ is given as follows:

$$
z = \mathbf{x} \cdot \mathbf{y} = \sum \limits_{j = 1}^{m} x_j y_j
$$

In `NumPy`, this could be done as follows:
"""

x = np.array([1, 2, 3, 4])
y = np.array([-4, -5, -6, -7])

z = np.dot(x, y)
z

"""## Shape of a vector

All `NumPy` arrays have an attribute called `shape`. The shape is a tuple. For vectors (single-dimensional) the shape is of the form $(n, )$, where $n$ is the number of components in the vector.
"""

x = np.array([10, 20, 30, 40])
x.shape

"""For a vector, the following relationship always holds good:"""

x = np.array([10, 20, 30, 40])
x.shape[0] == len(x)

"""## Vector of zeros or ones

On many occassions, we might want to create a `NumPy` array all of whose elements are zeros or ones or some other constant. If we want a vector of zeros, one way would be as follows:
"""

x = np.array([0 for _ in range(4)])
x

"""Here, `NumPy` provides a method that makes our job even simpler:"""

x = np.zeros(4)
x

"""For a vector of ones, we have"""

x = np.ones(6)
x

"""What about a vector where all the elements are equal to $2$? How can we do that? This is left as an exercise to the reader."""