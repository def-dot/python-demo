from setuptools import setup, find_packages

setup(
    name="python-demo",
    version="v1.0.0",
    packages=find_packages(include=["suanfa", "suanfa.*"]),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib"
    ],
    # entry_points={
    #     "console_scripts": [
    #         "demo-main = python-demo:main",
    #     ]
    # },
    extras_require={
        "dev": ["xlrd", "yarl"],
        "test": ["pytest"]
    },
    author="sjj",
    author_email="sjj@test.com",
    description="python build program",
    url="http://www.example.com",
    license="BSD"
)
