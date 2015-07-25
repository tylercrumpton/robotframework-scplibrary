from setuptools import setup

config = {
    'description': 'Robot Framework test library for transferring files via Secure Copy (SCP)',
    'author': 'Tyler Crumpton',
    'url': 'http://www.tylercrumpton.com',
    'download_url': 'https://github.com/tylercrumpton/robotframework-scplibrary',
    'author_email': 'tyler.crumpton@gmail.com',
    'vcversioner': {'version_module_paths': ['SCP/_version.py']},
    'install_requires': ['scp'],
    'packages': ['SCP'],
    'scripts': [],
    'name': 'robotframework-scp'
}

setup(**config)