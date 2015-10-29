JPMyNumber
=========================

JPMyNumber is Japanese common number of social security and tax (=My Number) library.

.. code-block:: python

    JPMyNumber(123456789018)
    # this is valid

    JPMyNumber(123456789019)
    # JPMyNumberCheckDigitError


Installation
------------

To install Requests, simply:

.. code-block:: bash

    $ pip install JPMyNumber


Usage
------------

Validation
^^^^^^^^

.. code-block:: python

    from jpmynumber import JPMyNumber
    from jpmunumber.exceptions import JPMyNumberLengthError, JPMyNumberCheckDigitError

    try:
        JPMyNumber(123456789018)
    except JPMyNumberLengthError:
        print('length error')
    except JPMyNumberCheckDigitError:
        print('check digit error')


Creation
^^^^^^^^

.. code-block:: python

    from jpmynumber import JPMyNumber

    JPMyNumber.random_create()
    # <jpmynumber.core.JPMyNumber(123456789018)>
