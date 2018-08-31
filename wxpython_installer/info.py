from __future__ import absolute_import, division, print_function
import sys
from os import path

__projectname__ = 'wxpython-installer'
__version__ = '0.1.0'
__homepage__ = 'https://github.com/swprojects/wxpython-installer'
__author__ = 'Simon Wu'
__author_email__ = 'swprojects@runbox.com'
__description__ = 'A wxPython installer for Linux distribution'

__classifiers__ = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

try:
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
        __readme__ = readme_file.read()
except Exception:
    __readme__ = ''

try:
    with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
        __history__ = history_file.read().replace('.. :changelog:', '')
except Exception:
    __history__ = ''


PY_EXE = sys.executable
PY_MAJOR = sys.version_info.major
PY_MINOR = sys.version_info.minor
PY_VER = '{0}{1}'.format(PY_MAJOR, PY_MINOR)
WX_VER = '4.0.3'
WX_DIR = 'wxPython-{0}'.format(WX_VER)
WX_TAR = WX_DIR + '.tar.gz'
