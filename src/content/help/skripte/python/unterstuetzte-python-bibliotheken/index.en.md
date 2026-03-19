---
title: 'Supported Python libraries'
date: 2023-05-12
lastmod: '2024-10-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/help/supported-python-libraries'
aliases:
    - '/help/unterstuetzte-python-bibliotheken'
seo:
    title: 'Supported Python libraries in SeaTable – full overview'
    description: 'Find out which Python modules and packages are available in SeaTable Cloud, Enterprise, and Server – and how to use custom libraries.'
---

The Python environment of SeaTable 6.1 (Marc 2026) uses Python 3.12 and imports the [Python Standard Library](https://docs.python.org/3.12/library/index.html). The Standard Library contains frequently used modules such as os, sys, datetime, math and random. You can use these directly in your Python scripts by importing them into your script.

## SeaTable Cloud

In addition to the modules of the standard library, the Python environment of SeaTable Cloud also includes some popular Python packages. A list of the available Python packages can be found in the [SeaTable Developer Manual](https://developer.seatable.com/scripts/python/common_questions/#list-of-libraries-supported-in-the-cloud-environment).

Other Python packages cannot be imported.

## SeaTable Server

If you run your own SeaTable server, you can add additional Python packages to the Python environment. In the [SeaTable Admin Manual](https://admin.seatable.com/installation/advanced/python-pipeline-custom-python-runner/) you will find instructions on how to build your custom Python runner.
