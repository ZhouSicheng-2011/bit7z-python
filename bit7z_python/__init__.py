import os
import pathlib
import platform


def _get_dll_path() -> str:
    dll_dir = pathlib.Path(__file__).parent / "7zip"

    if platform.system() == "Windows":
        # Keep raw code since environmental variable can work on Windows
        current = os.environ.get("PATH")
        if current is not None:
            os.environ["PATH"] = current + ";" + str(dll_dir)
        else:
            os.environ["PATH"] = str(dll_dir)

        return os.path.normpath(os.path.join(str(dll_dir), "7z.dll"))
    
    elif platform.system() == "Linux":
        return os.path.normpath(os.path.join(str(dll_dir), "7z.so"))
    
    elif platform.system() == "Darwin":
        return os.path.normpath(os.path.join(str(dll_dir), "7z.dylib"))
    
    else:
        raise OSError("This is not a supported platform!")

default_7zip_lib_path = _get_dll_path()

from .bit7z_python import *

__version__ = VERSION_INFO