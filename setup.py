from setuptools import setup, find_packages

cmdclass = {}
try:
    from babel.messages import frontend as babel
    cmdclass.update({
        'compile_catalog': babel.compile_catalog,
        'extract_messages': babel.extract_messages,
        'init_catalog': babel.init_catalog,
        'update_catalog': babel.update_catalog,
    })
except ImportError as e:
    pass

try:
    from sphinx.setup_command import BuildDoc
    cmdclass['build_sphinx'] = BuildDoc
except ImportError as e:
    pass

name = 'ltldoorstep'
version = '0.1'
release = '0.1.1'
setup(
    name='ltldoorstep',
    version=release,
    description='Doorstep: Project Lintol validation engine',
    url='https://github.com/lintol/doorstep',
    author='Project Lintol team (on behalf of)',
    author_email='help@lintol.io',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='validation lintol data',
    setup_requires=['pytest-runner'],
    extras_require={
        'babel-commands': ['Babel'],
        'sphinx-commands': ['sphinx']
    },
    install_requires=[
        'Click',
        'janus',
        'colorama',
        'dask',
        'distributed',
        'tabulate',
        'Flask',
        'flask_restful',
        'unicodeblock',
        'goodtables',
        'pypachy',
        'pandas',
        'boto3',
        'autobahn',
        'ckanapi'
    ],
    include_package_data=True,
    tests_require=[
        'pytest',
        'pytest-asyncio',
        'mock'
    ],
    entry_points='''
        [console_scripts]
        ltldoorstep=ltldoorstep.scripts.ltldoorstep:cli
        ltlwampclient=ltldoorstep.scripts.ltlwampclient:cli
    ''',
    cmdclass=cmdclass,
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', release)
        }
    }
)
