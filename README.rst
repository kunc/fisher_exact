========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1
    * - tests
      - | |requires|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|

.. |requires| image:: https://requires.io/github/kunc/fisher_exact/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/kunc/fisher_exact/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/fisher_exact.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/fisher_exact

.. |wheel| image:: https://img.shields.io/pypi/wheel/fisher_exact.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/fisher_exact

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/fisher_exact.svg
    :alt: Supported versions
    :target: https://pypi.org/project/fisher_exact

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/fisher_exact.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/fisher_exact

.. end-badges

Python wrapper over fishers_exact function implemented in Rust

Installation
============

::

    pip install fisher_exact


Examples
========

Example:

.. code-block:: python

    from fisher_exact import fisher_exact
    table = [[1, 9], [11, 3]]
    pval = fisher_exact(table, alternative='two-sided')
    print(pval)



Why not ``fisher_exact`` from ``scipy.stats``?
==========================================

The only reason this mini-library exists is because I needed to compute the Fisher's exact test pretty quickly quite often and the profiler showed that I spend most time in the ``scipy.stats.fisher_exact``.
    

Credits
=======

* The underlying Rust implementation: https://github.com/cpearce/fishers_exac

