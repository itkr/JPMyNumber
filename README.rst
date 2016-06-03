JPMyNumber
==========

JPMyNumber is Japanese common number of social security and tax
(=My Number) library.

.. code:: python

    # this is valid
    IndividualNumber('123456789018')

    # JPMyNumberCheckDigitError
    IndividualNumber('123456789019')


Installation
------------

::

    $ pip install JPMyNumber


Usage
-----

Validation
~~~~~~~~~~

.. code:: python

    from jpmynumber import IndividualNumber
    from jpmynumber.exceptions import JPMyNumberLengthError, JPMyNumberCheckDigitError

    try:
        IndividualNumber('123456789018')
    except JPMyNumberLengthError:
        print('length error')
    except JPMyNumberCheckDigitError:
        print('check digit error')


Creation
~~~~~~~~

.. code:: python

    from jpmynumber import IndividualNumber

    IndividualNumber.random_create()
    # <jpmynumber.individual.IndividualNumber('123456789018')>


Important Point
---------------

If the first letter is '0' you should use string.

.. code:: python

    # this is valid
    IndividualNumber(111111111118)

    # this is valid
    IndividualNumber('000111111111')

    # error
    IndividualNumber(000111111111)


Legal Entity Number
-------------------

It also supports legal entity numbers.

.. code:: python

    from jpmynumber import LegalEntityNumber

    LegalEntityNumber('9999999999999')

It has legal entity number classes of various types

* CorporationNumber
* LocalGovernmentNumber
* LocalGovernmentNumberWithCode
* LocalGovernmentNumberWithoutCode
* OtherOrganizationNumber
* StateOrgansNumber
