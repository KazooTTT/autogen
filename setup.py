"""
setuptools这是一个官方的python打包工具，用于打包python项目,然后发布到PyPI上
如果要用setuptools或者build来打包的话，都需要提供一个pyproject.toml文件，不要去直接修改setup.py，而是通过pyproject.toml来配置，去动态地生成它
"""

import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))
"""
__file__: 当前文件的路径
os.path.dirname(__file__): 当前文件的目录的路径（也就是不包括文件名的路径）
os.path.abspath(os.path.dirname(__file__))：当前文件的目录的绝对路径
"""

with open("README.md", "r", encoding="UTF-8") as fh:
    """
    fh是file handle的缩写，表示文件句柄
    从README.md中读取所有的内容，然后赋值给long_description
    """
    long_description = fh.read()

# Get the code version
version = {}
with open(os.path.join(here, "autogen/version.py")) as fp:
    """
    打开autogen/version.py,执行version.py,把里面的所有变量都保存在version中
    """
    exec(fp.read(), version)

# 从version.py中读取__version__的值
__version__ = version["__version__"]

# 定义需要安装的依赖
install_requires = [
    "openai>=1.3",
    "diskcache",
    "termcolor",
    "flaml",
    "python-dotenv",
    "tiktoken",
    "pydantic>=1.10,<3",  # could be both V1 and V2
    "docker",
]

setuptools.setup(
    name="pyautogen",
    version=__version__,
    author="AutoGen",
    author_email="auto-gen@outlook.com",
    description="Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microsoft/autogen",
    packages=setuptools.find_packages(include=["autogen*"], exclude=["test"]),
    install_requires=install_requires,
    extras_require={
        "test": [
            "coverage>=5.3",
            "ipykernel",
            "nbconvert",
            "nbformat",
            "pre-commit",
            "pytest-asyncio",
            "pytest>=6.1.1,<8",
        ],
        "blendsearch": ["flaml[blendsearch]"],
        "mathchat": ["sympy", "pydantic==1.10.9", "wolframalpha"],
        "retrievechat": ["chromadb", "sentence_transformers", "pypdf", "ipython"],
        "autobuild": ["chromadb", "sentence-transformers", "huggingface-hub"],
        "teachable": ["chromadb"],
        "lmm": ["replicate", "pillow"],
        "graphs": ["networkx~=3.2.1", "matplotlib~=3.8.1"],
        "websurfer": ["beautifulsoup4", "markdownify", "pdfminer.six", "pathvalidate"],
        "redis": ["redis"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8,<3.13",
)
