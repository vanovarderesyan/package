from setuptools import setup, version

with open("README.md") as fh:
    long_description = fh.read()
setup(
    name="helloworld",
    version='0.0.1',
    description="Say hello",
    py_modules=["helloworl"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'':'src'},
    classifiers=[
        'Programing Language :: Python :: 3',
        'Programing Language :: Python :: 3.6',
        'Programing Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 or later(GPLv3)',
        'Operating System :: os Intependent'
    ],
    install_requires=[
      
    ],
    extras_require = {
        "dev":[
            "pytest>=3.7"
        ]
    }
)