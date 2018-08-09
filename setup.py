#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-8-8 下午9:52
# @Author         : Tom.Lee
# @File           : setup.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from setuptools import setup, find_packages

setup(
    name='prometheus-http-client',
    version='1.0.0',
    author='liyuanjun',
    author_email='1123431949@qq.com',
    url='https://github.com/tomoncle/prometheus-http-client',
    description='Prometheus service http client, author liyuanjun',
    long_description=open("README.md").read(),
    license="MIT",
    install_requires=[
        'requests'
    ],
    packages=find_packages()
)
