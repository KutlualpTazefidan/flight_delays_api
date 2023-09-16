from setuptools import setup, find_packages

setup(
    name='pipelines_for_ml',
    version='0.1',
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    install_requires=[
        # Package dependencies
        'pandas',
        'numpy',
        'scikit-learn',
        'logging',
        'geopy',
    ],
)