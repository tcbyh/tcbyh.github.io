from setuptools import setup, find_packages

setup(
    name='arxiv_liter',
    version='0.0.1',
    author='tcbyh',
    author_email='545960442@qq.com',

    install_requires=[
        'fire',
        'loguru',
        'tqdm',
        'requests',
        'feedparser',
        'tabulate',
        'unidecode',
        'tenacity'
    ],

    entry_points={
      'console_scripts': [
          'arxiv_liter = arxiv_liter.main:main'
      ]
    },

    packages=find_packages(),

)