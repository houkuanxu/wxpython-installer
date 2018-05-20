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
    print('[INFO] ' + 'Exiting...')


def app_path():
    home = os.getenv("HOME")
    path = os.path.join(home, '.local', 'share', 'wxpython4-linux-installer')
    return path


def pip_install(arg, upgrade=False):
    if upgrade:
        cmd = [PY_EXE, '-m', 'pip', 'install', '-U', arg]
    else:
        cmd = [PY_EXE, '-m', 'pip', 'install', arg]
    print('[PIP]  ' + ' '.join(cmd))
    subprocess.call(cmd)


def pip_download(arg):
    cmd = [PY_EXE, '-m', 'pip', 'download', arg]
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

        self.run_command('flake8')


class Install(install):

    def run(self):

        if not on_linux():
            fail('Cannot install on non-linux platform')

        if is_root():
            fail('Running with root privileges. Try without sudo?')

        distro = linuxdistrocheck.find_distro()
        if not distro:
            fail('Could not find a supported Linux distribution')

        wheel = wxwheels.get_wheel(distro)
        if wheel:
            # Download the wheel in current directory ( at the moment)
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
            subprocess.call(['sudo', 'apt', 'install', '{0}'.format(req)])

        create_app_dirs()
        os.chdir(app_path())

        # Download, extract and
        pip_download('wxpython')

        # Build the wheel
        subprocess.call([PY_EXE, '-m', 'pip', 'wheel', '-v', WX_TAR, '2>&1', '| tee build.log'])
        
        # Install
        


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        return

    def finalize_options(self):
        return

    def run(self):
        self.run_command('flake8')


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
          packages=find_packages(),
          install_requires=[],
          classifiers=__classifiers__,
          test_suite='tests',
          tests_require=[],
          cmdclass=cmd_classes)


run_setup()
