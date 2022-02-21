from setuptools import setup, find, find_packages

classifiiers = [
    'Developement Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved "" MIT License',
    'Programming Language "" Python :: 3'
]

setup(
    name = 'Fatherbot Credentials',
    version= '0.0.1',
    description='Generate random credentials(names, phone numbers, etc)',
    long_description=open('READEME.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='OurFatherWhoCooksNheaven',
    author_email='fathercooks@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='',
    packages=find_packages(),
    install_requieres=['Random']
)