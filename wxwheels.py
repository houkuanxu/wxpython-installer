"""
"""

from setup import WX_VER, PY_VER

WHEEL_EXTRAS_URL = 'https://extras.wxpython.org/wxPython4/extras/linux/{0}'
WHEEL_BASE_URL_GTK3 = WHEEL_EXTRAS_URL.format('gtk3')

distro_like = {'LinuxMint 18': 'Ubuntu 16.04',
               'elementaryOS Loki': 'Ubuntu 16.04'}


def get_wheel_filename():
    """Return the standardised wheel filename"""
    if PY_VER == '27':
        f = 'wxPython-{0}-cp{1}-cp{2}mu-linux_x86_64.whl'.format(WX_VER, PY_VER, PY_VER)
    else:
        f = 'wxPython-{0}-cp{1}-cp{2}m-linux_x86_64.whl'.format(WX_VER, PY_VER, PY_VER)
    return f


def get_wheel(distro):
    """Return the full URL path to the wheel"""
    try:
        distro = distro_like[distro]
    except KeyError:
        pass
    d = distro.replace(' ', '-')
    d = d.lower()
    f = get_wheel_filename()
    url = '{0}/{1}/{2}'.format(WHEEL_BASE_URL_GTK3, d, f)
    return url
