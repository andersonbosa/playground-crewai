from setuptools import setup, find_packages

setup(
    name="gucli",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "shared-playground-crewai @ git+https://github.com/andersonbosa/playground-crewai.git@branch#subdirectory=projects/shared"
        "crewai",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "projeto-cli = cli.main:main",  # Substitua 'projeto-cli' pelo nome da sua CLI e 'cli.main:main' pelo caminho para a função principal da sua CLI
        ],
    },
)
