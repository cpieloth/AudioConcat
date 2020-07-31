#!/usr/bin/env python3

"""
A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

import setup_commands

__author__ = 'Christof Pieloth'

# runtime dependencies
install_requires = [
    'tinytag==1.4.*'
]

setup(
    cmdclass=dict(setup_commands.custom_commands),

    name=setup_commands.project_name,

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=setup_commands.version,

    description='Concat audio files to a single file.',

    url='https://github.com/cpieloth',

    author='Christof Pieloth',

    # Choose a license: https://choosealicense.com
    license='MIT License',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],

    packages=find_packages(exclude=['build*', 'docs*', 'tests*', 'tools*', 'venv*']),

    install_requires=install_requires,

    test_suite='tests',

    include_package_data=True,

    entry_points={
        'console_scripts': [
            '{} = {}.__main__::main'.format(setup_commands.api_name, setup_commands.api_name)
        ],
    },
)
