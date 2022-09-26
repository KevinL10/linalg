import setuptools

setuptools.setup(
    name="linalg",
    version="0.0.1",
    author="KevinL10",
    author_email="kevinsliu0@gmail.com",
    description="A pure python linear algebra library",
    url="https://github.com/KevinL10/linalg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
