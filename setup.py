from setuptools import setup, find_packages

setup(
    name='migrato',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'migrato = migrato:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='API Endpoint Migrator Tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/syedm1/migrato',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
