from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'riftwrapper',
  packages = find_packages(),
  version = 'v1.2',
  license='gpl-3.0',
  description = 'Python Riot API wrapper',
  author = 'verd1c',
  author_email = 'kwstasfortmanik@gmail.com',
  url = 'https://github.com/verd1c/Rift-Wrapper',
  download_url = 'https://github.com/verd1c/Rift-Wrapper/archive/v1.1.tar.gz',
  keywords = ['RiotAPI', 'Riot API wrapper', 'Python API'],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)