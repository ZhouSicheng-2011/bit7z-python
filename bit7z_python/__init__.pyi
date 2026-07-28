from __future__ import annotations
from bit7z_python.bit7z_python import ArchiveStartOffset
from bit7z_python.bit7z_python import Bit7zLibrary
from bit7z_python.bit7z_python import BitArchiveItem
from bit7z_python.bit7z_python import BitCompressionLevel
from bit7z_python.bit7z_python import BitCompressionMethod
from bit7z_python.bit7z_python import BitError
from bit7z_python.bit7z_python import BitFailureSource
from bit7z_python.bit7z_python import BitFileCompressor
from bit7z_python.bit7z_python import BitFileExtractor
from bit7z_python.bit7z_python import BitInFormat
from bit7z_python.bit7z_python import BitInOutFormat
from bit7z_python.bit7z_python import BitPropVariantType
from bit7z_python.bit7z_python import BitProperty
from bit7z_python.bit7z_python import DeletePolicy
from bit7z_python.bit7z_python import EncryptionScope
from bit7z_python.bit7z_python import FilterPolicy
from bit7z_python.bit7z_python import FilterResult
from bit7z_python.bit7z_python import FolderPathPolicy
from bit7z_python.bit7z_python import FormatFeatures
from bit7z_python.bit7z_python import OverwriteMode
from bit7z_python.bit7z_python import SymlinkPolicy
from bit7z_python.bit7z_python import UpdateMode
import os as os
import pathlib as pathlib
import platform as platform
from . import bit7z_python
__all__: list[str] = ['ArchiveStartOffset', 'Bit7zLibrary', 'BitArchiveItem', 'BitCompressionLevel', 'BitCompressionMethod', 'BitError', 'BitFailureSource', 'BitFileCompressor', 'BitFileExtractor', 'BitInFormat', 'BitInOutFormat', 'BitPropVariantType', 'BitProperty', 'DEFAULT_7ZIP_DLL', 'DeletePolicy', 'EncryptionScope', 'FORMAT_7Z', 'FORMAT_APM', 'FORMAT_ARJ', 'FORMAT_AUTO', 'FORMAT_BZIP2', 'FORMAT_CAB', 'FORMAT_CHM', 'FORMAT_COFF', 'FORMAT_COMPOUND', 'FORMAT_CPIO', 'FORMAT_CRAMFS', 'FORMAT_DEB', 'FORMAT_DMG', 'FORMAT_ELF', 'FORMAT_EXT', 'FORMAT_FAT', 'FORMAT_FLV', 'FORMAT_GPT', 'FORMAT_GZIP', 'FORMAT_HFS', 'FORMAT_HXS', 'FORMAT_IHEX', 'FORMAT_ISO', 'FORMAT_LZH', 'FORMAT_LZMA', 'FORMAT_LZMA86', 'FORMAT_MACHO', 'FORMAT_MBR', 'FORMAT_MSLZ', 'FORMAT_MUB', 'FORMAT_NSIS', 'FORMAT_NTFS', 'FORMAT_PE', 'FORMAT_PPMD', 'FORMAT_QCOW', 'FORMAT_RAR', 'FORMAT_RAR5', 'FORMAT_RPM', 'FORMAT_SPLIT', 'FORMAT_SQUASHFS', 'FORMAT_SWF', 'FORMAT_SWFC', 'FORMAT_TAR', 'FORMAT_TE', 'FORMAT_UDF', 'FORMAT_UEFIC', 'FORMAT_UEFIS', 'FORMAT_VDI', 'FORMAT_VHD', 'FORMAT_VHDX', 'FORMAT_VMDK', 'FORMAT_WIM', 'FORMAT_XAR', 'FORMAT_XZ', 'FORMAT_Z', 'FORMAT_ZIP', 'FilterPolicy', 'FilterResult', 'FolderPathPolicy', 'FormatFeatures', 'OverwriteMode', 'SymlinkPolicy', 'UpdateMode', 'VERSION_INFO', 'bit7z_python', 'os', 'pathlib', 'platform']
def _set_dll_path():
    ...
DEFAULT_7ZIP_DLL: str = '7z.dll'
FORMAT_7Z: BitInOutFormat  # value = <bit7z_python.bit7z_python.BitInOutFormat object>
FORMAT_APM: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_ARJ: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_AUTO: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_BZIP2: BitInOutFormat  # value = <bit7z_python.bit7z_python.BitInOutFormat object>
FORMAT_CAB: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_CHM: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_COFF: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_COMPOUND: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_CPIO: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_CRAMFS: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_DEB: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_DMG: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_ELF: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_EXT: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_FAT: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_FLV: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_GPT: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_GZIP: BitInOutFormat  # value = <bit7z_python.bit7z_python.BitInOutFormat object>
FORMAT_HFS: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_HXS: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_IHEX: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_ISO: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_LZH: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_LZMA: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_LZMA86: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_MACHO: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_MBR: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_MSLZ: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_MUB: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_NSIS: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_NTFS: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_PE: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_PPMD: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_QCOW: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_RAR: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_RAR5: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_RPM: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_SPLIT: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_SQUASHFS: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_SWF: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_SWFC: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_TAR: BitInOutFormat  # value = <bit7z_python.bit7z_python.BitInOutFormat object>
FORMAT_TE: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_UDF: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_UEFIC: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_UEFIS: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_VDI: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_VHD: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_VHDX: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_VMDK: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_WIM: BitInOutFormat  # value = <bit7z_python.bit7z_python.BitInOutFormat object>
FORMAT_XAR: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_XZ: BitInOutFormat  # value = <bit7z_python.bit7z_python.BitInOutFormat object>
FORMAT_Z: BitInFormat  # value = <bit7z_python.bit7z_python.BitInFormat object>
FORMAT_ZIP: BitInOutFormat  # value = <bit7z_python.bit7z_python.BitInOutFormat object>
VERSION_INFO: str = '0.1.0'
__version__: str = '0.1.0'
