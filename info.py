from os import path

__projectname__ = 'wxpython4-linux-installer'
__version__ = '0.0.1'
__homepage__ = 'https://github.com/swprojects/wxpython4-linux-installer'
__author__= 'Simon Wu'
__description__= 'An unofficial wxPython4 (Phoenix) installer for Linux distribution'

__classifiers__ = [
    'Development  Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    # 'Programming Language :: Python :: 3.3',
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