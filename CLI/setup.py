
from setuptools import setup, find_packages
from ourtube.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='ourtube',
    version=VERSION,
    description='A communist YouTube downloader',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='PoLocHiK',
    author_email='john.doe@example.com',
    url='https://github.com/ShadowOfPripyat/OurTube',
    license='GNU General Public License v3.0',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'ourtube': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        ourtube = ourtube.main:main
    """,
)
