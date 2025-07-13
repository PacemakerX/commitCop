from setuptools import setup, find_packages

setup(
    name="ccop",
    version="0.1.0",
    description="Git commit message enforcer",
    author="Sparsh",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",
        "PyYAML>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "ccop=ccop.main:cli",
        ],
    },
)
