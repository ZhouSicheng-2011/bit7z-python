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

//Test macro in this file, just used for VS Code syntax check:
//#define PYBIT7Z_MAIN

//BitFileCompressor interface
#ifdef PYBIT7Z_MAIN     //The macro of main binding file of bit7z
//Create a function to bind "bit7z::BitFileCompressor"
void init_bitcompressor(py::module& mod){

#else   //Just compile this file
//Add some needed bindings
#include <Enums_EVP.cpp>
#include <Bit7zLibrary_EVP.cpp>
//Create a test module to check the binding after finish this file
#ifdef PYTHON_NO_GIL
PYBIND11_MODULE(bfcps, mod, py::mod_gil_not_used()){
#else
PYBIND11_MODULE(bfcps, mod){
#endif
    init_lib(mod);
    init_enums(mod);

#endif
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

        //void compress( const std::map< tstring, tstring >& inPaths, std::ostream& outStream ) const
        //...
        
        //void compress( const std::vector< tstring >& inPaths, const tstring& outFile ) const
        .def("compress", static_cast<void (bit7z::BitFileCompressor::*)(
            const std::vector<tstring>&,
            const tstring&
        ) const>(&bit7z::BitFileCompressor::compress))

        //void compress( const std::vector< tstring >& inPaths, std::ostream& outStream ) const
        //...
        
        //void compressDirectory( const tstring& inDir, const tstring& outFile ) const
        .def("compress_directory", &bit7z::BitFileCompressor::compressDirectory)
        
        //void compressDirectoryContents( const tstring& inDir, const tstring& outFile, bool recursive = true, const tstring& filter = "*" ) const
        .def("compress_directory_contents", &bit7z::BitFileCompressor::compressDirectoryContents)
        
        //void compressFile( const tstring& inFile, const tstring& outFile, const tstring& inputName = {} ) const
        .def("compress_file", static_cast<void (bit7z::BitFileCompressor::*)(
            const tstring&,
            const tstring&,
            const tstring&
        ) const>(&bit7z::BitFileCompressor::compressFile),
        py::arg("inFile"),
        py::arg("outFile"),
        py::arg("inputName") = "")

        //void compressFile( const tstring& inFile, ostream& outStream, const tstring& inputName = {} ) const
        //...

        //void compressFile( const tstring& inFile, vector< byte_t >& outBuffer, const tstring& inputName = {} ) const
        //...

        //void compressFiles( const std::vector< tstring >& inFiles, const tstring& outFile ) const
        .def("compress_files", static_cast<void (bit7z::BitFileCompressor::*)(
            const std::vector< tstring >& inFiles,
            const tstring& outFile 
        ) const>(&bit7z::BitFileCompressor::compressFiles))

        //void compressFiles( const tstring& inDir, const tstring& outFile, bool recursive = true, const tstring& filter = "*" ) const
        .def("compress_files", static_cast<void (bit7z::BitFileCompressor::*)(
            const tstring&,
            const tstring&,
            bool,
            const tstring&
        ) const>(&bit7z::BitFileCompressor::compressFiles))

        //const BitInOutFormat & compressionFormat() const noexcept
        .def("compression_format", &bit7z::BitFileCompressor::compressionFormat)

        //BitCompressionLevel compressionLevel() const noexcept
        .def("comprssion_level", &bit7z::BitFileCompressor::compressionLevel)

        //BitCompressionMethod compressionMethod() const noexcept
        .def("compression_method", &bit7z::BitFileCompressor::compressionMethod)

        //bool cryptHeaders() const noexcept
        .def("crypt_headers", &bit7z::BitFileCompressor::cryptHeaders)

        //uint32_t dictionarySize() const noexcept
        .def("dictionary_size", &bit7z::BitFileCompressor::dictionarySize)

        //FileCallback fileCallback() const
        .def("file_callback", &bit7z::BitFileCompressor::fileCallback)

        //[virtual] const BitInFormat &override format() const noexcept
        .def("format", &bit7z::BitFileCompressor::format)

        //bool isPasswordDefined() const noexcept
        .def("is_password_defined", bit7z::BitFileCompressor::isPasswordDefined)

        //const Bit7zLibrary & library() const noexcept
        .def("library", &bit7z::BitFileCompressor::library)

        //OverwriteMode overwriteMode() const
        .def("overwrite_mode", &bit7z::BitFileCompressor::overwriteMode)

        //tstring password() const
        .def("passowrd", &bit7z::BitFileCompressor::password)

        //PasswordCallback passwordCallback() const
        .def("password_callback", &bit7z::BitFileCompressor::passwordCallback)

        //ProgressCallback progressCallback() const
        .def("progress_callback", &bit7z::BitFileCompressor::progressCallback)

        //RatioCallback ratioCallback() const
        .def("ratio_calllback" , &bit7z::BitFileCompressor::ratioCallback)

        //bool retainDirectories() const noexcept
        .def("retain_directories", &bit7z::BitFileCompressor::retainDirectories)

        //void setCompressionLevel( BitCompressionLevel level ) noexcept
        .def("set_compression_level", &bit7z::BitFileCompressor::setCompressionLevel)

        //void setCompressionMethod( BitCompressionMethod method )
        .def("set_compression_method", &bit7z::BitFileCompressor::setCompressionMethod)

        //void setDictionarySize( uint32_t dictionarySize )
        .def("set_dictionary_size", &bit7z::BitFileCompressor::setDictionarySize)

        //void setFileCallback( const FileCallback& callback )
        .def("set_file_callback", &bit7z::BitFileCompressor::setFileCallback)

        //void setFormatProperty( const wchar_t(&) name, const T& value ) noexcept
        //...

        //void setFormatProperty( const wchar_t(&) name, T value ) noexcept
        //...

        //void setOverwriteMode( OverwriteMode mode )
        .def("set_overweite_mode", &bit7z::BitFileCompressor::setOverwriteMode)

        //[virtual] void setPassword( const tstring& password ) override
        .def("set_password", static_cast<void (bit7z::BitFileCompressor::*)(
            const tstring&
        ) const>(&bit7z::BitFileCompressor::setPassword))
        ;

#ifdef PYBIT7Z_MAIN
}   //Finish the defination of the binding fuction
#else
}   //Finish the defination of the test module
#endif
