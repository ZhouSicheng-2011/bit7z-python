/*
This file is the main binding file.
Author: ZhouSicheng-2011
Time: 2026-06-18
License: This project is under the Apache-2.0 Lincense, see LICENSE for more details.
*/

#define BIT7Z_PYTHON_MAIN

//Include main API provider
#include <API.hpp>

//Include binding files
#include <Enums_EVP.cpp>
#include <Bit7zLibrary_EVP.cpp>
#include <BitFormat_EVP.cpp>
#include <BitFileExtractor_EVP.cpp>
#include <BitFileCompressor_EVP.cpp>

//Main module
#ifdef PYTHON_NO_GIL
PYBIND11_MODULE(bit7z_python, mod, py::mod_gil_not_used()){
    init_enums(mod);
    init_lib(mod);
    init_formats(mod);
    init_BitFileCompressor(mod);
    init_BitFileExtractor(mod);
}
#else
PYBIND11_MODULE(bit7z_python, mod){
    init_enums(mod);
    init_lib(mod);
    init_formats(mod);
    init_BitFileCompressor(mod);
    init_BitFileExtractor(mod);
}
#endif