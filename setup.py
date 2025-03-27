from setuptools import setup, find_packages

setup(
    name='test2',
    version='1.1',
    packages=find_packages(),
    package_data={'': ['py.typed']},
    author='TennisProjekt',
    description='Tennis Database',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TennisProjekt/test2',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=['sqlalchemy', 'pandas', 'psycopg2']
)