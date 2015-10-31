#!/usr/bin/env python

from setuptools import setup

from versioneer import get_cmdclass, get_version


setup(
    name='test',
    packages=['test'],
    cmdclass=get_cmdclass(),
    version=get_version(),
    zip_safe=False,
)
