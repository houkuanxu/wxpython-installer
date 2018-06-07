# wxpython4-linux-installer

from __future__ import absolute_import, division, print_function
import sys
from distutils.command.build import build
from setuptools import setup, find_packages, Command
from setuptools.command.install import install
from subprocess import call, check_output, CalledProcessError
from wxpython4_linux_installer.linuxdistrocheck import find_distro
from wxpython4_linux_installer.wxwheels import get_wheel
from wxpython4_linux_installer.info import (__projectname__, __version__, __homepage__, __author__,
                                            __classifiers__, __readme__, __history__, __description__,
                                            __author_email__, PY_EXE)


def on_linux():
    return sys.platform.startswith('linux')


def fail(msg=''):
    """Output error message and exit"""
    print('[ERROR] ' + msg)
    print('[ERROR] ' + 'Exiting...')
    sys.exit(1)


def log(msg=""):
    """Output msg message"""
    print('[INFO] ' + msg)


def pip_show(dep):
    """
    Check if pip dependency is installed

    :returns: version string or None if not installed
    """
    cmd = [PY_EXE, '-m', 'pip', 'show', 'wxPython']
    print('[PIP]  ' + ' '.join(cmd))
    output = None
    try:
        output = check_output(cmd)
    except CalledProcessError as e:
        print(e)

    if not output:
        return None
    output_str = str(output)
    ver_start = output_str.index('Version:') + 8
    ver_end = ver_start + output_str[ver_start:].index('\\r\\n')
    version = output_str[ver_start:ver_end]
    version = version.replace(' ', '')
    return version


def pip_install(arg, upgrade=False):
    if upgrade:
        cmd = [PY_EXE, '-m', 'pip', 'install', '-U', arg]
    else:
        cmd = [PY_EXE, '-m', 'pip', 'install', arg]
    print('[PIP]  ' + ' '.join(cmd))
    call(cmd)


def pip_uninstall(arg):
    cmd = [PY_EXE, '-m', 'pip', 'uninstall', arg]
    print('[PIP]  ' + ' '.join(cmd))
    try:
        call(cmd)
    except Exception as e:
        print(e)


class Build(build):

    def run(self):
        return


class Install(install):

    def run(self):
        if not on_linux():
            fail('Cannot install on non-linux platform')

        distro = find_distro()
        if not distro:
            fail('Could not find a supported Linux distribution')

        log('Finding a wheel for your distribution.')
        wheel = get_wheel(distro)
        if wheel:
            pip_install(wheel)
            return
            install.run(self)
            return

        fail('Could not find a suitable wheel for your distribution.')
        # install.run(self)
        return


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        return

    def finalize_options(self):
        return

    def run(self):
        call(['flake8', '--append-config=.flake8.ini'])


def run_setup():
    cmd_classes = {'build': Build,
                   'install': Install,
                   'test': TestCommand}

    setup(name=__projectname__,
          version=__version__,
          description=__description__,
          long_description=__readme__ + '\n\n' + __history__,
          author=__author__,
          author_email=__author_email__,
          url=__homepage__,
          license='MIT',
          packages=find_packages(),
          # package_data={'wxpython4-linux-installer': ['src/*.py']},
          install_requires=[],
          classifiers=__classifiers__,
          test_suite='tests',
          tests_require=[],
          cmdclass=cmd_classes)


if __name__ == '__main__':
    run_setup()
