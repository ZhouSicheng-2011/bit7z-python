# bit7z-python
The Support of bit7z in Python

[![PyPI version](https://badge.fury.io/py/bit7z-python.svg)](https://pypi.org/project/bit7z-python/)
[![Python versions](https://img.shields.io/pypi/pyversions/bit7z-python.svg)](https://pypi.org/project/bit7z-python/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub Actions](https://github.com/ZhouSicheng-2011/bit7z-python/actions/workflows/ci.yml/badge.svg)](https://github.com/ZhouSicheng-2011/bit7z-python/actions)

⚠️Notice: this package needs **Python 3.9 or later**


## 🚀 Usage
To install, just simply use this command:
```sh
pip install bit7z-python
```
To verify install *(⚠️Not available in `v0.0.1` becuase there is a minor bug)*, run:
```sh
python -c "import bit7z_python; print(bit7z_python.__version__)"
``` 

### Quick Start

```python
import bit7z_python as b7z

lib = b7z.Bit7zLibrary()
compressor = b7z.BitFileCompressor(lib, b7z.FORMAT_7Z)

# 压缩整个目录
compressor.compress_directory_contents("./my_folder", "./archive.7z")

# 解压
extractor = b7z.BitFileExtractor(lib, b7z.FORMAT_AUTO)
extractor.extract("./archive.7z", "./output/")
```

## ⚡ Performance

Compared to pure-Python alternatives like `py7zr`, `bit7z-python` delivers **2.2x faster** decompression.

| Tool | Time | Relative Speed |
| :--- | :--- | :--- |
| `py7zr` (pure Python) | ~22.0s | 1x |
| **`bit7z-python`** | **~10.0s** | **2.2x** |

*Test environment: `Intel Core i5-1135G7 CPU`, `16GB RAM`, `Windows 10 22H2`, `Python 3.11`.* 

*The test files are located in the `test/` directory of this repository:*
- `test/GTK4.7z` — 137MB archive for extraction tests
- `test/wx_demos/` — 37MB folder for compression tests

Test code: (Needs package `py7zr`)
```python
import bit7z_python
import py7zr

import time as t
import shutil
import os


print("Extract test starts.")
with py7zr.SevenZipFile(r"./GTK4.7z", "r") as fp:
    print("py7zr extracting ...")
    t0 = t.time()
    fp.extractall()
    t1 = t.time()
    print(f"py7zr used time (extraction): {t1 - t0} s")
    
shutil.rmtree(r"./GTK4")

print("bit7z-python extracting ...")
lib = bit7z_python.Bit7zLibrary(r"7z.dll")
ext = bit7z_python.BitFileExtractor(lib, bit7z_python.FORMAT_AUTO)
t2 = t.time()
ext.extract(r"./GTK4.7z", r"./GTK4")
t3 = t.time()
print(f"bit7z-python used time (extraction): {t3 - t2} s")
shutil.rmtree(r"./GTK4")


print("Compression test starts.")
with py7zr.SevenZipFile(r"test.7z", "w") as fp:
    print("py7zr compressing ...")
    t4 = t.time()
    fp.writeall(r"./wx_demos")
    t5 = t.time()
    print(f"py7zr used time (compression): {t5 - t4} s")
os.remove("test.7z")

print("bit7z-python compressing ...")
cps = bit7z_python.BitFileCompressor(lib, bit7z_python.FORMAT_7Z)
t6 = t.time()
cps.compress_directory_contents(r"./wx_demos", r"./test.7z", True, "*")
t7 = t.time()
print(f"bit7z-python used time (compression): {t7 - t6} s")
os.remove("test.7z")

```


Test result:
```text
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: D:\QMDownload\Hotfix\Python\Files\test.py
Extract test starts.
py7zr extracting ...
py7zr used time (extraction): 20.60436773300171 s
bit7z-python extracting ...
bit7z-python used time (extraction): 9.123618602752686 s
Compression test starts.
py7zr compressing ...
py7zr used time (compression): 11.3125159740448 s
bit7z-python compressing ...
bit7z-python used time (compression): 5.000096797943115 s

```


## Status
This project is still **developing**.
However, the first release [has published](https://github.com/ZhouSicheng-2011/bit7z-python/releases/tag/v0.0.1)🚀, and more function will be added in the future releases.

## 🗺️ Roadmap

### Hotfix release v0.0.2
Since we have found some little bugs in local tests, we will fix them, link newest bit7z, but we won't provide full support for bit7z v4.1.0

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