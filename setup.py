#!/usr/bin/env python
from distutils.core import setup


PACKAGES = ['redsys', ]

setup(
        name='redsys',
        description='Creates and encrypt the form parameter for RedSys Payment',
        author='Alejandro Otero Ortiz de Cosca',
        author_email='otero.alx@gmail.com',
        url='http://aotero.es',
        download_url="https://github.com/lexotero/python-redsys",
        version='0.0.1',
        license='MIT License',
        provides=[
            'redsys'
        ],
        install_requires=[
            'Crypto',
            'pycrypto'
        ],
        packages=PACKAGES,
        scripts=[],
)
