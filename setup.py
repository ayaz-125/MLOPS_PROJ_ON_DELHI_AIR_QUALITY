import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "mlops_proj_on_delhi_air_quality"
AUTHOR_USER_NAME = "ayaz-125"
SRC_REPO = "ml_Project"
AUTHOR_EMAIL = "ayazr425@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)