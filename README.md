Fwadmin
=======

Django based self-serivce firwall config tool.

The use-case is that a group of trusted users can easily configure
simple fireall rules for a set of machines. Each machine has a owner
and the rules are valid for a certain amount of time only, then they
need to be refreshed.


Dependencies:
 - python-django
 - python-netaddr

How to run the testsuite:
$ python manage.py test fwadmin

How to test interactively:
$ python manage.py runserver

go to the admin interface:
 http://localhost:8000/admin/
and create user(s) and add them to
the "Mitarb" or "G-zentrale-systeme".

Then go to:
 http://localhost:8000/fwadmin/
and create hosts/rules.