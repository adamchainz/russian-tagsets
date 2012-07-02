#! /usr/bin/env python
from distutils.core import setup

__version__ = '0.1'

setup(
    name="russian-tagsets",
    version=__version__,
    description="Russian tagset converters library",
    long_description = open('README.rst').read(),
    license = 'MIT license',
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    url = 'https://bitbucket.org/kmike/russian-tagsets/',
    test_requires = ['pytest'],

    packages = ['russian_tagsets', 'russian_tagsets.positional'],

    classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: Russian',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Text Processing :: Linguistic',
    ],

)




