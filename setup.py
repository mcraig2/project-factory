import os
import re
from setuptools import setup

# Parse the version number
version = re.search(
    "^__version__\s*=\s*'(.*)'",
    open('factory/factory.py').read(),
    re.M).group(1)

# Use README.md as the full description
with open('README.md', 'rb') as f:
    long_descr = f.read().decode('utf-8')

# Use the requirements.txt to get the list of dependencies
with open('requirements.txt', 'rb') as f:
    installs = f.read().decode('utf-8').split()

# Make sure we include the data files needed for this project
def include_data_files(directory):
    files = os.listdir('factory/{}'.format(directory))
    return ['{}/{}'.format(directory, f) for f in files]

data_files = include_data_files('cli_maker') + \
             include_data_files('project_maker')

setup(name='factory',
      version=version,
      description='CLI tool to bootstrap CLI and projects',
      long_description=long_descr,
      url='https://github.com/mcraig2/project-factory',
      author='Mike Craig',
      author_email='mike@michaelcraig.io',
      license='MIT',
      packages=['factory'],
      package_data={'factory': data_files},
      install_requires=installs,
      entry_points = {
          'console_scripts': ['factory = factory.factory:main']
      },
      zip_safe=False)
