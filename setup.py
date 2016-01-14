#!/usr/bin/env python
from distutils.core import setup


PACKAGES = ['redsys', ]

setup(
        name='redsys-256',
        description='Generates Redsys form parameters with new hmac sha256 encryption protocol.',
        long_description='This package allows to generate the appropriate parameters for new Redsys encryption protocol HMAC SHA256.',
        keywords='redsys hmac sha256 migration 256 python',
        author='Alejandro Otero Ortiz de Cosca',
        author_email='otero.alx@gmail.com',
        url='http://www.aotero.es',
        download_url="https://github.com/lexotero/python-redsys",
        version='0.1.4',
        license='MIT',
        provides=[
            'redsys'
        ],
        install_requires=[
            'pycrypto'
        ],
        packages=PACKAGES,
        scripts=[],
)
