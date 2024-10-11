from setuptools import setup

setup(
    name='ktemplates',
    version='0.1',
    py_modules=['ktemplates'],
    install_requires=[
        'PyYAML',
    ],
    extras_require={
        'dev': [
            'pytest',
        ]
    },
    entry_points={
        'console_scripts': [
            'ktemplates=ktemplates:main',
        ],
    }
)