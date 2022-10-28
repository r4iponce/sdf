SubDomain Fetcher
=================

How to use ?
------------
.. code-block:: sh

    % python3 sdf.py --help
    usage: sdf.py [-h] -d DOMAIN

    Fetch subdomain based on crt.sh

    options:
      -h, --help                    show this help message and exit
      -d DOMAIN, --domain DOMAIN    Specify domain to search

example :

``python3 sdf.py -d github.com``

`csp.py <./csp.py>`_
--------------------
Find subdomain or url with Content-Security-Policy http header

`crtsh.py <./crtsh.py>`_
------------------------
A tool for fetch subdomain based on `crt.sh <https://crt.sh>`_
