"""Airport List Query setup paackage.

See:
https://github.com/MatthieuMichon/aplist
"""

from setuptools import setup

setup(
    name='sample',
    version='0.1.dev1',
    description='Airport List Query module',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
    ],
    url='https://github.com/MatthieuMichon/aplist',
    author='Matthieu Michon',
    author_email='matthieu.michon@gmail.com',
    license='GPLv3',
    packages=['aplist'],
    test_suite='tests',
    zip_safe=False
)
