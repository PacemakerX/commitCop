from setuptools import setup, find_packages

setup(
    name="ccop",
    version="0.1.0",
    description="Commit message enforcer for Git",
    author="Sparsh",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click",
        # Add any other dependencies you use
    ],
    entry_points={
        "console_scripts": [
            "ccop=ccop.main:cli",  # maps `ccop` command to your CLI entry point
        ]
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
