import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-vpscommacc",
    version="1.0.1",
    author="VPS commacc",
    author_email="vps.commacc@yandex.ru",
    description="Заготовка для Python пакета",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vpscommacc/packaging_tutorial",
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
