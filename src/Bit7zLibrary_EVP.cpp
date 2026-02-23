/*
This file binds the Bit7zLibrary, the DLL provider of bit7z.
(bit7z uses it to call the DLL of 7-zip, like 7z.dll, 7za.dll and so on)
(For more details, see website https://github.com/rikyoz/bit7z/wiki/7z-DLLs)
(To get the extra DLLs, download 7z-extra package from https://www.7-zip.org/a/7z2600-extra.7z)
Author: ZhouSicheng-2011
Time: 2026-02-23
License: This project is under the MIT Lincense, the whole text is after the source
*/

#include <bit7z/bit7zlibrary.hpp>
#include <API.hpp>

void init_lib(py::module& mod){
    // Bind the Bit7zLibrary class
}