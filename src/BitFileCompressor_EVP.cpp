//bit7z header
#include <bitfilecompressor.hpp>
//Special Config
#include <pybind11/pybind11.h>
PYBIND11_MAKE_OPAQUE(std::map<std::string, std::string>)
PYBIND11_MAKE_OPAQUE(std::vector<std::string>)

//My headers
#include <API.hpp>

//BitFileCompressor interface
void init_bitcompressor(py::module& mod){
    py::class_<bit7z::BitFileCompressor>(mod, "BitFileCompressor")
        .def(py::init<const bit7z::Bit7zLibrary&, const bit7z::BitInOutFormat&>());
}