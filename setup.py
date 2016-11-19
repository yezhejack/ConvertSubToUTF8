from setuptools import setup, find_packages
setup(
    name = "ConvertSubToUTF8",
    version = "0.0.1",
    packages = find_packages(),
    scripts=['ConvertSubToUTF8.py'],
    install_requires=['chardet>0'],
    author='Zhe Ye',
    author_email='yezhejack@gmail.com',
    description='This is a useful tool for convert sub file code format',
    keywords='convert sub subtitles files utf8',
    url='http://yezhejack.github.io/2016/10/11/ConvertToUTF8/',
    license='PSF',
)
