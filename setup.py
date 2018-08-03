from os import path
from io import open
from setuptools import setup


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

config = {
    'description': 'Robot Framework test library for transferring files via Secure Copy (SCP)',
    'author': 'Tyler Crumpton',
    'url': 'https://www.tylercrumpton.com',
    'download_url': 'https://github.com/tylercrumpton/robotframework-scplibrary',
    'author_email': 'tyler.crumpton@gmail.com',
    'vcversioner': {'version_module_paths': ['SCPLibrary/_version.py']},
    'install_requires': ['scp', 'paramiko', 'six'],
    'packages': ['SCPLibrary'],
    'scripts': [],
    'name': 'robotframework-scplibrary',
    'license': 'GPLv3',
    'long_description': LONG_DESCRIPTION,
    'project_urls': {
        'Bug Reports': 'https://github.com/tylercrumpton/robotframework-scplibrary/issues',
        'Source': 'https://github.com/tylercrumpton/robotframework-scplibrary',
    },

}

setup(**config)
