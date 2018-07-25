from cx_Freeze import setup, Executable
import os
import PyPDF2, sys, tkinter

os.environ['TCL_LIBRARY'] = r'C:\Users\BillyErmlick\Anaconda3\tcl'
os.environ['TK_LIBRARY'] = r'C:\Users\BillyErmlick\Anaconda3\tcl\tk8.6'


base = None

executables = [Executable("mergePDF.py", base=base)]

packages = ["idna", "os","tkinter", "PyPDF2", "sys",]
files = [r'C:\Users\BillyErmlick\Anaconda3\DLLs\tcl86t.dll',r'C:\Users\BillyErmlick\Anaconda3\DLLs\tk86t.dll']
options = {
    'build_exe': {
        'packages':packages,
        'include_files':files
    },
}
setup(
    name = "<any name>",
    options = options,
    version = "1.0",
    description = '<any description>',
    executables = executables
)











#'python setup.py build' in directory
