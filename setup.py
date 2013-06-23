from setuptools import setup, find_packages
import sys, os

version = 'Make python functions subscribable'

setup(name='subscribable',
      version=version,
      description="Make python functions subscribable",
      long_description="""\
Make python functions subscribable""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='subscribe',
      author='Fedor Baart',
      author_email='f.baart@gmail.com',
      url='https://github.com/SiggyF/subscribable',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      test_suite = 'nose.collector',
      setup_requires=['nose>=1.0'],
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
