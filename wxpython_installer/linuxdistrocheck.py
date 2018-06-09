from __future__ import absolute_import, division, print_function
import logging

os_release_path = ['/etc/os-release',
                   '/usr/lib/os-release']


distros = {

    'Ubuntu 18.10': {'NAME': 'Ubuntu',
                     'VERSION_ID': '18.10'},

    'Ubuntu 18.04': {'NAME': 'Ubuntu',
                     'VERSION_ID': '18.04'},

    'Ubuntu 16.10': {'NAME': 'Ubuntu',
                     'VERSION_ID': '16.10'},

    'Ubuntu 16.04': {'NAME': 'Ubuntu',
                     'VERSION_ID': '16.04'},

    'Ubuntu 14.10': {'NAME': 'Ubuntu',
                     'VERSION_ID': '14.10'},

    'Ubuntu 14.04': {'NAME': 'Ubuntu',
                     'VERSION_ID': '14.04'},

    'Debian 9': {'NAME': 'Debian GNU/Linux',
                 'VERSION_ID': '9',
                 'ID': 'debian'},

    'Debian 8': {'NAME': 'Debian GNU/Linux',
                 'VERSION_ID': '8',
                 'ID': 'debian'},

    'Fedora 28': {'NAME': 'Fedora',
                  'ID': 'fedora',
                  'VERSION_ID': '28'},

    'Fedora 27': {'NAME': 'Fedora',
                  'ID': 'fedora',
                  'VERSION_ID': '27'},

    'Fedora 26': {'NAME': 'Fedora',
                  'ID': 'fedora',
                  'VERSION_ID': '26'},

    'Fedora 24': {'NAME': 'Fedora',
                  'ID': 'fedora',
                  'VERSION_ID': '24'},

    'Fedora 23': {'NAME': 'Fedora',
                  'ID': 'fedora',
                  'VERSION_ID': '23'},

    'CentOS 7': {'NAME': 'CentOS Linux',
                 'VERSION_ID': '7'},

    'LinuxMint 18': {'NAME': 'Linux Mint',
                     'ID_LIKE': 'ubuntu',
                     'VERSION_CODENAME': 'sylvia'},

    'elementaryOS Loki': {'NAME': 'elementary OS',
                          'VERSION_CODENAME': 'loki',
                          'ID_LIKE': 'ubuntu'},

    'Solus': {'NAME': 'Solus',
              'ID': 'solus'},
}


def get_os_release_results():
    """Parse os-release file and yield results dict"""
    for file in os_release_path:
        print('Checking for distributions from %s' % file)
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError as e:
            print(e)

        result = {}
        for line in lines:
            k, v = line.split('=')
            v = v.replace('\n', '')
            v = v.replace('"', '')
            result[k] = v
        yield result


def find_distro():

    for result in get_os_release_results():
        logging.debug(result)
        for distro_name, distro_validators in distros.items():
            match = None
            for validator, value in distro_validators.items():
                logging.debug('Check: "{0}" key in file'.format(validator))
                if validator not in result:
                    match = None
                    logging.debug('Not Found: "{0}" key in file'.format(validator))
                    break
                logging.debug('Found: "{0}" key in file'.format(validator))
                logging.debug('Check Match: "{0}" == "{1}"'.format(value, result[validator]))
                if result[validator] != value:
                    match = None
                    logging.debug('No Match: "{0}" == "{1}"'.format(value, result[validator]))
                    break

                match = distro_name

            if match:
                match = distro_name
                print('Found distribution:', match)
                return match

    print('No distribution found. All checks finished.')
    return None


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    d = find_distro()
    print(d)
