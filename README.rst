===============================
wx-phoenix-installer
===============================

**An unofficial wxPython Phoenix installer.**

----

This intended for developers who want to distribute their wxPython Phoenix package
to PyPi.


See [] for why it is difficult to distribute Linux operating systems.


 https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip/index.html
 
 
-----

What does this package do?

    Check 
    Install distribution specific dependencies via their package manager
    Search for any matching wheel available on snapshot builds
    Build wheel from source tarball then install

    
TODO:

    Support more distributions
    
.. _snapshot_build https://wxpython.org/Phoenix/snapshot-builds/linux/gtk3/ 

-----

Example setup.py

.. image:: https://github.com/swprojects/Zippy-Ip-Scanner/raw/master/resources/images/screen.png?raw=true
         :align: center

Installation
============

        pip: **pip install wxpython4-linux-installer**

.. _pypi: https://pypi.org/project/wx/#description


Support
============