Processing Documentation
========================

This page contains the Processing Package documentation.

Subpackages
-----------

.. toctree::

    processing.mln
    processing.conceptnet

The :mod:`alchemy_api` Module
-----------------------------

.. automodule:: processing.alchemy_api
    :members:
    :undoc-members:
    :show-inheritance:

The :mod:`concepts` Module
--------------------------

.. automodule:: processing.concepts
    :members:
    :undoc-members:
    :show-inheritance:

The :mod:`tagger` Module
------------------------

.. automodule:: processing.tagger
    :members:
    :undoc-members:
    :show-inheritance:

The :mod:`stopwords` Module
---------------------------

.. automodule:: processing.stopwords
    :members:
    :undoc-members:
    :show-inheritance:

The :mod:`sentence` Module
--------------------------

.. automodule:: processing.sentence
    :members:
    :undoc-members:
    :show-inheritance:

The :mod:`sentence_helper` Module
---------------------------------

.. automodule:: processing.sentence_helper
    :members:
    :undoc-members:
    :show-inheritance:

.. testsetup:: *
   from processing.sentence_helper import sentence_helper

>>> s = sentence_helper()
... s.tokenize('the quick brown fox')
['the', 'quick', 'brown', 'fox']


The :mod:`calais_api` Module
----------------------------

.. automodule:: processing.calais_api
    :members:
    :undoc-members:
    :show-inheritance:

