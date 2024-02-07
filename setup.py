# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tomlkit']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tomlkit',
    'version': '0.12.3',
    'description': 'Style preserving TOML library',
    'author': 'Sébastien Eustace',
    'author_email': 'sebastien@eustace.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sdispater/tomlkit',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
