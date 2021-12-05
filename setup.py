import setuptools

with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()

setuptools.setup(
    name="dico-extsource",
    version="0.0.3",
    author="eunwoo1104",
    author_email="sions04@naver.com",
    description="Enhanced Audio Source for dico.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eunwoo1104/dico-extsource",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=["av", "youtube-dl", "markdownify", "numpy"],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)