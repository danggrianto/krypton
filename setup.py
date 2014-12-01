from setuptools import find_packages, setup

setup(
    name='krypton',
    version='0.1.1',
    url='https://bitbucket.org/danggrianto/krypton',
    license='BSD',
    author='Daniel Anggrianto',
    author_email='danggrianto@50onred.com',
    description='Automation Framework using Selenium',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'selenium',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
