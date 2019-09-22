.. pypacks documentation master file, created by
   sphinx-quickstart on Sun Sep 22 12:42:31 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pypacks's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


This is Shapes Package
========================

1. Shape Interface
*******************
.. automodule:: shapes.shape

.. autoclass:: shapes.shape.Shape
    :members: perimeter, area, name

2. Triangle Shape
*******************
.. automodule:: shapes.triangle

.. autoclass:: shapes.triangle.Triangle
    :members: is_equivalent, is_right_triangle

3. Rectangle Shape
*******************
.. automodule:: shapes.rectangle

.. autoclass:: shapes.rectangle.Rectangle
    :members: is_square
