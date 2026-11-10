from setuptools import setup, find_packages

setup(
    name="car_rental_backend",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask>=3.0.3",
        "Flask-SQLAlchemy>=3.1.1",
        "PyMySQL>=1.1.1",
        "PyYAML>=6.0.1",
        "cryptography>=42.0.8",
    ],
)
