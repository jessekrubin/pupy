# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(name='pupy',
      version='2.0.1a',
      description='pretty useful python',
      long_description='coming soon',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
      ],
      keywords='pretty useful python',
      # url='http://github.com/jessekrubin/pupy/',
      url='https://upload.pypi.org/legacy/',
      author='jesse r',
      author_email='jessekrubin@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'markdown',
          'tqdm>=4',
      ],
      include_package_data=True,
      zip_safe=False)


