from setuptools import setup, find_packages

setup(
    name='metastable_baselines2',
    version='2.3.0.1',
    url='https://git.dominik-roth.eu/dodox/metastable-baselines2',
    author='Dominik Roth',
    author_email='mail@dominik-roth.eu',
    packages=find_packages(),
    install_requires=[
        'gymnasium',
        'stable_baselines3>=2.1.0,<=2.3.0',
    ],
    extras_require={
        'pca': [
            'priorConditionedAnnealing @ git+ssh://git@dominik-roth.eu/dodox/PriorConditionedAnnealing.git#egg=priorConditionedAnnealing'
        ],
    },
)

