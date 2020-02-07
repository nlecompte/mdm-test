from setuptools import setup

setup(
    name='countcli',
    version='1.0.0',
    packages=['countcli'],
    entry_points={
        'console_scripts': [
            'countcli = countcli.__main__:main'
        ]
    }
)
