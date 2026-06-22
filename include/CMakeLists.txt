cmake_minimum_required(VERSION 3.10)
project(pyos_lib)

# 要求 C++17 标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 所有生成物（可执行文件、动态库、导入库）都放到源码目录下的 dist 文件夹
set(DIST_DIR ${CMAKE_SOURCE_DIR}/dist)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${DIST_DIR})   # .exe, .dll
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${DIST_DIR})   # .so, .dylib
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${DIST_DIR})   # .lib (Windows 导入库)

# ---------- 添加对 MSVC 的特殊处理 ----------
if(MSVC)
    add_compile_options(/utf-8)                 # 指定源文件为 UTF-8
    add_definitions(-D_CRT_SECURE_NO_WARNINGS)  # 屏蔽安全警告
endif()
# --------------------------------------------


# 为 Linux/macOS 设置 RPATH，使可执行文件能在 dist 目录中找到动态库
if(UNIX)
    set(CMAKE_BUILD_RPATH "${DIST_DIR}")
endif()

# ---------- 动态库 pyos ----------
add_library(pyos SHARED pyos.cpp)

# 编译库时定义 pyos_EXPORTS，使 Windows 上的 __declspec(dllexport) 生效
target_compile_definitions(pyos PRIVATE pyos_EXPORTS)

# 让外部使用库时能正确包含头文件
target_include_directories(pyos PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# 对 GCC 8 及更早版本，需要额外链接 stdc++fs 库（GCC 9+ 内置支持）
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU" AND CMAKE_CXX_COMPILER_VERSION VERSION_LESS 9)
    target_link_libraries(pyos PUBLIC stdc++fs)
endif()
# 若你使用 Clang + libc++ 且需要链接 c++fs，可取消下一行注释：
# if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
#     target_link_libraries(pyos PUBLIC c++fs)
# endif()

# ---------- 测试可执行文件 example ----------
add_executable(example example.cpp)

# 链接动态库 pyos
target_link_libraries(example pyos)