from setuptools import setup

VERSION= '0.0.1'

setup(
    name='reurl',
    version = VERSION,
    packages = ['packaging-test-repo'],
    url='https://github.com/shang-vikas/packaging-test-repo',
    download_url=f'https://github.com/shang-vikas/packaging-test-repo/tarball/{VERSION}',
    license='MIT',
    author = 'Vikas Sangwan',
    author_email = '16vikas96@gmail.com',
    description='Just a test repo package. In the future, i will put something useful over here',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['pandas>=0.23.0','numpy>=1.0.13','requests>=2.20'],
    entry_points= {'console_scripts':
        ['reurl=download:main'],
        },
    classifiers=[
                'Development Status :: 4 - Beta',
                'License :: OSI Approved :: MIT License',
                'Topic :: Office/Business :: Financial',
                'Topic :: Scientific/Engineering :: Mathematics',
                'Topic :: Software Development :: Libraries :: Python Modules',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: Implementation :: CPython'
        
        ]
    )
