#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Sahil Sawant",
    author_email='smsawant17@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This is the MLOPs ISA performed by H.Fayaz ans Sahil Sawant.",
    entry_points={
        'console_scripts': [
            'mlops_isa_2307_2309=mlops_isa_2307_2309.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mlops_isa_2307_2309',
    name='mlops_isa_2307_2309',
    packages=find_packages(include=['mlops_isa_2307_2309', 'mlops_isa_2307_2309.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Sahildj17/mlops_isa_2307_2309',
    version='0.0.1',
    zip_safe=False,
)
