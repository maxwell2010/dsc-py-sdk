
---

## 🐍 `setup.py`

```python
from setuptools import setup, find_packages

setup(
    name='dsc_py_sdk',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests>=2.31',
        'eth-account>=0.5.7',
        'eth-keys>=0.4.0',
        'eth-utils>=1.10.0',
        'web3>=5.31.1',
        'cosmos==0.6.1',
        'bech32==1.2.0'
    ],
    description='Python SDK for Decimal blockchain',
    author='Decimal Team',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
