# cxfreeze Example

This project reproduces the issue reported here: https://github.com/marcelotduarte/cx_Freeze/issues/682

System setup: win10 1909, anaconda3

Two separate setup scripts are provided. `setup.py` is used to `pip` install the package, 
`setup_csfreeze.py` to build the installer.

To setup the environment run:
```
conda env create -f environment.yml
pip install --upgrade git+https://github.com/marcelotduarte/cx_Freeze.git@develop
python setup_cxfreeze.py bdist_msi
```