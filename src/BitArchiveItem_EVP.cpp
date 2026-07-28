/*
This file binds the BitFileCompressor, the file compressor of bit7z.
(For more details, see website https://github.com/rikyoz/bit7z/wiki/BitArchiveItem)
Author: ZhouSicheng-2011
Time: 2026-07-28
License: This project is under the Apache-2.0 Lincense, see LICENSE for more details.
*/

// Public API header
#include <API.hpp>

//Needed bit7z header
#include <bitarchiveitem.hpp>

void init_BitArchiveItem(py::module_& mod){
    py::class_<bit7z::BitArchiveItem>(mod, "BitArchiveItem")
        .def("attributes", &bit7z::BitArchiveItem::attributes)
        .def("crc", &bit7z::BitArchiveItem::crc)
        .def("creation_time", &bit7z::BitArchiveItem::creationTime)
        .def("extension", &bit7z::BitArchiveItem::extension)
        .def("index", &bit7z::BitArchiveItem::index)
        .def("is_dir", &bit7z::BitArchiveItem::isDir)
        .def("is_encrypted", &bit7z::BitArchiveItem::isEncrypted)
        .def("is_symlink", &bit7z::BitArchiveItem::isSymLink)
        .def("item_property", &bit7z::BitArchiveItem::itemProperty)
        .def("last_access_time", &bit7z::BitArchiveItem::lastAccessTime)
        .def("last_write_time", &bit7z::BitArchiveItem::lastWriteTime)
        .def("name", &bit7z::BitArchiveItem::name)
        .def("native_name", &bit7z::BitArchiveItem::nativeName)
        .def("native_path", &bit7z::BitArchiveItem::nativePath)
        .def("pack_size", &bit7z::BitArchiveItem::packSize)
        .def("path", &bit7z::BitArchiveItem::path)
        .def("raw_path", &bit7z::BitArchiveItem::rawPath)
        .def("size", &bit7z::BitArchiveItem::size);
}