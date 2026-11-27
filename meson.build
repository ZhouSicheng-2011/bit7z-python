project('bit7z-python', 'cpp',
    version: '0.1.4',
    license: 'Apache-2.0',
    default_options: [
        'cpp_std=c++17',
        'buildtype=release',
        'warning_level=2',
        'python.install_env=auto'
    ],
    meson_version: '>=1.3.0'
)

# Import necessary modules
cmake = import('cmake')
py = import('python').find_installation(pure: false)
pybind11_dep = dependency('pybind11', version: '>=3.0.0')

# Pass the version macro of project
version_parts = meson.project_version().split('.')
cpp_args = [
  '-DVER_MAJOR=' + version_parts[0],
  '-DVER_MINOR=' + version_parts[1],
  '-DVER_PATCH=' + version_parts[2],
]

# Get whether the Python interpreter is free-threading build
python_is_free_threaded = py.get_variable('Py_GIL_DISABLED', 0) == 1
if python_is_free_threaded
  cpp_args += '-DPy_GIL_DISABLED=1'
endif

# Build bit7z
bit7z_opts = cmake.subproject_options()

bit7z_opts.add_cmake_defines({
    'BIT7Z_AUTO_FORMAT': 'ON',
    'BIT7Z_REGEX_MATCHING': 'ON',
    'CMAKE_BUILD_TYPE': 'Release',
    'CMAKE_POSITION_INDEPENDENT_CODE': 'ON'
})

bit7z_proj = cmake.subproject(
    'bit7z',
    options: bit7z_opts
)

bit7z_dep = bit7z_proj.dependency('bit7z')

# My project
inc_dirs = [
    'include'
]

src = [
    'src/core.cpp'
]

pkg_subdir = 'bit7z_python'

py.extension_module('bit7z_python',
    sources: src,
    subdir: pkg_subdir,
    include_directories: inc_dirs,
    dependencies: [bit7z_dep, pybind11_dep],
    cpp_args: cpp_args,
    install: true
)

# Collect necessary data
py.install_sources(
    [
        'bit7z_python/__init__.py',
        'bit7z_python/__init__.pyi',
        'bit7z_python/bit7z_python.pyi',
        'bit7z_python/py.typed'
    ],
    subdir: pkg_subdir
)

sevenzip_dir = py.get_install_dir() / pkg_subdir / '7zip'
host = host_machine.system()

if host == 'windows'
    install_data('bit7z_python/7zip/7z.dll', install_dir: sevenzip_dir)
elif host == 'linux'
    install_data('bit7z_python/7zip/7z.so', install_dir: sevenzip_dir)
elif host == 'darwin'
    install_data('bit7z_python/7zip/7z.dylib', install_dir: sevenzip_dir)
endif
