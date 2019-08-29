# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Setup for pip package."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import find_packages
from setuptools import setup
from setuptools.dist import Distribution

__version__ = '0.0.1dev'
REQUIRED_PACKAGES = [
    'tensorflow >= 1.12.0',
]

project_name = 'tf-quant-finance'
description = 'High performance Tensorflow library for quantitative finance.'


class BinaryDistribution(Distribution):
  """This class is needed in order to create OS specific wheels."""

  def has_ext_modules(self):
    return True


setup(
    name=project_name,
    version=__version__,
    description=description,
    author='Google Inc.',
    author_email='tf-quant-finance@google.com',
    # Contained modules and scripts.
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    # Add in any packaged data.
    include_package_data=True,
    zip_safe=False,
    distclass=BinaryDistribution,
    # PyPI package information.
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
    ],
    license='Apache 2.0',
    keywords='tensorflow quantitative finance hpc gpu option pricing',
    package_data={
        'tf_quant_finance': [
            'third_party/sobol_data/new-joe-kuo.6.21201',
            'third_party/sobol_data/LICENSE'
        ]
    },
)