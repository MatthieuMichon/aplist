#########################
Airport List Query Module
#########################

Provides a query API against a list of worldwide airports.


************
Installation
************

This module being registered in PyPI, it can be installed using PIP::

	pip install aplist

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
