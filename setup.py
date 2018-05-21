#
# wxpython4-linux-installer
#

import errno
import os
import os.path
import subprocess
import sys

from distutils.command.build import build
from setuptools import setup, find_packages, Command
from setuptools.command.install import install

import linuxdistrocheck
import wxspec
import wxwheels
from info import (__projectname__, __version__, __homepage__, __author__,
                  __classifiers__, __readme__, __history__, __description__)


PY_EXE = sys.executable
PY_MAJOR = sys.version_info.major
PY_MINOR = sys.version_info.minor
PY_VER = '{0}{1}'.format(PY_MAJOR, PY_MINOR)
WX_VER = '4.0.1'
WX_DIR = 'wxPython-{0}'.format(WX_VER)
WX_TAR = WX_DIR + '.tar.gz'


def on_linux():
    return sys.platform.startswith('linux')


def is_root():
    return os.geteuid() == 0


def fail(msg=""):
    """Output error message and exit"""
    print('[ERROR] ' + msg)
    print('[ERROR] ' + 'Exiting...')
    sys.exit(1)


def log(msg=""):
    """Output msg message"""
    print('[INFO] ' + msg)


def app_path():
    home = os.getenv("HOME")
    path = os.path.join(home, '.local', 'share', 'wxpython4-linux-installer')
    return path


def pip_check_wx_version():
    """
    Check if wxPython is already installed

    :returns: version string or None if not installed
    """
    cmd = [PY_EXE, '-m', 'pip', 'show', 'wxPython']
    print('[PIP]  ' + ' '.join(cmd))
    output = subprocess.check_output(cmd)
    if not output:
        return None
    output_str = str(output)    
    ver_start = output_str.index('Version:') + 8
    ver_end = ver_start + output_str[ver_start:].index('\\r\\n')
    version = output_str[ver_start:ver_end]
    version = version.replace(' ', '')
    return version


def pip_download(arg):
    cmd = [PY_EXE, '-m', 'pip', 'download', arg]
    print('[PIP]  ' + ' '.join(cmd))
    subprocess.call(cmd)


def pip_install(arg, upgrade=False):
    if upgrade:
        cmd = [PY_EXE, '-m', 'pip', 'install', '-U', arg]
    else:
        cmd = [PY_EXE, '-m', 'pip', 'install', arg]
    print('[PIP]  ' + ' '.join(cmd))
    subprocess.call(cmd)


def create_app_dirs():
    try:
        os.makedirs(app_path())
    except OSError as e:
        if e.errno != errno.EEXIST:
            fail('Failed to create app directories.')


class Build(build):

    def run(self):

        if not on_linux():
            fail('Cannot build on non-linux platform')

        if is_root():
            fail('Running with root privileges. Try without sudo?')

        subprocess.call(['flake8', '--append-config=.flake8.ini'])


class Install(install):

    def run(self):

        if not on_linux():
            fail('Cannot install on non-linux platform')

        if is_root():
            fail('Running with root privileges. Try without sudo?')

        distro = linuxdistrocheck.find_distro()
        if not distro:
            fail('Could not find a supported Linux distribution')

        log('Finding a wheel for your distribution.')
        wheel = wxwheels.get_wheel(distro)
        if wheel:
            # Download the wheel in current directory (at the moment)
            # create_app_dirs()
            # os.chdir(app_path())
            pip_download(wheel)
            # install here
            # Probably install directly from URL, rather than
            # download first.
            return

        log('Could not find a suitable wheel for your distribution.')
        log('Try to download source and build.')

        spec = wxspec.get_spec(distro)
        if not spec:
            fail('Could not find a specification for your distribution.')

        log('Installing build requirements...')
        for req in spec['requirements']:
            log('    - ' + req)

        # Try to install all requirements in spec. No handling of
        # any requirement which failed to be installed. In this
        # this situation, the subsequent build should probably fail.
        for req in spec['requirements']:
            cmd = ['sudo'] + spec['pkg_install'] + ['{0}'.format(req)]
            subprocess.call(cmd)

        create_app_dirs()
        os.chdir(app_path())

        # Download, extract and
        pip_download('wxpython')

        # Build the wheel
        cmd_build = [PY_EXE, '-m', 'pip', 'wheel', '-v', WX_TAR]
        subprocess.call(cmd_build)

        # Install


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        return

    def finalize_options(self):
        return

    def run(self):
        subprocess.call(['flake8', '--append-config=.flake8.ini'])


def run_setup():
    cmd_classes = {
        'build': Build,
        'install': Install,
        'test': TestCommand,
    }

    setup(name=__projectname__,
          version=__version__,
          description=__description__,
          long_description=__readme__ + '\n\n' + __history__,
          author=__author__,
          url=__homepage__,
          license='MIT',
          packages=find_packages(exclude=['tests*']),
          install_requires=[],
          classifiers=__classifiers__,
          test_suite='tests',
          tests_require=[],
          cmdclass=cmd_classes)


if __name__ == '__main__':
    run_setup()
