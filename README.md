# bit7z-python
The Support of bit7z in Python

[![PyPI version](https://img.shields.io/pypi/v/bit7z-python.svg?label=PyPI&color=blue)](https://pypi.org/project/bit7z-python/)
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

## ⚡ Performance

Compared to pure‑Python alternatives like `py7zr`, `bit7z‑python` delivers **~2.2× faster extraction** and **~2.85× faster compression** — thanks to the underlying C++ 7‑zip library.

| Operation | `py7zr` (pure Python) | **`bit7z‑python`** | Speedup |
| :-------- | --------------------: | -----------------: | ------: |
| **Extract** (137 MB) | 44.88 s | **20.18 s** | **2.22×** |
| **Compress** (37 MB) | 16.63 s | **5.83 s** | **2.85×** |

*Test environment:*  
`Intel Core i5‑6500`, `16 GB RAM`, `Windows 10 22H2`, `Python 3.14.3 free‑threading`

Test archives are located in the `test/` directory of this repository:  
- `test/GTK4.7z` — 137 MB archive for extraction tests  
- `test/wx_demos/` — 37 MB folder for compression tests

Run the benchmark yourself with the included [`test/test.py`](./test/test.py) script (requires `py7zr` installed).


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