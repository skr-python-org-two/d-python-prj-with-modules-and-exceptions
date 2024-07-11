import os
import pathlib
#import subprocess
#import sys
import setuptools


#def install(package):
#    subprocess.check_call([sys.excutable,"-m","pip","install",package])

# GH_TOKEN = os.getenv("GH_TOKEN")
# if GH_TOKEN is None:
#     required = 'python-dotenv==1.0.0'
#     install(required)
#     from dotenv import load_dotenv
#
#     load_dotenv()
#     GH_TOKEN = os.getenv("GH_USERNAME")+ ":" +os.getenv("GH_TOKEN")
#     print(f"##### GH_TOKEN is :::: {GH_TOKEN}")


GH_USERNAME = os.getenv("GH_USERNAME")
GH_TOKEN = os.getenv("GH_TOKEN")


PACKAGE_REQUIREMENTS = [
    "PyYAML==6.0",
    "pysftp==0.2.9",
    "boto3==1.34.51",
    "wheel",
    # success #
    f"python-generic-functon-library @ git+https://{GH_USERNAME}:{GH_TOKEN}@github.com/skr-python-org-two/python-generic-functon-library.git@v1.0.5",
    # success #f"python-generic-functon-library @ git+https://{GH_USERNAME}:{GH_TOKEN}@github.com/skr-python-org-two/python-generic-functon-library.git@v1.0.5#egg=my-python-lib"
    # Failed # f"python-custom-library @ git+https://{GH_USERNAME}:{GH_TOKEN}@github.com/skr-python-org-two/python-generic-functon-library.git@v1.0.5"
    f"python-generic-functon-library-two-custom-code @ git+https://{GH_USERNAME}:{GH_TOKEN}@github.com/skr-python-org-two/python-generic-functon-library-two.git@v1.0.0",
]

DEV_REQUIREMENTS = [
    "pytest == 7.1.3",
    "pandas == 1.5.0",
    "pytest-cov == 3.0.0",
    "python-dotenv == 1.0.0"
]


current_dir = pathlib.Path(__file__).parent.resolve()
#long_description = (current_dir / 'README.md').read_txt(encoding="utf-8")
long_description = "test project "
#os.environ["PROJ_BASE_DIR"] = str(current_dir)
#print(f"current_dir value is :::: {current_dir}")
#b=25
#sprint(f"value of b is :::: {b}")




setuptools.setup(
    name="d-python-prj-with-modules-and-exceptions",
    version="1.0.0",
    author="ABC Team",
    author_email = "sekher.talupula@gmail.com,sekhar.jagadeesh9@gmail.com",
    description = "contains code for exception handling and module ",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(exclude=["test_*","**/test/*"]),
    python_requires = ">=3.9",
    setup_requires = ["setuptools" , "wheel"],
    install_requires = PACKAGE_REQUIREMENTS,
    extras_require = { "dev" : DEV_REQUIREMENTS },
    classifiers= [
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_data = {
        'me.personal': ['*.csv' , '*.json']
    }
)