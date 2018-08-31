# wxpython-installer


# A wxPython Phoenix installer.

[![Build Status](https://travis-ci.org/swprojects/wxpython4-linux-installer.svg?branch=master)](https://travis-ci.org/swprojects/wxpython4-linux-installer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


This is intended for developers who want to distribute their wxPython-based application to PyPi.


See [wxpython linux build](https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip/index.html) for why it is difficult to distribute to Linux operating systems.

# Latest + History

   - See HISTORY.rst for details

# What does this package do?


   - If on linux, search for any matching wheel available on builds. If one exists,
     download and install the wxpython wheel.
   - Otherwise defaults by trying to install via ```pip install wxpython```

   
# Which linux distributions/releases are supported?

    - Go to link below to see which wheels are available
      
[linux wheels](https://extras.wxpython.org/wxPython4/extras/linux/gtk3)

# Usage

If you want your pypi to install wxpython, you should add `wxpython4-linux-installer` in your setup.py requirements.

For example `install_requires=['wxpython-installer']`


# Download

If you just want to download wxpython, you can just run the command below:

    sudo pip install wxpython-installer

# Note

This currently does not seem to work without sudo. More testing required.