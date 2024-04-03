from setuptools import setup, find_packages

setup(
    name="gucli",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "shared-playground-crewai @ git+https://github.com/andersonbosa/playground-crewai.git@branch#subdirectory=projects/shared",
        "crewai",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "gu = cli.main:main",
            "guia = cli.main:main",
            "gucli = cli.main:main",
        ],
    },
)
