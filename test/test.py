import bit7z_python
import py7zr

import time as t
import shutil
import os
import platform

input("Press enter to start...")


print("Extract test starts.")
with py7zr.SevenZipFile(r"./GTK4.7z", "r") as fp:
    print("py7zr extracting ...")
    t0 = t.time()
    fp.extractall()
    t1 = t.time()
    print(f"py7zr used time (extraction): {t1 - t0} s")
    
shutil.rmtree(r"./GTK4")

input("Press enter to continue...")

print("bit7z-python extracting ...")
dll_name = r"7z.dll" if platform.system() == "Windows" else "7z.so"
lib = bit7z_python.Bit7zLibrary()
ext = bit7z_python.BitFileExtractor(lib, bit7z_python.FORMAT_AUTO)
t2 = t.time()
ext.extract(r"./GTK4.7z", r"./GTK4")
t3 = t.time()
print(f"bit7z-python used time (extraction): {t3 - t2} s")
del ext
shutil.rmtree(r"./GTK4")

input("Press enter to continue...")


print("Compression test starts.")

if os.cpu_count() is not None:
    cores = min(os.cpu_count(), 64) #type: ignore
else:
    cores = 1

filters = [{'id': py7zr.FILTER_LZMA2, 'preset': 9}]
with py7zr.SevenZipFile(r"test.7z", "w", filters=filters, mp=cores) as fp: # type: ignore
    print("py7zr compressing ...")
    t4 = t.time()
    fp.writeall(r"./wx_demos")
    t5 = t.time()
    print(f"py7zr used time (compression): {t5 - t4} s")
os.remove("test.7z")

input("Press enter to continue...")

print("bit7z-python compressing ...")
cps = bit7z_python.BitFileCompressor(lib, bit7z_python.FORMAT_7Z)
cps.set_compression_level(bit7z_python.BitCompressionLevel.Ultra)
cps.set_compression_method(bit7z_python.BitCompressionMethod.Lzma2)
cps.set_threads_count(cores) # type: ignore
t6 = t.time()
cps.compress_directory_contents(r"./wx_demos", r"./test.7z", True, "*")
t7 = t.time()
print(f"bit7z-python used time (compression): {t7 - t6} s")
del cps
os.remove("test.7z")
