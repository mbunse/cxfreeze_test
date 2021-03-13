import glob
import os
import sys

from cx_Freeze import setup, Executable

# GUI applications require a different base on Windows (the default is for
# a console application).
base = "Console"
# if sys.platform == "win32":
#     base = "Win32GUI"

setup(
    name="cxfreezetest",
    description="""
                    Implementierung einer Regelbasierten Udk für die KE nach dem Vorbild https://git.easycredit.intern/projects/KI-MODELLE/repos/ke-umsatzdatenkategorisierung/browse/kategorisierung?at=refs%2Fheads%2Faktuelle_logik.
                    Funktionalität basiert auf einem Wrapper, welcher csv basierte Fachlogik anwendet um Umsätze gemäß Fachvorgaben zu kategorisieren (Fachlogik = Steuertabelle und wird von PMKE zugeliefert)  
                """,
    long_description=open('README.md').read(),
    packages=["cxfreezetest"],
    include_package_data=True,
    install_requires=['pandas', 'numpy'],
    entry_points={
        'console_scripts': ["app=cxfreezetest.app:main"],
    },
    executables=[Executable("cxfreezetest/app.py", base=base,
                            shortcut_name="cxfreezetest", shortcut_dir="ProgramMenuFolder")],
    options={
        # "build_exe": {
        #     "includes": ["pandas", "PySimpleGUI", ],
        #     "excludes": ["pytest", "unittest"],
        #     #"optimize": 2,
        #     "include_files": mkl_files + mkl_omp_files, # see https://github.com/marcelotduarte/cx_Freeze/issues/682#issuecomment-786474193
        # },
        "bdist_msi": {
            # generated with https://www.guidgen.com/
            "upgrade_code": "{33da850a-9e6e-41a4-81f5-281a3b5116bc}",
        }
    }
)
