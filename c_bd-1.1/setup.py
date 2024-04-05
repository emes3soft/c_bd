from setuptools import find_packages, setup

with open("Readme.md", "r") as f:
    long_description = f.read()

setup(
    name="c_bd",
    version = "1.1",
    description="Integração entre bases de dados, python, flask, html com a Bootstrap e DataTables",
    package_dir={"":"c_bd"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/emes3soft/c_bd/c_bd-1.1",
    author= "Emes3Soft",
    author_email= "emes3soft@emes3soft.com",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPLv3)",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords="database basedados tabela table c_bd",
    install_requires = [
        "bcrypt >= 2.1.2",
        "Flask >= 3.0.2",
        "mysql-connector-python >= 8.3",
        "Flask-Session >= 0.6.0",
        "numpy >= 1.26.4"
    ],
    extras_require = {
        "dev" : [
            "pytest>=7.0",
            "twine>=4.0.2"
        ]
    },
    python_requires = ">=3.12",
    # entry_points = {
    #     "console_scripts": [
    #         "c_bd = c:_bd"
    #     ]
    # },
    package_data={'': ['*.zip']},
    # packages=find_packages(exclude=("tests",), include="*.zip"),
    # packages=find_packages(include=("c_bd/*.zip",)),
    include_package_data=True,
)
