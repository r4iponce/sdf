SubDomain Fetcher
=================

How to use ?
------------
.. code-block:: sh
    % python3 sdf.py --help
    usage: sdf.py [-h] [-q] -d DOMAIN

    Fetch subdomain based on crt.sh

    options:
      -h, --help                    show this help message and exit
      -q, --quiet                   Only display domain
      -d DOMAIN, --domain DOMAIN    Specify domain to search

.. note:: example :

.. code-block::sh
    python3 sdf.py github.com


csp.py
------
Find subdomain or url with Content-Security-Policy http header

crtsh.py
--------
A tool for fetch subdomain based on `crt.sh <https://crt.sh>`_
