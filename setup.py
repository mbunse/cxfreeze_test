from setuptools import setup

setup(
    name="cxfreezetest",
    long_description=open('README.md').read(),
    packages=["cxfreezetest"],
    install_requires=['pandas', "numpy"],
    entry_points={
        'console_scripts': ["app=cxfreezetest.app:main"],
    },
)
