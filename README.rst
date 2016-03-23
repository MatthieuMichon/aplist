#########################
Airport List Query Module
#########################

Provides a query API against a list of worldwide airports.


************
Installation
************

This module being registered in PyPI, it can be installed using PIP::

	pip install aplist

You may want to avoid bloating your system Python with packages using ``virtualenv`` which works in way like a ``chroot`` but limited to PIP packages::

	virtualenv .
        source bin/activate
	(do your things...)
	deactivate

*****
Usage
*****

Importing the module
====================

Import this module the usual way::

	import aplist

API
===


::

	apl_inst = AirportList()

::

	query(query_dict}


``query_dict`` is a *dict* type with one or more of the three actions as keys:

* ``search``: dictionnary of fields and values
* ``sort``: dictionnary of a single field and a direction
* ``paginate``: dictionnary of paginate options and their values

Search Action
-------------

A *search action* is defined as a dictionnary of field and value pairs. Airports with their fields matching this dictionnary are selected, the remaining items are discarded.

Example::

	{'country': 'Russia', 'tzoffset': 6}

Sort Action
-----------

A *sort action* is a dictionnary holding a single field / direction pair. Pair must be either ``asc`` for sorting in ascending order the given field, and ``des`` for the opposite.

Example::

	{'city': 'des'}


Paginate Action
---------------

A *paginate action* consists in splitting a list of selected airports in pages. Two parameters are supporter:
* ``offset`` indicating the index where the selection starts
* ``limite`` indicating the maximum number of airports in the selection

Example::

	{'offset': 80, `limit`: 20}


Field List
----------

========= ========================
Field     Description
========= ========================
uid       Unique identifier
name      Airport name
city      Closest major city
country   Airport country
iata      3-letter IATA code
icao      4-letter ICAO code
latitude  Latitude
longitude longitude
altitude  Airfield elevation
tzoffset  Timezone offset
dst       One if DST is observed
tzname    Timezone name
========= ========================
