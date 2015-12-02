JPMyNumber
==========

JPMyNumber is Japanese common number of social security and tax
(=My Number) library.

.. code:: python

    # this is valid
    JPMyNumber('123456789018')

    # JPMyNumberCheckDigitError
    JPMyNumber('123456789019')


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
        JPMyNumber('123456789018')
    except JPMyNumberLengthError:
        print('length error')
    except JPMyNumberCheckDigitError:
        print('check digit error')


Creation
~~~~~~~~

.. code:: python

    from jpmynumber import JPMyNumber

    JPMyNumber.random_create()
    # <jpmynumber.core.JPMyNumber('123456789018')>


Important Point
---------------

If the first letter is '0' you should use string

.. code:: python

    # this is valid
    JPMyNumber(111111111118)

    # this is valid
    JPMyNumber('000111111111')

    # error
    JPMyNumber(000111111111)


Corporation Number
------------------

It also supports the corporation number.

.. code:: python

    from jpmynumber import CorporationMyNumber

    CorporationMyNumber('9999999999999')
