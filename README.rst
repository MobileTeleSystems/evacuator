.. title

Evacuator
=========

|Repo Status| |PyPI| |PyPI License| |PyPI Python Version|
|Documentation| |Build Status| |Coverage|

.. |Repo Status| image:: https://www.repostatus.org/badges/latest/active.svg
    :target: https://www.repostatus.org/#active
.. |PyPI| image:: https://img.shields.io/pypi/v/evacuator
    :target: https://pypi.org/project/evacuator/
.. |PyPI License| image:: https://img.shields.io/pypi/l/evacuator.svg
    :target: https://github.com/MobileTeleSystems/evacuator/blob/develop/LICENSE.txt
.. |PyPI Python Version| image:: https://img.shields.io/pypi/pyversions/evacuator.svg
    :target: https://badge.fury.io/py/evacuator
.. |ReadTheDocs| image:: https://img.shields.io/readthedocs/evacuator.svg
    :target: https://evacuator.readthedocs.io
.. |Build Status| image:: https://github.com/MobileTeleSystems/evacuator/workflows/Tests/badge.svg
    :target: https://github.com/MobileTeleSystems/evacuator/actions
.. |Documentation| image:: https://readthedocs.org/projects/evacuator/badge/?version=stable
    :target: https://evacuator.readthedocs.io/en/stable/
.. |Coverage| image:: https://codecov.io/gh/MobileTeleSystems/evacuator/branch/develop/graph/badge.svg?token=CM6AQWY65P
    :target: https://codecov.io/gh/MobileTeleSystems/evacuator

What is Evacuator?
------------------

Decorator/context manager designed to catch a certain exception and exit with specific exit code.

Designed to be used in `Apache Airflow <https://airflow.apache.org/>`__ with:
    * ``BashOperator``
    * ``SSHOperator``
    * ``DockerOperator``
    * ``KubernetesPodOperator``
    * any other operator which can handle process exit codes.

.. installation

How to install
---------------

.. code:: bash

    pip install evacuator

.. documentation

Documentation
-------------

See https://evacuator.readthedocs.io/

.. contribution

Contribution guide
-------------------

See `<CONTRIBUTING.rst>`__

.. security

Security
-------------------

See `<SECURITY.rst>`__

.. develops

Develop
-------

Clone repo
~~~~~~~~~~

Clone repo:

.. code:: bash

    git clone git@github.com:MobileTeleSystems/evacuator.git -b develop

    cd evacuator

Setup environment
~~~~~~~~~~~~~~~~~

Create virtualenv:

.. code:: bash

    python -m venv venv
    source venv/bin/activate
    pip install -U wheel
    pip install -U pip setuptools

Install dependencies for development:

.. code:: bash

    # install linters, formatters, etc
    pip install -U -r requirements-dev.txt

Enable pre-commit hooks
~~~~~~~~~~~~~~~~~~~~~~~

Install pre-commit hooks:

.. code:: bash

    pre-commit install --install-hooks

Test pre-commit hooks run:

.. code:: bash

    pre-commit run

Run tests
~~~~~~~~~

.. code:: bash

    # install requirements for testing
    pip install -U -r requirements-test.txt

    # run tests
    pytest

Build documentation
~~~~~~~~~~~~~~~~~~~

.. code:: bash

    # install requirements for documentation
    pip install -U -r requirements-docs.txt

    cd docs

    # generate html documentation
    make html

Then open ``docs/_build/html/index.html`` file in browser.
