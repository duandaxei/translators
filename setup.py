# coding=utf-8
# author=UlionTse

from setuptools import setup,find_packages


PACKAGE = "translators"
NAME = "translators"
DESCRIPTION = "Translators is a library which aims to bring free, multiple, enjoyable translation to individuals " \
              "and students in Python."
AUTHOR = "UlionTse"
AUTHOR_EMAIL = "shinalone@outlook.com"
URL = "https://github.com/uliontse/translators"
VERSION = __import__(PACKAGE).__version__

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        # "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=['translate', 'translator', 'fanyi', 'translate_html', 'Google', 'Yandex', 'Bing',
              'Baidu', 'Alibaba', 'Tencent', 'Youdao', 'Sogou', 'Iciba', 'Iflytek', 'Deepl', 'Caiyun', 'Argos'],
    install_requires=[
        'requests>=2.26.0',
        'PyExecJS>=1.5.1',
        'lxml>=4.5.0',
        'loguru>=0.4.1',
        'pathos>=0.2.7',
    ],
    zip_safe=False,
)
