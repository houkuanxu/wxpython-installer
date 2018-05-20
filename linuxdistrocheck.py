import logging
import subprocess
import os.path

os_release_path = [
    '/etc/os-release',
    '/usr/lib/os-release'
]


distros = {
    "Ubuntu 16.10": {'NAME': 'Ubuntu',
                     'VERSION_ID': '16.10'},

    "Ubuntu 16.04": {'NAME': 'Ubuntu',
                     'VERSION_ID': '16.04'},

    "Linux Mint 18": {'NAME': 'Linux Mint',
                     'ID_LIKE': 'ubuntu',
                     'VERSION_CODENAME': 'sylvia'},
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
            logging.info("Checking for distribution: %s" % distro_name)
            logging.debug("Distribution validators: %s" % distro_validators)
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