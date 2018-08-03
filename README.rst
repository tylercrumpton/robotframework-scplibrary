robotframework-scplibrary
=========================

|PyPI version| |PyPI license| |PyPI pyversions|


Robot Framework test library for Secure Copy (SCP)
--------------------------------------------------

This library can be used to copy files to and from a remote machine
using Secure Copy (SCP). It uses the Paramiko SSH Python library (just
like robotframework-sshlibrary) and an SCP wrapper (‘scp’ by James
Bardin).

The library does not currently support Jython or IronPython at this
time.

Installation
------------

This library may be installed via PyPI or from the source distribution.
To install using pip, run:

::

   pip install robotframework-scplibrary

To install from the source distribution, download the repo archive and
extract the source and run:

::

   python setup.py install

Example
-------

.. code::

   *** Settings ***
   Library   SCPLibrary

   *** Test Cases ***
   Grab Files From My Server
       Open Connection   192.168.1.42    username=tyler  password=teapot
       Get File          remotefile.txt  localfile.txt
       Get File          /home/tyler/    mytylerdir/     recursive=True
       Close Connection

   Put File On My Server
       Open Connection   192.168.1.42    username=tyler  password=teapot
       Put File          mytea.txt       /home/tyler/
       Close Connection

Connection
----------

Before files can be transferred, a connection to remote machine must
first be made. A connection can be made with the ``Open Connection``
keyword. Both normal username/password authentication and asymmetric
key-pair authentication may be used.

Connections should be closed using the ``Close Connection`` keyword when
they are no longer in use.

File transfer
-------------

Files and directories can be uploaded to the remote machine using the
``Put File`` or ``Put Directory`` keywords or downloaded to the local
machine using the ``Get File`` keyword.

A connection must be made using the ``Open Connection`` keyword before
file transfers may be made.

.. |PyPI version| image:: https://img.shields.io/pypi/v/robotframework-scplibrary.svg
   :target: https://pypi.org/project/robotframework-scplibrary/

.. |PyPI license| image:: https://img.shields.io/pypi/l/robotframework-scplibrary.svg
   :target: https://pypi.org/project/robotframework-scplibrary/

.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/robotframework-scplibrary.svg
   :target: https://pypi.org/project/robotframework-scplibrary/

