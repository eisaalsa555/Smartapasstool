from setuptools import setup, find_packages

setup(
    name="smartpass",
    version="1.0.0",
    description="Smart password generator for educational & ethical hacking use",
    author="Mohd Eisa",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'smartpass = smartpass.main:run',
        ],
    },
)