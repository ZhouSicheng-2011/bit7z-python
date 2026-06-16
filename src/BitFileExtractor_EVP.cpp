/*
This file binds the BitFileExtractor, the file extractor of bit7z.
(For more details, see website https://github.com/rikyoz/bit7z/wiki/BitFileExtractor)
Author: ZhouSicheng-2011
Time: 2026-06-16
License: This project is under the Apache-2.0 Lincense, see LICENSE for more details.
*/

//My API header
#include <API.hpp>

//bit7z header
#include <bitfileextractor.hpp>

void init_BitFileExtractor(py::module_& mod){
    py::class_<bit7z::BitFileExtractor>(mod, "BitFileExtractor")
        //BitExtractor( const Bit7zLibrary& lib, const BitInFormat& format = BitFormat::Auto )
        .def(py::init<const bit7z::Bit7zLibrary&, const bit7z::BitInFormat&>(), py::arg("lib"), py::arg("format")=bit7z::BitFormat::Auto)
        
        //void clearPassword() noexcept
        .def("clear_password", &bit7z::BitFileExtractor::clearPassword)

        //void extract( const tstring& inArchive, const tstring& outDir = {} ) const
        .def("extract", static_cast<void (bit7z::BitFileExtractor::*)(
            const tstring&,
            const tstring&
        ) const>(&bit7z::BitFileExtractor::extract),
        py::arg("inArchive"), py::arg("outDir")="")

        //void extract( const tstring& inArchive, std::map< tstring, vector< byte_t > >& outMap ) const
        //...

        //void extract( const tstring& inArchive, std::ostream& outStream, uint32_t index = 0 ) const
        //...

        //void extract( const tstring& inArchive, vector< byte_t >& outBuffer, uint32_t index = 0 ) const
        //...

        //const BitInFormat & extractionFormat() const noexcept
        .def("extraction_format", &bit7z::BitFileExtractor::extractionFormat, py::return_value_policy::reference_internal)
        
        //void extractItems( const tstring& inArchive, const std::vector< uint32_t >& indices, const tstring& outDir = {} ) const
        .def("extract_items", &bit7z::BitFileExtractor::extractItems, 
        py::arg("inArchive"), py::arg("indices"), py::arg("outDir")="")

        //void extractMatching( const tstring& inArchive, const tstring& itemFilter, const tstring& outDir = {}, FilterPolicy policy = FilterPolicy::Include ) const
        .def("extract_matching", static_cast<void (bit7z::BitFileExtractor::*)(
            const tstring&,
            const tstring&,
            const tstring&,
            bit7z::FilterPolicy
        ) const>(&bit7z::BitFileExtractor::extractMatching),
        py::arg("inArchive"), py::arg("itemFilter"), py::arg("outDir")="",
        py::arg("policy")=bit7z::FilterPolicy::Include)

        //void extractMatching( const tstring& inArchive, const tstring& itemFilter, vector< byte_t >& outBuffer, FilterPolicy policy = FilterPolicy::Include ) const
        //...

        //void extractMatchingRegex( const tstring& inArchive, const tstring& regex, const tstring& outDir = {}, FilterPolicy policy = FilterPolicy::Include ) const
        .def("extract_matching_regex", static_cast<void (bit7z::BitFileExtractor::*)(
            const tstring&,
            const tstring&,
            const tstring&,
            bit7z::FilterPolicy
        ) const>(&bit7z::BitFileExtractor::extractMatchingRegex),
        py::arg("inArchive"), py::arg("regex"), py::arg("outDir")="",
        py::arg("policy")=bit7z::FilterPolicy::Include)

        //void extractMatchingRegex( const tstring& inArchive, const tstring& regex, vector< byte_t >& outBuffer, FilterPolicy policy = FilterPolicy::Include ) const
        //...

        //FileCallback fileCallback() const
        .def("file_callback", &bit7z::BitFileExtractor::fileCallback)

        //[virtual] const BitInFormat &override format() const noexcept
        .def("format", &bit7z::BitFileExtractor::format, py::return_value_policy::reference_internal)

        //bool isPasswordDefined() const noexcept
        .def("is_password_defined", &bit7z::BitFileExtractor::isPasswordDefined)

        //const Bit7zLibrary & library() const noexcept
        .def("library", &bit7z::BitFileExtractor::library, py::return_value_policy::reference_internal)

        //OverwriteMode overwriteMode() const
        .def("overwrite_mode", &bit7z::BitFileExtractor::overwriteMode)

        //tstring password() const
        .def("password", &bit7z::BitFileExtractor::password)

        //PasswordCallback passwordCallback() const
        .def("password_callback", &bit7z::BitFileExtractor::passwordCallback)

        //ProgressCallback progressCallback() const
        .def("progress_callback", &bit7z::BitFileExtractor::progressCallback)

        //RatioCallback ratioCallback() const
        .def("ratio_callback", &bit7z::BitFileExtractor::ratioCallback)

        //bool retainDirectories() const noexcept
        .def("retain_directories", &bit7z::BitFileExtractor::retainDirectories)

        //void setFileCallback( const FileCallback& callback )
        .def("set_file_callback", &bit7z::BitFileExtractor::setFileCallback)

        //void setOverwriteMode( OverwriteMode mode )
        .def("set_overwrite_mode", &bit7z::BitFileExtractor::setOverwriteMode)

        //[virtual] void setPassword( const tstring& password )
        .def("set_password", &bit7z::BitFileExtractor::setPassword)

        //void setPasswordCallback( const PasswordCallback& callback )
        .def("set_password_callback", &bit7z::BitFileExtractor::setPasswordCallback)

        //void setProgressCallback( const ProgressCallback& callback )
        .def("set_progress_callback", &bit7z::BitFileExtractor::setProgressCallback)

        //void setRatioCallback( const RatioCallback& callback )
        .def("set_ratio_callback", &bit7z::BitFileExtractor::setRatioCallback)

        //void setRetainDirectories( bool retain ) noexcept
        .def("set_retain_directories", &bit7z::BitFileExtractor::setRetainDirectories)

        //void setTotalCallback( const TotalCallback& callback )
        .def("set_total_callback", &bit7z::BitFileExtractor::setTotalCallback)

        //void test( const tstring& inArchive ) const
        .def("test", &bit7z::BitFileExtractor::test)

        //TotalCallback totalCallback() const
        .def("total_callback", &bit7z::BitFileExtractor::totalCallback)
        ;
}

#ifndef PYBIT7Z_MAIN //The macro of the main binding file
//Add some headers to let it be an independent test module
#include <Enums_EVP.cpp>
#include <Bit7zLibrary_EVP.cpp>
#include <BitFormat_EVP.cpp>

#ifdef PYTHON_NO_GIL //Compat Python 3.13+ free-threadind build
PYBIND11_MODULE(bfext, mod, py::mod_gil_not_used()){
    init_lib(mod);
    init_enums(mod);
    init_formats(mod);
    init_BitFileExtractor(mod);
    mod.attr("VERSION_INFO") = VERSION_STRING;
}
#else //Just simple Python build
PYBIND11_MODULE(bfext, mod){
    init_lib(mod);
    init_enums(mod);
    init_formats(mod);
    init_BitFileExtractor(mod);
    mod.attr("VERSION_INFO") = VERSION_STRING;
}
#endif

#endif