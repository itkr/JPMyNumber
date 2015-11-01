JPMyNumber
==========

JPMyNumber is Japanese common number of social security and tax
(=My Number) library.

.. code:: python

    JPMyNumber(123456789018)
    # this is valid

    JPMyNumber(123456789019)
    # JPMyNumberCheckDigitError


Installation
------------

::

    $ pip install JPMyNumber


Usage
-----

Validation
~~~~~~~~~~

.. code:: python

    from jpmynumber import JPMyNumber
    from jpmynumber.exceptions import JPMyNumberLengthError, JPMyNumberCheckDigitError

    try:
        JPMyNumber(123456789018)
    except JPMyNumberLengthError:
        print('length error')
    except JPMyNumberCheckDigitError:
        print('check digit error')


Creation
~~~~~~~~

.. code:: python

    from jpmynumber import JPMyNumber

    JPMyNumber.random_create()
    # <jpmynumber.core.JPMyNumber(123456789018)>


Corporation Number
------------------

It also supports the corporation number.

.. code:: python

    from jpmynumber import CorporationMyNumber

    CorporationMyNumber(9999999999999)
