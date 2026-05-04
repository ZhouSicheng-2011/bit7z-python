/*
This file binds the BitFileCompressor, the file compressor of bit7z.
Author: ZhouSicheng-2011
Time: 2026-05-01
License: This project is under the Apache-2.0 Lincense, see LICENSE for more details.
*/

//bit7z header
#include <bitfilecompressor.hpp>

//My headers
#include <API.hpp>

//BitFileCompressor interface
void init_bitcompressor(py::module& mod){
    py::class_<bit7z::BitFileCompressor>(mod, "BitFileCompressor")
        //BitFileCompressor( const Bit7zLibrary& lib, const BitInOutFormat& format )
        .def(py::init<const bit7z::Bit7zLibrary&, const bit7z::BitInOutFormat&>())

        //void clearPassword() noexcept
        .def("clear_password", &bit7z::BitFileCompressor::clearPassword, "Clear the current password used by the handler. Calling clearPassword() will disable the encryption/decryption of archives.")
        
        //void compress( const std::map< tstring, tstring >& inPaths, const tstring& outFile ) const
        .def("compress", static_cast<void (bit7z::BitFileCompressor::*)(
            const std::map<tstring, tstring>&,
            const tstring&
        ) const>(&bit7z::BitFileCompressor::compress))
        
        //void compress( const std::vector< tstring >& inPaths, const tstring& outFile ) const
        .def("compress", static_cast<void (bit7z::BitFileCompressor::*)(
            const std::vector<tstring>&,
            const tstring&
        ) const>(&bit7z::BitFileCompressor::compress))
        
        //void compressDirectory( const tstring& inDir, const tstring& outFile ) const
        .def("compress_directory", &bit7z::BitFileCompressor::compressDirectory)
        
        //void compressDirectoryContents( const tstring& inDir, const tstring& outFile, bool recursive = true, const tstring& filter = "*" ) const
        .def("compress_directory_contents", &bit7z::BitFileCompressor::compressDirectoryContents)
        
        //void compressFile( const tstring& inFile, const tstring& outFile, const tstring& inputName = {} ) const
        .def("compress_file", static_cast<void (bit7z::BitFileCompressor::*)(
            const tstring&,
            const tstring&,
            const tstring&
        ) const>(&bit7z::BitFileCompressor::compressFile))
        ;
}