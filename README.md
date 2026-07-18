# bit7z-python
The Support of bit7z in Python

⚠️Notice: this package needs **Python 3.9 or later**

## ⚡ Performance

Compared to pure-Python alternatives like `py7zr`, `bit7z-python` delivers **2.2x faster** decompression.

| Tool | Time | Relative Speed |
| :--- | :--- | :--- |
| `py7zr` (pure Python) | ~22.0s | 1x |
| **`bit7z-python`** | **~10.0s** | **2.2x** |

*Test environment: `Intel Core i5-1135G7 CPU`, `16GB RAM`, `Windows 10 22H2`, `Python 3.11`.* 

*Archive (will be uploaded later): 137MB 7z file containing EXE, DLL, C/C++ headers, images, etc.*

Test code: (Needs package `py7zr`)
```python
import bit7z_python
import py7zr

import time as t
import shutil


with py7zr.SevenZipFile(r"D:\GTK4.7z", "r") as fp:
    t0 = t.time()
    fp.extractall()
    t1 = t.time()
    print(f"py7zr used time: {t1 - t0} s")
    shutil.rmtree(r".\GTK4")


lib = bit7z_python.Bit7zLibrary(r"7z.dll")
ext = bit7z_python.BitFileExtractor(lib, bit7z_python.FORMAT_AUTO)
t2 = t.time()
ext.extract(r"D:\GTK4.7z", r"D:\GTK4")
t3 = t.time()
print(f"bit7z-python used time: {t3 - t2} s")
shutil.rmtree(r"D:\GTK4")
```


Test result:
```powershell
PS C:\Users\Administrator> cd D:\QMDownload\Hotfix\Python\Files
PS D:\QMDownload\Hotfix\Python\Files> .\test.dist\test.exe     # Packaged test program, uses MinGW64 compiler downloaded by Nuitka
py7zr used time: 22.08535408973694 s
bit7z-python used time: 9.906861782073975 s
PS D:\QMDownload\Hotfix\Python\Files> py -3.11 test.py         # Raw test program
py7zr used time: 21.76419186592102 s
bit7z-python used time: 10.00881052017212 s
PS D:\QMDownload\Hotfix\Python\Files>
```


## Usage
To install, just simply use this command:
```sh
pip install bit7z-python
```

## Status
This project is still **developing**.
However, the first release [has published](https://github.com/ZhouSicheng-2011/bit7z-python/releases/tag/v0.0.1)🚀, and more function will be added in the future releases.

## 🗺️ Roadmap

### v0.1.0 (Next Release)
- Upgrade bit7z to v4.1.0
- API compatibility updates (no breaking changes)
- Performance improvements from bit7z v4.1.0

### v0.2.0 ~ v1.0.0
- [ ] `BitArchiveEditor` — edit existing archives (add/remove/update)
- [ ] `BitArchiveWriter` — create archives
- [ ] `BitArchiveReader` — read archive metadata

### v1.0.0+
- [ ] Memory compression/decompression (`BitMemCompressor`/`BitMemExtractor`)
- [ ] Stream compression/decompression
- [ ] Nested archive support (v4.1.0 feature)

### Goal
Provide a **full-featured, convenient, and efficient** compression library for Python.

## 📖 Documentation

For now, please refer to the [bit7z Wiki](https://github.com/rikyoz/bit7z/wiki) for API details.  
The Python API follows the same structure with **PEP8** naming conventions:

| bit7z (C++) | bit7z-python (Python) |
| :--- | :--- |
| `compressFiles()` | `compress_files()` |
| `extractArchive()` | `extract_archive()` |
| `BitFileCompressor` | `BitFileCompressor` (same) |

Full API documentation is planned for future releases.

## License
This project is under the Apache-2.0 License, see [here](./LICENSE) for more details