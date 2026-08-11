#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time as t
import shutil
import os
import psutil
import bit7z_python
import py7zr
import tracy_client as tracy

# ---------- Tracy 初始化 ----------
tracy.program_name("CompressionBenchmark")
tracy.thread_name("MainThread")
tracy.app_info("Comparing py7zr vs bit7z-python with memory/cpu monitoring")

# ---------- 监控控制 ----------
stop_event = threading.Event()

def monitor():
    """后台监控线程：持续记录 RSS 和 CPU 使用率并发送到 Tracy Plots"""
    mem_plot = tracy.plot_config("RSS (MB)", tracy.PlotFormatType.Number)
    cpu_plot = tracy.plot_config("CPU %", tracy.PlotFormatType.Number)
    assert mem_plot is not None, "Failed to create memory plot"
    assert cpu_plot is not None, "Failed to create CPU plot"
    
    while not stop_event.is_set():
        mem = psutil.Process().memory_info().rss / (1024 * 1024)
        cpu = psutil.cpu_percent(interval=0.2)   # 200ms 平均 CPU
        tracy.plot(mem_plot, mem)
        tracy.plot(cpu_plot, cpu)
        t.sleep(0.2)

# 启动监控线程
monitor_thread = threading.Thread(target=monitor, daemon=True)
monitor_thread.start()

# ---------- 辅助函数 ----------
def safe_remove(path):
    """安全删除文件或目录，忽略不存在的错误"""
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Warning: Could not remove {path} - {e}")

# ---------- 测试数据 ----------
ARCHIVE = "./GTK4.7z"
OUT_DIR = "./GTK4"
COMPRESS_SRC = "./wx_demos"
COMPRESS_DST = "./test.7z"

# 清理可能残留的旧文件/目录
safe_remove(OUT_DIR)
safe_remove(COMPRESS_DST)

# ========== 解压测试 ==========
print("=== Extract test ===")

# 1. py7zr 解压
print("py7zr extracting ...")
with tracy.ScopedZone(name="py7zr_extract"):
    t0 = t.time()
    with py7zr.SevenZipFile(ARCHIVE, "r") as fp:
        fp.extractall()
    elapsed = t.time() - t0
    tracy.message(f"py7zr_extract took {elapsed:.3f}s")
print(f"py7zr used time (extraction): {elapsed:.3f} s")
tracy.frame_mark()

# 2. bit7z 解压
print("bit7z-python extracting ...")
with tracy.ScopedZone(name="bit7z_extract"):
    lib = bit7z_python.Bit7zLibrary(r"7z.dll")
    ext = bit7z_python.BitFileExtractor(lib, bit7z_python.FORMAT_AUTO)
    t0 = t.time()
    ext.extract(ARCHIVE, OUT_DIR)
    elapsed = t.time() - t0
    tracy.message(f"bit7z_extract took {elapsed:.3f}s")
    del ext
print(f"bit7z-python used time (extraction): {elapsed:.3f} s")
tracy.frame_mark()

safe_remove(OUT_DIR)

# ========== 压缩测试 ==========
print("\n=== Compress test ===")

# 3. py7zr 压缩
print("py7zr compressing ...")
with tracy.ScopedZone(name="py7zr_compress"):
    t0 = t.time()
    with py7zr.SevenZipFile(COMPRESS_DST, "w") as fp:
        fp.writeall(COMPRESS_SRC)
    elapsed = t.time() - t0
    tracy.message(f"py7zr_compress took {elapsed:.3f}s")
print(f"py7zr used time (compression): {elapsed:.3f} s")
tracy.frame_mark()

safe_remove(COMPRESS_DST)

# 4. bit7z 压缩
print("bit7z-python compressing ...")
with tracy.ScopedZone(name="bit7z_compress"):
    cps = bit7z_python.BitFileCompressor(lib, bit7z_python.FORMAT_7Z)
    t0 = t.time()
    cps.compress_directory_contents(COMPRESS_SRC, COMPRESS_DST, True, "*")
    elapsed = t.time() - t0
    tracy.message(f"bit7z_compress took {elapsed:.3f}s")
    del cps
print(f"bit7z-python used time (compression): {elapsed:.3f} s")
tracy.frame_mark()

safe_remove(COMPRESS_DST)

# ---------- 停止监控 ----------
stop_event.set()
monitor_thread.join(timeout=1.0)

print("\nTest completed. All data sent to Tracy. Check the profiler GUI for detailed timeline and plots.")