/*
This file binds the Bit7zLibrary, the DLL provider of bit7z.
(bit7z uses it to call the DLL of 7-zip, like 7z.dll, 7za.dll and so on)
(For more details, see website https://github.com/rikyoz/bit7z/wiki/7z-DLLs)
(To get the extra DLLs, download 7z-extra package from https://www.7-zip.org/a/7z2600-extra.7z)
(Want other versions of 7-zip DLLs? Use the version number you want to replace "2600" in the above URL, for example, "2501" for 7-zip 25.01)
Author: ZhouSicheng-2011
Time: 2026-02-26
License: This project is under the MIT Lincense, the whole text is after the source
*/


#include <API.hpp>
#include <bit7z/bitformat.hpp>

 // 跳转表：索引 -> BitInFormat 常量指针
const std::map<std::string, const bit7z::BitInFormat*> i_formatIndexMap = {
    {"APM",  &bit7z::BitFormat::APM},
    {"ARJ",  &bit7z::BitFormat::Arj},
    {"AUTO",  &bit7z::BitFormat::Auto},      // 需启用 BIT7Z_AUTO_FORMAT 宏，否则可移除
    {"CAB",  &bit7z::BitFormat::Cab},
    {"CHM",  &bit7z::BitFormat::Chm},
    {"COFF",  &bit7z::BitFormat::COFF},
    {"COMPOUND",  &bit7z::BitFormat::Compound},
    {"CPIO",  &bit7z::BitFormat::Cpio},
    {"CRAMFS",  &bit7z::BitFormat::CramFS},
    {"DEB",  &bit7z::BitFormat::Deb},
    {"DMG", &bit7z::BitFormat::Dmg},
    {"ELF", &bit7z::BitFormat::Elf},
    {"EXT", &bit7z::BitFormat::Ext},
    {"FAT", &bit7z::BitFormat::Fat},
    {"FLV", &bit7z::BitFormat::Flv},
    {"GPT", &bit7z::BitFormat::GPT},
    {"HFS", &bit7z::BitFormat::Hfs},
    {"HXS", &bit7z::BitFormat::Hxs},
    {"IHEX", &bit7z::BitFormat::IHex},
    {"ISO", &bit7z::BitFormat::Iso},
    {"LZH", &bit7z::BitFormat::Lzh},
    {"LZMA", &bit7z::BitFormat::Lzma},
    {"LZMA86", &bit7z::BitFormat::Lzma86},
    {"MACHO", &bit7z::BitFormat::Macho},
    {"MBR", &bit7z::BitFormat::Mbr},
    {"MSLZ", &bit7z::BitFormat::Mslz},
    {"MUB", &bit7z::BitFormat::Mub},
    {"NSIS", &bit7z::BitFormat::Nsis},
    {"NTFS", &bit7z::BitFormat::Ntfs},
    {"PE", &bit7z::BitFormat::Pe},
    {"PPMD", &bit7z::BitFormat::Ppmd},
    {"QCOW", &bit7z::BitFormat::QCow},
    {"RAR", &bit7z::BitFormat::Rar},
    {"RAR5", &bit7z::BitFormat::Rar5},
    {"RPM", &bit7z::BitFormat::Rpm},
    {"SPLIT", &bit7z::BitFormat::Split},
    {"SQUASHFS", &bit7z::BitFormat::SquashFS},
    {"SWF", &bit7z::BitFormat::Swf},
    {"SWFC", &bit7z::BitFormat::Swfc},
    {"TE", &bit7z::BitFormat::TE},
    {"UDF", &bit7z::BitFormat::Udf},
    {"UEFIC", &bit7z::BitFormat::UEFIc},
    {"UEFIS", &bit7z::BitFormat::UEFIs},
    {"VDI", &bit7z::BitFormat::VDI},
    {"VHD", &bit7z::BitFormat::Vhd},
    {"VHDX", &bit7z::BitFormat::Vhdx},
    {"VMDK", &bit7z::BitFormat::VMDK},
    {"XAR", &bit7z::BitFormat::Xar},
    {"Z", &bit7z::BitFormat::Z}
};

const bit7z::BitInFormat* get_i_format_id(const std::string& id){
    return (i_formatIndexMap.at(id));
}

/*
const std::map<int, const bit7z::BitInOutFormat*> io_formatIndexMap = {
    
}
*/

void init_format(py::module& mod){
    ;
}