########################
Quickstart
########################

========================
**Installation**
========================

*  Requires Python ``>=3.7``
*  ``pip install firebolt-sdk`` 

==========================
**Connection parameters**
==========================

These parameters are used to connect to a Firebolt database:

* **engine_url** - url for a Firebolt engine to make requests to. This can be retrieved from our web interface, or from the `engine <https://github.com/firebolt-db/firebolt-sdk/tree/main/src/firebolt/model/engine.py>`_ attribute endpoint
* **database** - the name of the database to receive queries
* **username** - Firebolt account username
* **password** - Firebolt account password
* **api_endpoint** - (*optional*) api hostname for logging in. Defaults to ``api.app.firebolt.io``.

==========================
**Examples** 
==========================

See `PEP-249 <https://www.python.org/dev/peps/pep-0249>`_ for the DB API reference and specifications. 

An example `jupyter notebook <https://github.com/firebolt-db/firebolt-sdk/tree/main/examples/dbapi.ipynb>`_ is included to illustrate the use of the Firebolt API.


==========================
**Optional features** 
==========================

By default, the firebolt-python-sdk uses ``datetime`` module to parse date and datetime values, which might be slow for a large amount of operations. In order to speed up datetime operations, it's possible to use `ciso8601 <https://pypi.org/project/ciso8601/>`_ package. 

To install firebolt--python-sdk with ``ciso8601`` support, run ``pip install firebolt-sdk[ciso8601]``