.. Django Featurette documentation master file, created by
   sphinx-quickstart on Wed Jan  7 15:51:09 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django Featurette's documentation!
=============================================

Django Featurette is a simple application that helps your website to offer
certain feature only to selected users.

Suppose for example that you have one or more groups of *premium* users, and
that a given page is only visible to a certain group, or that a section of an
otherwise public page should be rendered only for another group.

There are three ways to achieve that goals with Featurette:

* Using a decorator on a view
* Wrapping within a template tag a section of your template
* Fine-grained control through helper methods

We are going to show all these methods in the :doc:`usage` guide.

Contents:

.. toctree::
   :maxdepth: 2

   quickstart
   usage
   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

