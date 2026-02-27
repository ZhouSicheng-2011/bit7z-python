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
const std::map<int, const bit7z::BitInFormat*> i_formatIndexMap = {
    {0,  &bit7z::BitFormat::APM},
    {1,  &bit7z::BitFormat::Arj},
    {2,  &bit7z::BitFormat::Auto},      // 需启用 BIT7Z_AUTO_FORMAT 宏，否则可移除
    {3,  &bit7z::BitFormat::Cab},
    {4,  &bit7z::BitFormat::Chm},
    {5,  &bit7z::BitFormat::COFF},
    {6,  &bit7z::BitFormat::Compound},
    {7,  &bit7z::BitFormat::Cpio},
    {8,  &bit7z::BitFormat::CramFS},
    {9,  &bit7z::BitFormat::Deb},
    {10, &bit7z::BitFormat::Dmg},
    {11, &bit7z::BitFormat::Elf},
    {12, &bit7z::BitFormat::Ext},
    {13, &bit7z::BitFormat::Fat},
    {14, &bit7z::BitFormat::Flv},
    {15, &bit7z::BitFormat::GPT},
    {16, &bit7z::BitFormat::Hfs},
    {17, &bit7z::BitFormat::Hxs},
    {18, &bit7z::BitFormat::IHex},
    {19, &bit7z::BitFormat::Iso},
    {20, &bit7z::BitFormat::Lzh},
    {21, &bit7z::BitFormat::Lzma},
    {22, &bit7z::BitFormat::Lzma86},
    {23, &bit7z::BitFormat::Macho},
    {24, &bit7z::BitFormat::Mbr},
    {25, &bit7z::BitFormat::Mslz},
    {26, &bit7z::BitFormat::Mub},
    {27, &bit7z::BitFormat::Nsis},
    {28, &bit7z::BitFormat::Ntfs},
    {29, &bit7z::BitFormat::Pe},
    {30, &bit7z::BitFormat::Ppmd},
    {31, &bit7z::BitFormat::QCow},
    {32, &bit7z::BitFormat::Rar},
    {33, &bit7z::BitFormat::Rar5},
    {34, &bit7z::BitFormat::Rpm},
    {35, &bit7z::BitFormat::Split},
    {36, &bit7z::BitFormat::SquashFS},
    {37, &bit7z::BitFormat::Swf},
    {38, &bit7z::BitFormat::Swfc},
    {39, &bit7z::BitFormat::TE},
    {40, &bit7z::BitFormat::Udf},
    {41, &bit7z::BitFormat::UEFIc},
    {42, &bit7z::BitFormat::UEFIs},
    {43, &bit7z::BitFormat::VDI},
    {44, &bit7z::BitFormat::Vhd},
    {45, &bit7z::BitFormat::Vhdx},
    {46, &bit7z::BitFormat::VMDK},
    {47, &bit7z::BitFormat::Xar},
    {48, &bit7z::BitFormat::Z}
};

const bit7z::BitInFormat* get_i_format_id(int id){
    return (i_formatIndexMap.at(id));
}

/*
const std::map<int, const bit7z::BitInOutFormat*> io_formatIndexMap = {
    
}
*/

void init_format(py::module& mod){
    ;
}