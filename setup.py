from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rbxm-parser",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library for parsing Roblox binary model files (.rbxm and .rbxl)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/rbxm-parser",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "zstandard>=0.18.0",
    ],
    keywords="roblox rbxm rbxl parser binary model",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/rbxm-parser/issues",
        "Source": "https://github.com/yourusername/rbxm-parser",
    },
)