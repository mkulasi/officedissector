#!/usr/bin/env python

from distutils.core import setup

setup(
    author='Grier Forensics',
    author_email='jdgrier@grierforensics.com',
    description="""OfficeDissector is a parser library for static security analysis of OOXML documents.""",
    name='officedissector',
    packages=['officedissector'],
    install_requires=['lxml'])
