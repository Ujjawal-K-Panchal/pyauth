# -*- coding: utf-8 -*-
"""
Title: pyauth setup.
    
Created on Sun Nov 21 11:02:43 2021
@author: Ujjawal.K.Panchal, @Email: ujjawalpanchal32@gmail.com
Copyright (C) Ujjawal K. Panchal - All Rights Reserved.
---
"""
from setuptools import setup

desc = """
        Title: pyauth: Simple Tokenized Authentication Protocols Implementations.
	---
	Contents:	
		1.) oauth.: OpenAuthentication Protocols.
        
  @author: Ujjawal.K.Panchal, @Email: ujjawalpanchal32@gmail.com
	---
        Copyright (C) Ujjawal K. Panchal - All Rights Reserved.	
	---
    """

package_list = ['pyauth',]

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup( name = "pyauth",
       version = "1.0.0",
       description = desc,
       url = "#",
       author = "Ujjawal K. Panchal",
       author_email = "ujjawalpanchal32@gmail.com",
       license = "BSD3.",
       packages = package_list,
       install_requires=requirements,
       python_requires=">=3.8",
       zip_safe = False
      )