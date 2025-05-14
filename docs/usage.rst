Usage
=====

.. _installation:

Installation
------------

To use mymodule, first install it using pip:

.. code-block:: console

   pip install mymodule

This is just dummy text. pip won't install mymodule since it doesn't exist!

Lines!
----------------

To make a beautiful line you can use the ``mymodule.script1.line()`` function:

.. autofunction:: mymodule.script1.line

The ``x``, ``m`` and ``b`` parameters are the independent variable, slope and intercept.

For example:

>>> from mymodule.script1 import line
>>> import numpy as np
>>> line(x=np.array([0,1]), m=1, b=1)
array([1, 2])