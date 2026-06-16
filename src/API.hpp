/*
This is the main wrapper of bit7z for Python 3.8 or higher versions (pybind11-3.0.2)
*/

/*
If you want to use this program on Windows 7, please add "/DWIN7_COMPAT" opition in cl compiler command
*/
/*
Author: ZhouSicheng-2011
Date: 2026-05-01
License: This project is under the Apache-2.0 Lincense, see LICENSE for more details.
*/


#ifndef API_HPP
#define API_HPP

#ifdef WIN7_COMPAT
  #define _WIN32_WINNT 0x0601
  #define WINVER 0X0601
#endif

//Enable bit7z auto format detection
#ifndef BIT7Z_AUTO_FORMAT
#define BIT7Z_AUTO_FORMAT
#endif

//Enable bit7z regular expression matching
#ifndef BIT7Z_REGEX_MATCHING
#define BIT7Z_REGEX_MATCHING
#endif

//Convert macro to string
#define STRINGIFY_HELPER(x) #x
#define STRINGIFY(x) STRINGIFY_HELPER(x)
//Get version string
#ifndef VER_MAJOR
#define VER_MAJOR 0
#endif
#ifndef VER_MINOR
#define VER_MINOR 0
#endif
#ifndef VER_PATCH
#define VER_PATCH 0
#endif
#define VERSION_STRING STRINGIFY(VER_MAJOR) "." STRINGIFY(VER_MINOR) "." STRINGIFY(VER_PATCH)

//C++ standard headers include
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <thread>

//pybind11 headers include
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/gil.h>
namespace py = pybind11;
//Special Config to disable using native Python list to save time which is spent on converting
#include <pybind11/functional.h>
/*
PYBIND11_MAKE_OPAQUE(std::map<std::string, std::string>)
PYBIND11_MAKE_OPAQUE(std::vector<std::string>)
// Function: use py::list to construct std::vector<std::string>
std::vector<std::string> list_to_string_vec(const py::list& lst) {
    return lst.cast<std::vector<std::string>>();
}

// Function: use py::dict to construct std::map<std::string, std::string>
std::map<std::string, std::string> dict_to_string_map(const py::dict& d) {
    return d.cast<std::map<std::string, std::string>>();
}
*/
#define PYBIND11_DETAILED_ERROR_MESSAGES

//General bit7z headers
#include <bit7z.hpp>
using bit7z::tstring;

//My headers
#include <pyos.hpp>
#include <sysinfo.hpp>
#include <time.hpp>

#ifdef PYTHON_313_PLUS_FREE_THREADING_BUILD
#define PYTHON_NO_GIL
#endif

#endif