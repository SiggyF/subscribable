import sys
import os

from setuptools import (
    setup,
    find_packages
)

version = 'Make python functions subscribable'

setup(name='subscribable',
      version=version,
      description="Make python functions subscribable",
      long_description="""\
      Decorate python functions to make them subscribable using similar syntax
      to c# delegates.
      """,
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries'
      ],
      keywords='subscribe',
      author='Fedor Baart',
      author_email='f.baart@gmail.com',
      url='https://github.com/SiggyF/subscribable',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      setup_requires=['nose>=1.0'],
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
