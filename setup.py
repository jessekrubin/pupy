# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='pupy',
      version='1.3.0',
      description='pretty useful python',
      long_description='coming soon',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          ],
      keywords='pretty useful python',
      repository='https://github.com/jessekrubin/pupy',
      url='https://upload.pypi.org/legacy/',
      author='jessekrubin',
      author_email='jessekrubin@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'tqdm>=4', 'pytest'
          ],
      include_package_data=True,
      zip_safe=False)
