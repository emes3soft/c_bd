from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
# with open(this_directory + "\Readme.md", "r") as f:
#     long_description = f.read()

setup(
    name="c_bd",
    version = "2.0",
    description="Integração entre bases de dados, python, flask, html com a Bootstrap e DataTables",
    package_dir={"":"c_bd2"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/emes3soft/c_bd",
    download_url = "https://github.com/emes3soft/c_bd/blob/main/dist/c_bd-2.0.zip",
    author= "Emes3Soft",
    author_email= "emes3soft@gmail.com",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPLv3)",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords="database basedados tabela table c_bd",
    install_requires = [
        "bcrypt",
        "Flask",
        "mysql-connector-python",
        "Flask-Session",
        "numpy",
        "pycryptodome",
        "passlib",
        "DateTime",
        "argon2-cffi-bindings",
        "multipledispatch"
    ],
    extras_require = {
        "dev" : [
            "pytest",
            "twine"
        ]
    },
    python_requires = ">=3.10",
    package_data={'': ['*.zip']},
    include_package_data=True,
)