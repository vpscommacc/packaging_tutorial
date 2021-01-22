import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-commercito", 
    version="0.0.1",
    author="Commer Cito",
    author_email="commercito@gmail.com",
    description="Заготовка для Python пакета",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/commercito/packaging_tutorial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Natural Language :: Russian",
        "Intended Audience :: Developers",
        "License :: Freely Distributable",
        "Topic :: Utilities",
    ],
    python_requires='>=3.8',
)
