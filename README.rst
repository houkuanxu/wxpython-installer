===============================
wxpython4-linux-installer
===============================

**An unofficial wxPython Phoenix installer.**

----

This intended for developers who want to distribute their wxPython Phoenix package
to PyPi.


See wx_linux_build_ for why it is difficult to distribute to Linux operating systems.


What does this package do?

    
    Search for any matching wheel available on snapshot builds. If one exists,
    download and install wheel. Ideally from snapshot_build_
    
    
    If not possible, install distribution specific dependencies via their package manager
    
    
    Download wxPython tar source and build

    Finally install.
    

Other Notes:

    Is wxpython4-linux-installer an appropriate name? Should I explicitly state
    it is unofficial?
    
    Build only runs flake8. Nothing else.
    
    Install downloads dependencies and builds wheel. But doesn't yet actually
    install the wheel.
    
    If user installs this package but then uninstalls wxPython directly.
    Other packages which rely on this package will see that this package is already
    installed therefore think wxPython is still installed. Need to handle this.
    
    Install or Build commands will fail upon running with sudo. For safety.
    
    
    Source/downloaded files are placed in './local/share/wxpython4-linux-installer' 
    
    
TODO:

    Support more distributions
    
    Include better documentation and docstrings
    
    Make sure all necessary dependencies are specified and no unnecessary dependencies
    
    Handle cleanup of installation.

    Maybe a separate git repository for unofficial wheels built by myself.
    


-----

Example setup.py


    todo: Include small setup.py recipe


Installation
============

        **pip install wxpython4-linux-installer** Not possible yet

.. _pypi: https://pypi.org/project/wx/#description

.. _wx_linux_build: https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip/index.html

.. _snapshot_build https://wxpython.org/Phoenix/snapshot-builds/linux/gtk3/ 

Support
============