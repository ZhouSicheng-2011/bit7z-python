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

cmake = import('cmake')

py = import('python').find_installation(pure: false)
pybind11_dep = dependency('pybind11')

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

inc_dirs = [
    'include'
]

src = [
    'src/core.cpp'
]

py.extension_module('bit7z_python',
    sources: src,
    include_directories: inc_dirs,
    dependencies: [bit7z_dep, pybind11_dep],
    install: true
)