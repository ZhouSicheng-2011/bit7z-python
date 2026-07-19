import os
import pathlib
import platform

__version__ = "0.0.2"

def _set_dll_path():
    dll_dir = pathlib.Path(__file__).parent / "7zip"

    if platform.system() == "Windows":
        os.add_dll_directory(str(dll_dir))
        current = os.environ.get("PATH")
        if current is not None:
            os.environ["PATH"] = current + ";" + str(dll_dir)
        else:
            os.environ["PATH"] = str(dll_dir)
    
    elif platform.system() == "Linux":
        current = os.environ.get("LD_LIBRARY_PATH")
        if current is not None:
            os.environ["LD_LIBRARY_PATH"] = current + ":" + str(dll_dir)
        else:
            os.environ["LD_LIBRARY_PATH"] = str(dll_dir)
    
    elif platform.system() == "Darwin":
        current = os.environ.get("DYLD_LIBRARY_PATH")
        if current is not None:
            os.environ["DYLD_LIBRARY_PATH"] = current + ":" + str(dll_dir)
        else:
            os.environ["DYLD_LIBRARY_PATH"] = str(dll_dir)
    
    else:
        raise OSError("This is not a supported platform!")

_set_dll_path()

from .bit7z_python import *        # pyright: ignore[reportMissingImports]