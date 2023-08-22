from setuptools import setup, find_packages, find_namespace_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
#long_description = (here / 'README.MD').read_text(encoding='utf-8')

setup(
    name='function',
    version='0.0.1',
    package_dir={'': 'src'},
    packages=find_packages('src')
    #packages=find_namespace_packages(where='python', include='*.py'),
    #python_requires='>=3.8, <4',
    #install_requires=['boto3', 'botocore', 'pyyaml'],
    #extras_require={
    #    'dev': ['pre-commit', 'black', 'pylint'],
    #    'test': ['pytest', 'pytest-mock', 'coverage'],
    #},
    #entry_points={
    #    'console_scripts': [
    #        'environment-manager=environment_manager.environment_controller:main',
    #    ],
    #}
)
