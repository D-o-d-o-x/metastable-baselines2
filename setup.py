from setuptools import setup, find_packages

setup(
    name='metastable_baselines2',
    version='2.1.0.0',
    # url='https://github.com/mypackage.git',
    # author='Author Name',
    # author_email='author@gmail.com',
    # description='Description of my package',
    packages=['.'],
    install_requires=['gymnasium', 'stable_baselines3==2.1.0'],
)
