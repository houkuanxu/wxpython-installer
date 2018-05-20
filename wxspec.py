"""
Requirements alphabetical order (A-Z)

https://wxpython.org/Phoenix/snapshot-builds/linux/gtk3/ubuntu-16.04/
"""


import sys

PY_MAJOR = sys.version_info.major
PY_MINOR = sys.version_info.minor
PY_VER = '{0}{1}'.format(PY_MAJOR, PY_MINOR)
if PY_MAJOR == 3:
    python_dev = 'python3-dev'
elif PY_MAJOR == 2:
    python_dev = 'python-dev'


__spec__ = {}
__spec__['Ubuntu 16.04'] = {
    'requirements': [
                     python_dev,
                     'libgtk-3.0'
                     'libgtk-3-dev'
                     'freeglut3'
                     'freeglut3-dev'
                     'libtiff5'
                     'libtiff5-dev'
                     'libnotify4'
                     'libnotify-dev'
                     'libsdl1.2debian'
                     'libsdl1.2-dev'
                     'libsm6'
                     'libsm-dev'
                     'libgstreamer-plugins-base1.0-0'
                     'libgstreamer-plugins-base1.0-dev'
                     'libpng12-0'
                     'libpng12-dev'
                     'libjpeg-dev'
                     'libwebkitgtk-3.0-0'
                     'libwebkitgtk-3.0-dev'
                     ], 
    'pkg_install': 'apt install'
}


def get_spec(distro):
    try:
        return __spec__[distro]
    except KeyError:
        return None