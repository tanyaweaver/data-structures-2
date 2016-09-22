# -*- coding: utf -8*-
from setuptools import setup

setup(
    name="binary search tree, trie",
    description="This package implements binary search tree",
    version=0.1,
    license='MIT',
    author="Crystal Lessor, Tatiana Weaver",
    author_email="email@email.com",
    py_modules=['bst', 'trie'],
    package_dir={' ': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
)
