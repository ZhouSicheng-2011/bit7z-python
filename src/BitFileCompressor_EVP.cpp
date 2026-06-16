/*
This file binds the BitFileCompressor, the file compressor of bit7z.
(For more details, see website https://github.com/rikyoz/bit7z/wiki/BitFileCompressor)
Author: ZhouSicheng-2011
Time: 2026-05-01
License: This project is under the Apache-2.0 Lincense, see LICENSE for more details.
*/

//My headers
#include <API.hpp>

//bit7z headers
#include <bitfilecompressor.hpp>

void init_BitFileCompressor(py::module_& mod){
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
        .def("compress_directory_contents", &bit7z::BitFileCompressor::compressDirectoryContents,
        py::arg("inDir"), py::arg("outFile"), py::arg("recursive") = true, py::arg("filter") = "*")
        
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
        ) const>(&bit7z::BitFileCompressor::compressFiles),
        py::arg("inDir"), py::arg("outFile"), py::arg("recursive")=true, py::arg("filter")="*")

        //const BitInOutFormat & compressionFormat() const noexcept
        .def("compression_format", &bit7z::BitFileCompressor::compressionFormat, py::return_value_policy::reference_internal)

        //BitCompressionLevel compressionLevel() const noexcept
        .def("compression_level", &bit7z::BitFileCompressor::compressionLevel)

        //BitCompressionMethod compressionMethod() const noexcept
        .def("compression_method", &bit7z::BitFileCompressor::compressionMethod)

        //bool cryptHeaders() const noexcept
        .def("crypt_headers", &bit7z::BitFileCompressor::cryptHeaders)

        //uint32_t dictionarySize() const noexcept
        .def("dictionary_size", &bit7z::BitFileCompressor::dictionarySize)

        //FileCallback fileCallback() const
        .def("file_callback", &bit7z::BitFileCompressor::fileCallback)

        //[virtual] const BitInFormat &override format() const noexcept
        .def("format", &bit7z::BitFileCompressor::format, py::return_value_policy::reference_internal)

        //bool isPasswordDefined() const noexcept
        .def("is_password_defined", &bit7z::BitFileCompressor::isPasswordDefined)

        //const Bit7zLibrary & library() const noexcept
        .def("library", &bit7z::BitFileCompressor::library, py::return_value_policy::reference_internal)

        //OverwriteMode overwriteMode() const
        .def("overwrite_mode", &bit7z::BitFileCompressor::overwriteMode)

        //tstring password() const
        .def("password", &bit7z::BitFileCompressor::password)

        //PasswordCallback passwordCallback() const
        .def("password_callback", &bit7z::BitFileCompressor::passwordCallback)

        //ProgressCallback progressCallback() const
        .def("progress_callback", &bit7z::BitFileCompressor::progressCallback)

        //RatioCallback ratioCallback() const
        .def("ratio_callback" , &bit7z::BitFileCompressor::ratioCallback)

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
        .def("set_overwrite_mode", &bit7z::BitFileCompressor::setOverwriteMode)

        //[virtual] void setPassword( const tstring& password ) override
        .def("set_password", static_cast<void (bit7z::BitFileCompressor::*)(
            const tstring&
        ) >(&bit7z::BitFileCompressor::setPassword))

        //void setPassword( const tstring& password, bool cryptHeaders )
        .def("set_password", static_cast<void (bit7z::BitFileCompressor::*)(
            const tstring&,
            bool
        ) >(&bit7z::BitFileCompressor::setPassword))

        //void setPasswordCallback( const PasswordCallback& callback )
        .def("set_password_callback", &bit7z::BitFileCompressor::setPasswordCallback)

        //void setProgressCallback( const ProgressCallback& callback )
        .def("set_progress_callback", &bit7z::BitFileCompressor::setProgressCallback)

        //void setRatioCallback( const RatioCallback& callback )
        .def("set_ratio_callback", &bit7z::BitFileCompressor::setRatioCallback)

        //void setRetainDirectories( bool retain ) noexcept
        .def("set_retain_directories", &bit7z::BitFileCompressor::setRetainDirectories)

        //void setSolidMode( bool solidMode ) noexcept
        .def("set_solid_mode", &bit7z::BitFileCompressor::setSolidMode)

        //void setStoreSymbolicLinks( bool storeSymlinks ) noexcept
        .def("set_store_symbolic_links", &bit7z::BitFileCompressor::setStoreSymbolicLinks)

        //void setThreadsCount( uint32_t threadsCount ) noexcept
        .def("set_threads_count", &bit7z::BitFileCompressor::setThreadsCount)

        //void setTotalCallback( const TotalCallback& callback )
        .def("set_total_callback", &bit7z::BitFileCompressor::setTotalCallback)

        //void setUpdateMode( bool canUpdate )
        //Deprecated since bit7z-4.0, and we won't use this API in new project

        //[virtual] void setUpdateMode( UpdateMode mode )
        .def("set_update_mode", static_cast<void (bit7z::BitFileCompressor::*)(
            bit7z::UpdateMode
        ) >(&bit7z::BitFileCompressor::setUpdateMode))

        //void setVolumeSize( uint64_t volumeSize ) noexcept
        .def("set_volume_size", &bit7z::BitFileCompressor::setVolumeSize)

        //void setWordSize( uint32_t wordSize )
        .def("set_word_size", &bit7z::BitFileCompressor::setWordSize)

        //bool solidMode() const noexcept
        .def("solid_mode", &bit7z::BitFileCompressor::solidMode)

        //bool storeSymbolicLinks() const noexcept
        .def("store_symbolic_links", &bit7z::BitFileCompressor::storeSymbolicLinks)

        //uint32_t threadsCount() const noexcept
        .def("threads_count", &bit7z::BitFileCompressor::threadsCount)

        //TotalCallback totalCallback() const
        .def("total_callback", &bit7z::BitFileCompressor::totalCallback)

        //UpdateMode updateMode() const noexcept
        .def("update_mode", &bit7z::BitFileCompressor::updateMode)

        //uint64_t volumeSize() const noexcept
        .def("volume_size", &bit7z::BitFileCompressor::volumeSize)

        //uint32_t wordSize() const noexcept
        .def("word_size", &bit7z::BitFileCompressor::wordSize)
        ;
}

#ifndef PYBIT7Z_MAIN //The macro of the main binding file
//Add some headers to let it be an independent test module
#include <Enums_EVP.cpp>
#include <Bit7zLibrary_EVP.cpp>
#include <BitFormat_EVP.cpp>

#ifdef PYTHON_NO_GIL //Compat Python 3.13+ free-threadind build
PYBIND11_MODULE(bfcps, mod, py::mod_gil_not_used()){
    init_lib(mod);
    init_enums(mod);
    init_formats(mod);
    init_BitFileCompressor(mod);
    mod.attr("VERSION_INFO") = VERSION_STRING;
}
#else //Just simple Python build
PYBIND11_MODULE(bfcps, mod){
    init_lib(mod);
    init_enums(mod);
    init_formats(mod);
    init_BitFileCompressor(mod);
    mod.attr("VERSION_INFO") = VERSION_STRING;
}
#endif

#endif