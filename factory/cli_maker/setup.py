import os
import re
from setuptools import setup

# Parse the version number
version = re.search(
    "^__version__\s*=\s*'(.*)'",
    open('{NAME}/{NAME}.py').read(),
    re.M).group(1)

# Use README.md as the full description
with open('README.md', 'rb') as f:
    long_descr = f.read().decode('utf-8')

# Use requirements.txt to get the list of dependencies
with open('requirements.txt', 'rb') as f:
    installs = f.read().decode('utf-8').split()

# This function allows you to include extra files
def include_data_files(directory):
    return [directory + '/' + f for f in os.listdir('{NAME}/' + directory)]
# Usage:
#   data_files = include_data_files('some_folder')
#   then in the setup function below, add "package_data={{NAME: data_files}}"

setup(name='{NAME}',
      version=version,
      description='The {NAME} command line tool',
      long_description=long_descr,
      url='https://github.com/mcraig2/{NAME}',
      author='Mike Craig',
      author_email='mike@michaelcraig.io',
      license='MIT',
      packages=['{NAME}'],
      install_requires=installs,
      entry_points = {{
          'console_scripts': ['{NAME} = {NAME}.{NAME}:main']
      }},
      zip_safe=False)
