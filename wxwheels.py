"""
"""


import sys

PY_MAJOR = sys.version_info.major
PY_MINOR = sys.version_info.minor
PY_VER = '{0}{1}'.format(PY_MAJOR, PY_MINOR)
if PY_MAJOR == 3:
    python_dev = 'python3-dev'
elif PY_MAJOR == 2:
    python_dev = 'python-dev'

WHEEL_BASE_URL_GTK3 = 'https://wxpython.org/Phoenix/snapshot-builds/linux/gtk3/'

WHEEL_PATH = {}    
WHEEL_PATH['Ubuntu 16.04'] = WHEEL_BASE_URL_GTK3 + 'ubuntu-16.04/'
WHEEL_PATH['Ubuntu 14.04'] = WHEEL_BASE_URL_GTK3 + 'ubuntu-14.04/'
WHEEL_PATH['Fedora 24'] = WHEEL_BASE_URL_GTK3 + 'fedora-24/'
WHEEL_PATH['Debian 8'] = WHEEL_BASE_URL_GTK3 + 'debian-8/'
WHEEL_PATH['Cent OS 7'] = WHEEL_BASE_URL_GTK3 + 'centos-7/'

__wheel__ = {}
__wheel__['Ubuntu 16.04'] = {
    '36': WHEEL_PATH['Ubuntu 16.04'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp36-cp36m-linux_x86_64.whl',
    '35': WHEEL_PATH['Ubuntu 16.04'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp35-cp35m-linux_x86_64.whl',
    '27': WHEEL_PATH['Ubuntu 16.04'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp27-cp27mu-linux_x86_64.whl',
}    
    
__wheel__['Ubuntu 14.04'] = {
    '36': WHEEL_PATH['Ubuntu 14.04'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp36-cp36m-linux_x86_64.whl',
    '35': WHEEL_PATH['Ubuntu 14.04'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp35-cp35m-linux_x86_64.whl',
    '27': WHEEL_PATH['Ubuntu 14.04'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp27-cp27mu-linux_x86_64.whl',
}   

__wheel__['Fedora 24'] = {
    '35': WHEEL_PATH['Fedora 24'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp35-cp35m-linux_x86_64.whl',
    '27': WHEEL_PATH['Fedora 24'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp27-cp27mu-linux_x86_64.whl',
}

__wheel__['Debian 8'] = {
    '34': WHEEL_PATH['Debian 8'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp34-cp34m-linux_x86_64.whl',
    '27': WHEEL_PATH['Debian 8'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp27-cp27mu-linux_x86_64.whl',
}    

__wheel__['Cent OS 7'] = {
    '36': WHEEL_PATH['Cent OS 7'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp36-cp36m-linux_x86_64.whl',
    '35': WHEEL_PATH['Cent OS 7'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp35-cp35m-linux_x86_64.whl',
    '27': WHEEL_PATH['Cent OS 7'] + 'wxPython-4.0.0a3.dev3059+4a5c5d9-cp27-cp27mu-linux_x86_64.whl',
}

__wheel__['Linux Mint 18'] = __wheel__['Ubuntu 16.04']



def get_wheel(distro):
    try:
        return __wheel__[distro][PY_VER]
    except KeyError:
        return None