import setuptools
# readme.md = github readme.md, 這裡可接受markdown寫法
# 如果沒有的話，需要自己打出介紹此專案的檔案，再讓程式知道
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CIoT_Course", # 
    version="0.0.1",
    author="Felix Weiss",
    author_email="felixweiss1999@gmail.com",
    description="Provides API for simulated stock trading platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/felixweiss1999/CIoT_Course",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)