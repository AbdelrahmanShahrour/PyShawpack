from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

ver = '0.7'


setup(
    name='PyShawpack',
    version= ver,
    install_requires=required,
    tests_require=['pytest'],
    author="AbdelrahmanShahrour",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AbdelrahmanShahrour/PyShawpack',
    keywords=['NLP', 'text-data', 'AI', 'DS', 'Shahrour', 'arabic-py', 'arabic-nlp'],
    description="SHAWPACK NLP processing package",
    packages=find_packages(include=['PyShawpack']),
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
 ],
)
