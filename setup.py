from setuptools import setup, find_packages

setup(
    name='metastable_baselines2',
    version='2.1.0.0',
    url='https://git.dominik-roth.eu/dodox/metastable-baselines2',
    author='Dominik Roth',
    author_email='mail@dominik-roth.eu',
    # description='Description of my package',
    packages=['.'],
    install_requires=['gymnasium', 'stable_baselines3==2.1.0', '-e git+ssh://git@dominik-roth.eu/dodox/PriorConditionedAnnealing.git#egg=priorConditionedAnnealing'],
)
