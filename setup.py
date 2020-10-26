from setuptools import setup, find_packages

setup(
    name="linepipe",
    use_version_scm=True,
    packages=find_packages(),
    setup_requires=[
        "setuptools_scm",
    ],
    entry_points={
        "console_scripts": [
            "linepipe = linepipe.cli.main:main"
        ],
    },
)
