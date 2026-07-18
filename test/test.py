import bit7z_python
import py7zr

import time as t
import shutil
import os


print("Extract test starts.")
with py7zr.SevenZipFile(r"D:\GTK4.7z", "r") as fp:
    print("py7zr extracting ...")
    t0 = t.time()
    fp.extractall()
    t1 = t.time()
    print(f"py7zr used time (extraction): {t1 - t0} s")
    
shutil.rmtree(r".\GTK4")

print("bit7z-python extracting ...")
lib = bit7z_python.Bit7zLibrary(r"7z.dll")
ext = bit7z_python.BitFileExtractor(lib, bit7z_python.FORMAT_AUTO)
t2 = t.time()
ext.extract(r"D:\GTK4.7z", r"D:\GTK4")
t3 = t.time()
print(f"bit7z-python used time (extraction): {t3 - t2} s")
shutil.rmtree(r"D:\GTK4")


print("Compression test starts.")
with py7zr.SevenZipFile(r"test.7z", "w") as fp:
    print("py7zr compressing ...")
    t4 = t.time()
    fp.writeall(r"D:\我的文档\Pictures\wx")
    t5 = t.time()
    print(f"py7zr used time (compression): {t5 - t4} s")
os.remove("test.7z")

print("bit7z-python compressing ...")
cps = bit7z_python.BitFileCompressor(lib, bit7z_python.FORMAT_7Z)
t6 = t.time()
cps.compress_directory_contents(r"D:\我的文档\Pictures\wx", r".\test.7z", True, "*")
t7 = t.time()
print(f"py7zr used time (compression): {t7 - t6} s")
os.remove("test.7z")
