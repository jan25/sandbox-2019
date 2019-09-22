.. pypacks documentation master file, created by
   sphinx-quickstart on Sun Sep 22 12:42:31 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pypacks's documentation!
===================================

This is Shapes Package
========================

Shape Interface
*******************
.. automodule:: shapes.shape

.. autoclass:: shapes.shape.Shape
    :members: perimeter, area, name

Implementations
****************

.. toctree::
   :maxdepth: 2
   
   triangle.rst
   rectangle.rst
