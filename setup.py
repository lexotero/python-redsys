#!/usr/bin/env python
from distutils.core import setup


PACKAGES = ['redsys', ]

setup(
        name='redsys-256',
        description='This package can generate the necessary fields to the Redsys payment form.',
        keywords='redsys hmac sha256',
        author='Alejandro Otero Ortiz de Cosca',
        author_email='otero.alx@gmail.com',
        url='http://www.aotero.es',
        download_url="https://github.com/lexotero/python-redsys",
        version='0.1.0',
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
