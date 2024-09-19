from setuptools import setup

setup(
    name = 'EXCELntDonut',
    python_requires='>3.5.2',
    version = '1.0',
    author = 'Joseph Leon (FortyNorthSecurity.com)',
    author_email = 'jleon@fortynorthsecurity.com',
    packages = ['EXCELntDonut'],
    install_requires = [
        'donut-shellcode @ https://github.com/jsf9k/donut/tarball/bugfix/python-extension-fails-to-build',
        'pandas'
      ],
    entry_points = {
        'console_scripts': [
            'EXCELntDonut = EXCELntDonut.drive:main'
        ]
    })
