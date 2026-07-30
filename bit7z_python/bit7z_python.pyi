from __future__ import annotations
import bit7z_python
import collections.abc
import enum
import typing
__all__: list[str] = ['ArchiveStartOffset', 'Bit7zLibrary', 'BitArchiveItem', 'BitCompressionLevel', 'BitCompressionMethod', 'BitError', 'BitFailureSource', 'BitFileCompressor', 'BitFileExtractor', 'BitInFormat', 'BitInOutFormat', 'BitPropVariantType', 'BitProperty', 'DEFAULT_7ZIP_DLL', 'DeletePolicy', 'EncryptionScope', 'FORMAT_7Z', 'FORMAT_APM', 'FORMAT_ARJ', 'FORMAT_AUTO', 'FORMAT_BZIP2', 'FORMAT_CAB', 'FORMAT_CHM', 'FORMAT_COFF', 'FORMAT_COMPOUND', 'FORMAT_CPIO', 'FORMAT_CRAMFS', 'FORMAT_DEB', 'FORMAT_DMG', 'FORMAT_ELF', 'FORMAT_EXT', 'FORMAT_FAT', 'FORMAT_FLV', 'FORMAT_GPT', 'FORMAT_GZIP', 'FORMAT_HFS', 'FORMAT_HXS', 'FORMAT_IHEX', 'FORMAT_ISO', 'FORMAT_LZH', 'FORMAT_LZMA', 'FORMAT_LZMA86', 'FORMAT_MACHO', 'FORMAT_MBR', 'FORMAT_MSLZ', 'FORMAT_MUB', 'FORMAT_NSIS', 'FORMAT_NTFS', 'FORMAT_PE', 'FORMAT_PPMD', 'FORMAT_QCOW', 'FORMAT_RAR', 'FORMAT_RAR5', 'FORMAT_RPM', 'FORMAT_SPLIT', 'FORMAT_SQUASHFS', 'FORMAT_SWF', 'FORMAT_SWFC', 'FORMAT_TAR', 'FORMAT_TE', 'FORMAT_UDF', 'FORMAT_UEFIC', 'FORMAT_UEFIS', 'FORMAT_VDI', 'FORMAT_VHD', 'FORMAT_VHDX', 'FORMAT_VMDK', 'FORMAT_WIM', 'FORMAT_XAR', 'FORMAT_XZ', 'FORMAT_Z', 'FORMAT_ZIP', 'FilterPolicy', 'FilterResult', 'FolderPathPolicy', 'FormatFeatures', 'OverwriteMode', 'SymlinkPolicy', 'UpdateMode', 'VERSION_INFO']
class ArchiveStartOffset(enum.Enum):
    FileStart: typing.ClassVar[ArchiveStartOffset]  # value = <ArchiveStartOffset.FileStart: 1>
    NoneOffset: typing.ClassVar[ArchiveStartOffset]  # value = <ArchiveStartOffset.NoneOffset: 0>
class Bit7zLibrary:
    def __init__(self, library_path: str = '7z.dll') -> None:
        """
        Constructs a Bit7zLibrary object by loading the specified 7zip shared library. By default, it searches a 7z.dll in the same path of the application. Args: libraryPath(str): the path to the shared library file to be loaded.
        """
    def set_large_page_mode(self) -> None:
        """
        [Deprecated] Set the 7-zip shared library to use large memory pages.
        """
    def use_large_pages(self) -> None:
        """
        Set the 7-zip shared library to use large memory pages.
        """
class BitArchiveItem:
    def attributes(self) -> int:
        ...
    def crc(self) -> int:
        ...
    def creation_time(self) -> ...:
        ...
    def extension(self) -> str:
        ...
    def index(self) -> int:
        ...
    def is_dir(self) -> bool:
        ...
    def is_encrypted(self) -> bool:
        ...
    def is_symlink(self) -> bool:
        ...
    def item_property(self, arg0: BitProperty) -> ...:
        ...
    def last_access_time(self) -> ...:
        ...
    def last_write_time(self) -> ...:
        ...
    def name(self) -> str:
        ...
    def native_name(self) -> str:
        ...
    def native_path(self) -> str:
        ...
    def pack_size(self) -> int:
        ...
    def path(self) -> str:
        ...
    def raw_path(self) -> str:
        ...
    def size(self) -> int:
        ...
class BitCompressionLevel(enum.Enum):
    Fast: typing.ClassVar[BitCompressionLevel]  # value = <BitCompressionLevel.Fast: 3>
    Fastest: typing.ClassVar[BitCompressionLevel]  # value = <BitCompressionLevel.Fastest: 1>
    Max: typing.ClassVar[BitCompressionLevel]  # value = <BitCompressionLevel.Max: 7>
    NoneCompression: typing.ClassVar[BitCompressionLevel]  # value = <BitCompressionLevel.NoneCompression: 0>
    Normal: typing.ClassVar[BitCompressionLevel]  # value = <BitCompressionLevel.Normal: 5>
    Ultra: typing.ClassVar[BitCompressionLevel]  # value = <BitCompressionLevel.Ultra: 9>
class BitCompressionMethod(enum.Enum):
    BZip2: typing.ClassVar[BitCompressionMethod]  # value = <BitCompressionMethod.BZip2: 3>
    Copy: typing.ClassVar[BitCompressionMethod]  # value = <BitCompressionMethod.Copy: 0>
    Deflate: typing.ClassVar[BitCompressionMethod]  # value = <BitCompressionMethod.Deflate: 1>
    Deflate64: typing.ClassVar[BitCompressionMethod]  # value = <BitCompressionMethod.Deflate64: 2>
    Lzma: typing.ClassVar[BitCompressionMethod]  # value = <BitCompressionMethod.Lzma: 4>
    Lzma2: typing.ClassVar[BitCompressionMethod]  # value = <BitCompressionMethod.Lzma2: 5>
    Ppmd: typing.ClassVar[BitCompressionMethod]  # value = <BitCompressionMethod.Ppmd: 6>
class BitError(enum.Enum):
    Fail: typing.ClassVar[BitError]  # value = <BitError.Fail: 1>
    FilterNotSpecified: typing.ClassVar[BitError]  # value = <BitError.FilterNotSpecified: 2>
    FormatFeatureNotSupported: typing.ClassVar[BitError]  # value = <BitError.FormatFeatureNotSupported: 3>
    IndicesNotSpecified: typing.ClassVar[BitError]  # value = <BitError.IndicesNotSpecified: 4>
    InvalidArchivePath: typing.ClassVar[BitError]  # value = <BitError.InvalidArchivePath: 5>
    InvalidCompressionMethod: typing.ClassVar[BitError]  # value = <BitError.InvalidCompressionMethod: 7>
    InvalidDictionarySize: typing.ClassVar[BitError]  # value = <BitError.InvalidDictionarySize: 8>
    InvalidDirectoryPath: typing.ClassVar[BitError]  # value = <BitError.InvalidDirectoryPath: 23>
    InvalidIndex: typing.ClassVar[BitError]  # value = <BitError.InvalidIndex: 9>
    InvalidItemPath: typing.ClassVar[BitError]  # value = <BitError.InvalidItemPath: 26>
    InvalidOutputBufferSize: typing.ClassVar[BitError]  # value = <BitError.InvalidOutputBufferSize: 6>
    InvalidWordSize: typing.ClassVar[BitError]  # value = <BitError.InvalidWordSize: 10>
    InvalidZipPassword: typing.ClassVar[BitError]  # value = <BitError.InvalidZipPassword: 22>
    ItemHasAbsolutePath: typing.ClassVar[BitError]  # value = <BitError.ItemHasAbsolutePath: 25>
    ItemIsAFolder: typing.ClassVar[BitError]  # value = <BitError.ItemIsAFolder: 11>
    ItemMarkedAsDeleted: typing.ClassVar[BitError]  # value = <BitError.ItemMarkedAsDeleted: 12>
    ItemPathOutsideOutputDirectory: typing.ClassVar[BitError]  # value = <BitError.ItemPathOutsideOutputDirectory: 24>
    NoMatchingFile: typing.ClassVar[BitError]  # value = <BitError.NoMatchingFile: 14>
    NoMatchingItems: typing.ClassVar[BitError]  # value = <BitError.NoMatchingItems: 13>
    NoMatchingSignature: typing.ClassVar[BitError]  # value = <BitError.NoMatchingSignature: 15>
    NonEmptyOutputBuffer: typing.ClassVar[BitError]  # value = <BitError.NonEmptyOutputBuffer: 16>
    NullOutputBuffer: typing.ClassVar[BitError]  # value = <BitError.NullOutputBuffer: 17>
    RequestedWrongVariantType: typing.ClassVar[BitError]  # value = <BitError.RequestedWrongVariantType: 18>
    UnsupportedOperation: typing.ClassVar[BitError]  # value = <BitError.UnsupportedOperation: 19>
    UnsupportedVariantType: typing.ClassVar[BitError]  # value = <BitError.UnsupportedVariantType: 20>
    WrongUpdateMode: typing.ClassVar[BitError]  # value = <BitError.WrongUpdateMode: 21>
class BitFailureSource(enum.Enum):
    CRCError: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.CRCError: 0>
    DataAfterEnd: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.DataAfterEnd: 1>
    DataError: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.DataError: 2>
    FormatDetectionError: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.FormatDetectionError: 5>
    HeadersError: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.HeadersError: 6>
    InvalidArchive: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.InvalidArchive: 3>
    InvalidArgument: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.InvalidArgument: 4>
    NoSuchItem: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.NoSuchItem: 7>
    OperationNotPermitted: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.OperationNotPermitted: 9>
    OperationNotSupported: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.OperationNotSupported: 8>
    UnavailableData: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.UnavailableData: 10>
    UnexpectedEnd: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.UnexpectedEnd: 11>
    WrongPassword: typing.ClassVar[BitFailureSource]  # value = <BitFailureSource.WrongPassword: 12>
class BitFileCompressor:
    def __init__(self, arg0: Bit7zLibrary, arg1: BitInOutFormat) -> None:
        ...
    def clear_password(self) -> None:
        """
        Clear the current password used by the handler. Calling clear_password() will disable the encryption/decryption of archives.
        """
    @typing.overload
    def compress(self, in_paths: collections.abc.Mapping[str, str], out_file: str) -> None:
        ...
    @typing.overload
    def compress(self, in_paths: collections.abc.Sequence[str], out_file: str) -> None:
        ...
    @typing.overload
    def compress(self, in_paths: collections.abc.Sequence[tuple[str, str]], out_file: str) -> None:
        ...
    def compress_directory(self, in_dir: str, out_file: str) -> None:
        ...
    def compress_directory_contents(self, in_dir: str, out_file: str, recursive: bool = True, filter: str = '*') -> None:
        ...
    def compress_file(self, in_file: str, out_file: str, input_name: str = '') -> None:
        ...
    @typing.overload
    def compress_files(self, in_files: collections.abc.Sequence[str], out_file: str) -> None:
        ...
    @typing.overload
    def compress_files(self, in_dir: str, out_file: str, recursive: bool = True, filter: str = '*') -> None:
        ...
    def compression_format(self) -> BitInOutFormat:
        ...
    def compression_level(self) -> BitCompressionLevel:
        ...
    def compression_method(self) -> BitCompressionMethod:
        ...
    def crypt_headers(self) -> bool:
        ...
    def dictionary_size(self) -> int:
        ...
    def file_callback(self) -> collections.abc.Callable[[str], None]:
        ...
    def format(self) -> BitInFormat:
        ...
    def is_password_defined(self) -> bool:
        ...
    def library(self) -> Bit7zLibrary:
        ...
    def overwrite_mode(self) -> OverwriteMode:
        ...
    def password(self) -> str:
        ...
    def password_callback(self) -> collections.abc.Callable[[], str]:
        ...
    def progress_callback(self) -> collections.abc.Callable[[typing.SupportsInt | typing.SupportsIndex], bool]:
        ...
    def ratio_callback(self) -> collections.abc.Callable[[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex], None]:
        ...
    def retain_directories(self) -> bool:
        ...
    def set_compression_level(self, level: BitCompressionLevel) -> None:
        ...
    def set_compression_method(self, method: BitCompressionMethod) -> None:
        ...
    def set_dictionary_size(self, dictionary_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def set_file_callback(self, callback: collections.abc.Callable[[str], None]) -> None:
        ...
    def set_overwrite_mode(self, mode: OverwriteMode) -> None:
        ...
    @typing.overload
    def set_password(self, password: str) -> None:
        ...
    @typing.overload
    def set_password(self, password: str, crypt_headers: bool) -> None:
        ...
    @typing.overload
    def set_password(self, password: str, scope: EncryptionScope) -> None:
        ...
    def set_password_callback(self, callback: collections.abc.Callable[[], str]) -> None:
        ...
    def set_progress_callback(self, callback: collections.abc.Callable[[typing.SupportsInt | typing.SupportsIndex], bool]) -> None:
        ...
    def set_ratio_callback(self, callback: collections.abc.Callable[[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex], None]) -> None:
        ...
    def set_retain_directories(self, retain: bool) -> None:
        ...
    def set_solid_mode(self, mode: bool) -> None:
        ...
    def set_store_creation_time(self, store_creation_time: bool) -> None:
        ...
    def set_store_last_access_time(self, store_last_access_time: bool) -> None:
        ...
    def set_store_last_write_time(self, store_last_write_time: bool) -> None:
        ...
    def set_store_open_files(self, store_open_files: bool) -> None:
        ...
    def set_store_symbolic_links(self, store_symlinks: bool) -> None:
        ...
    def set_threads_count(self, threads_count: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def set_total_callback(self, callback: collections.abc.Callable[[typing.SupportsInt | typing.SupportsIndex], None]) -> None:
        ...
    @typing.overload
    def set_update_mode(self, can_update: bool) -> None:
        ...
    @typing.overload
    def set_update_mode(self, mode: UpdateMode) -> None:
        ...
    def set_volume_size(self, volume_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def set_word_size(self, word_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def solid_mode(self) -> bool:
        ...
    def store_creation_time(self) -> bool:
        ...
    def store_last_access_time(self) -> bool:
        ...
    def store_last_write_time(self) -> bool:
        ...
    def store_open_files(self) -> bool:
        ...
    def store_symbolic_links(self) -> bool:
        ...
    def threads_count(self) -> int:
        ...
    def total_callback(self) -> collections.abc.Callable[[typing.SupportsInt | typing.SupportsIndex], None]:
        ...
    def update_mode(self) -> UpdateMode:
        ...
    def volume_size(self) -> int:
        ...
    def word_size(self) -> int:
        ...
class BitFileExtractor:
    def __init__(self, lib: Bit7zLibrary, format: BitInFormat = ...) -> None:
        ...
    def clear_password(self) -> None:
        ...
    @typing.overload
    def extract(self, in_archive: str, out_dir: str, callback: collections.abc.Callable[[BitArchiveItem], str]) -> None:
        ...
    @typing.overload
    def extract(self, in_archive: str, out_dir: str = '') -> None:
        ...
    def extract_if(self, in_archive: str, out_dir: str, callback: collections.abc.Callable[[BitArchiveItem], FilterResult]) -> None:
        ...
    def extract_items(self, in_archive: str, indices: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], out_dir: str = '') -> None:
        ...
    def extract_matching(self, in_archive: str, item_filter: str, out_dir: str = '', policy: FilterPolicy = bit7z_python.FilterPolicy.Include) -> None:
        ...
    def extract_matching_regex(self, in_archive: str, regex: str, out_dir: str = '', policy: FilterPolicy = bit7z_python.FilterPolicy.Include) -> None:
        ...
    def extract_root_folder_content(self, in_archive: str, out_dir: str) -> None:
        ...
    def extraction_format(self) -> BitInFormat:
        ...
    def file_callback(self) -> collections.abc.Callable[[str], None]:
        ...
    def format(self) -> BitInFormat:
        ...
    def is_password_defined(self) -> bool:
        ...
    def library(self) -> Bit7zLibrary:
        ...
    def overwrite_mode(self) -> OverwriteMode:
        ...
    def password(self) -> str:
        ...
    def password_callback(self) -> collections.abc.Callable[[], str]:
        ...
    def progress_callback(self) -> collections.abc.Callable[[typing.SupportsInt | typing.SupportsIndex], bool]:
        ...
    def ratio_callback(self) -> collections.abc.Callable[[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex], None]:
        ...
    def retain_directories(self) -> bool:
        ...
    def set_file_callback(self, callback: collections.abc.Callable[[str], None]) -> None:
        ...
    def set_overwrite_mode(self, mode: OverwriteMode) -> None:
        ...
    def set_password(self, password: str) -> None:
        ...
    def set_password_callback(self, callback: collections.abc.Callable[[], str]) -> None:
        ...
    def set_progress_callback(self, callback: collections.abc.Callable[[typing.SupportsInt | typing.SupportsIndex], bool]) -> None:
        ...
    def set_ratio_callback(self, callback: collections.abc.Callable[[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex], None]) -> None:
        ...
    def set_retain_directories(self, retain: bool) -> None:
        ...
    def set_total_callback(self, callback: collections.abc.Callable[[typing.SupportsInt | typing.SupportsIndex], None]) -> None:
        ...
    def test(self, in_archive: str, indices: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex] = []) -> None:
        ...
    def total_callback(self) -> collections.abc.Callable[[typing.SupportsInt | typing.SupportsIndex], None]:
        ...
class BitInFormat:
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: BitInFormat) -> bool:
        """
        Checks if two BitInFormat objects are equal.
        """
    def __ne__(self, arg0: BitInFormat) -> bool:
        """
        Checks if two BitInFormat objects are not equal.
        """
    def value(self) -> int:
        """
        Returns the ID value of this BitInFormat object.
        """
class BitInOutFormat:
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: BitInFormat) -> bool:
        """
        Checks if two BitOutFormat objects are equal.
        """
    def __ne__(self, arg0: BitInFormat) -> bool:
        """
        Checks if two BitOutFormat objects are not equal.
        """
    def default_method(self) -> BitCompressionMethod:
        """
        Returns the default method used for compressing the archive format.
        """
    def features(self) -> FormatFeatures:
        """
        Returns the bitset of the features supported by the format.
        """
    def has_feature(self, feature: FormatFeatures) -> bool:
        """
        Returns a boolean value indicating whether the format has the given feature.
        """
    def value(self) -> int:
        """
        Returns the ID value of this BitOutFormat object.
        """
class BitPropVariantType(enum.Enum):
    Bool: typing.ClassVar[BitPropVariantType]  # value = <BitPropVariantType.Bool: 1>
    Empty: typing.ClassVar[BitPropVariantType]  # value = <BitPropVariantType.Empty: 0>
    FileTime: typing.ClassVar[BitPropVariantType]  # value = <BitPropVariantType.FileTime: 11>
    Int16: typing.ClassVar[BitPropVariantType]  # value = <BitPropVariantType.Int16: 8>
    Int32: typing.ClassVar[BitPropVariantType]  # value = <BitPropVariantType.Int32: 9>
    Int64: typing.ClassVar[BitPropVariantType]  # value = <BitPropVariantType.Int64: 10>
    Int8: typing.ClassVar[BitPropVariantType]  # value = <BitPropVariantType.Int8: 7>
    String: typing.ClassVar[BitPropVariantType]  # value = <BitPropVariantType.String: 2>
    UInt16: typing.ClassVar[BitPropVariantType]  # value = <BitPropVariantType.UInt16: 4>
    UInt32: typing.ClassVar[BitPropVariantType]  # value = <BitPropVariantType.UInt32: 5>
    UInt64: typing.ClassVar[BitPropVariantType]  # value = <BitPropVariantType.UInt64: 6>
    UInt8: typing.ClassVar[BitPropVariantType]  # value = <BitPropVariantType.UInt8: 3>
class BitProperty(enum.Enum):
    ATime: typing.ClassVar[BitProperty]  # value = <BitProperty.ATime: 11>
    AltStreamsSize: typing.ClassVar[BitProperty]  # value = <BitProperty.AltStreamsSize: 76>
    Attrib: typing.ClassVar[BitProperty]  # value = <BitProperty.Attrib: 9>
    BigEndian: typing.ClassVar[BitProperty]  # value = <BitProperty.BigEndian: 42>
    Bit64: typing.ClassVar[BitProperty]  # value = <BitProperty.Bit64: 41>
    Block: typing.ClassVar[BitProperty]  # value = <BitProperty.Block: 27>
    CRC: typing.ClassVar[BitProperty]  # value = <BitProperty.CRC: 19>
    CTime: typing.ClassVar[BitProperty]  # value = <BitProperty.CTime: 10>
    Characts: typing.ClassVar[BitProperty]  # value = <BitProperty.Characts: 47>
    Checksum: typing.ClassVar[BitProperty]  # value = <BitProperty.Checksum: 46>
    ClusterSize: typing.ClassVar[BitProperty]  # value = <BitProperty.ClusterSize: 58>
    CodePage: typing.ClassVar[BitProperty]  # value = <BitProperty.CodePage: 83>
    Comment: typing.ClassVar[BitProperty]  # value = <BitProperty.Comment: 28>
    Commented: typing.ClassVar[BitProperty]  # value = <BitProperty.Commented: 14>
    CopyLink: typing.ClassVar[BitProperty]  # value = <BitProperty.CopyLink: 95>
    Cpu: typing.ClassVar[BitProperty]  # value = <BitProperty.Cpu: 43>
    CreatorApp: typing.ClassVar[BitProperty]  # value = <BitProperty.CreatorApp: 51>
    DictionarySize: typing.ClassVar[BitProperty]  # value = <BitProperty.DictionarySize: 18>
    EmbeddedStubSize: typing.ClassVar[BitProperty]  # value = <BitProperty.EmbeddedStubSize: 88>
    Encrypted: typing.ClassVar[BitProperty]  # value = <BitProperty.Encrypted: 15>
    Error: typing.ClassVar[BitProperty]  # value = <BitProperty.Error: 55>
    ErrorFlags: typing.ClassVar[BitProperty]  # value = <BitProperty.ErrorFlags: 71>
    ErrorType: typing.ClassVar[BitProperty]  # value = <BitProperty.ErrorType: 69>
    Extension: typing.ClassVar[BitProperty]  # value = <BitProperty.Extension: 5>
    FileSystem: typing.ClassVar[BitProperty]  # value = <BitProperty.FileSystem: 24>
    FreeSpace: typing.ClassVar[BitProperty]  # value = <BitProperty.FreeSpace: 57>
    Group: typing.ClassVar[BitProperty]  # value = <BitProperty.Group: 26>
    HandlerItemIndex: typing.ClassVar[BitProperty]  # value = <BitProperty.HandlerItemIndex: 2>
    HardLink: typing.ClassVar[BitProperty]  # value = <BitProperty.HardLink: 90>
    HeadersSize: typing.ClassVar[BitProperty]  # value = <BitProperty.HeadersSize: 45>
    HostOS: typing.ClassVar[BitProperty]  # value = <BitProperty.HostOS: 23>
    INode: typing.ClassVar[BitProperty]  # value = <BitProperty.INode: 91>
    Id: typing.ClassVar[BitProperty]  # value = <BitProperty.Id: 49>
    IsAltStream: typing.ClassVar[BitProperty]  # value = <BitProperty.IsAltStream: 63>
    IsAnti: typing.ClassVar[BitProperty]  # value = <BitProperty.IsAnti: 21>
    IsAux: typing.ClassVar[BitProperty]  # value = <BitProperty.IsAux: 64>
    IsDeleted: typing.ClassVar[BitProperty]  # value = <BitProperty.IsDeleted: 65>
    IsDir: typing.ClassVar[BitProperty]  # value = <BitProperty.IsDir: 6>
    IsNotArcType: typing.ClassVar[BitProperty]  # value = <BitProperty.IsNotArcType: 84>
    IsTree: typing.ClassVar[BitProperty]  # value = <BitProperty.IsTree: 66>
    IsVolume: typing.ClassVar[BitProperty]  # value = <BitProperty.IsVolume: 35>
    Links: typing.ClassVar[BitProperty]  # value = <BitProperty.Links: 37>
    LocalName: typing.ClassVar[BitProperty]  # value = <BitProperty.LocalName: 60>
    MTime: typing.ClassVar[BitProperty]  # value = <BitProperty.MTime: 12>
    MainSubfile: typing.ClassVar[BitProperty]  # value = <BitProperty.MainSubfile: 1>
    Method: typing.ClassVar[BitProperty]  # value = <BitProperty.Method: 22>
    Name: typing.ClassVar[BitProperty]  # value = <BitProperty.Name: 4>
    NoProperty: typing.ClassVar[BitProperty]  # value = <BitProperty.NoProperty: 0>
    NtReparse: typing.ClassVar[BitProperty]  # value = <BitProperty.NtReparse: 89>
    NtSecure: typing.ClassVar[BitProperty]  # value = <BitProperty.NtSecure: 62>
    NumAltStreams: typing.ClassVar[BitProperty]  # value = <BitProperty.NumAltStreams: 75>
    NumBlocks: typing.ClassVar[BitProperty]  # value = <BitProperty.NumBlocks: 38>
    NumErrors: typing.ClassVar[BitProperty]  # value = <BitProperty.NumErrors: 70>
    NumStreams: typing.ClassVar[BitProperty]  # value = <BitProperty.NumStreams: 74>
    NumSubDirs: typing.ClassVar[BitProperty]  # value = <BitProperty.NumSubDirs: 31>
    NumSubFiles: typing.ClassVar[BitProperty]  # value = <BitProperty.NumSubFiles: 32>
    NumVolumes: typing.ClassVar[BitProperty]  # value = <BitProperty.NumVolumes: 39>
    Offset: typing.ClassVar[BitProperty]  # value = <BitProperty.Offset: 36>
    OutName: typing.ClassVar[BitProperty]  # value = <BitProperty.OutName: 94>
    PackSize: typing.ClassVar[BitProperty]  # value = <BitProperty.PackSize: 8>
    Path: typing.ClassVar[BitProperty]  # value = <BitProperty.Path: 3>
    PhySize: typing.ClassVar[BitProperty]  # value = <BitProperty.PhySize: 44>
    PhySizeCantBeDetected: typing.ClassVar[BitProperty]  # value = <BitProperty.PhySizeCantBeDetected: 85>
    Position: typing.ClassVar[BitProperty]  # value = <BitProperty.Position: 29>
    PosixAttrib: typing.ClassVar[BitProperty]  # value = <BitProperty.PosixAttrib: 53>
    Prefix: typing.ClassVar[BitProperty]  # value = <BitProperty.Prefix: 30>
    Provider: typing.ClassVar[BitProperty]  # value = <BitProperty.Provider: 61>
    ReadOnly: typing.ClassVar[BitProperty]  # value = <BitProperty.ReadOnly: 93>
    SectorSize: typing.ClassVar[BitProperty]  # value = <BitProperty.SectorSize: 52>
    Sha1: typing.ClassVar[BitProperty]  # value = <BitProperty.Sha1: 67>
    Sha256: typing.ClassVar[BitProperty]  # value = <BitProperty.Sha256: 68>
    ShortComment: typing.ClassVar[BitProperty]  # value = <BitProperty.ShortComment: 82>
    ShortName: typing.ClassVar[BitProperty]  # value = <BitProperty.ShortName: 50>
    Size: typing.ClassVar[BitProperty]  # value = <BitProperty.Size: 7>
    Solid: typing.ClassVar[BitProperty]  # value = <BitProperty.Solid: 13>
    SplitAfter: typing.ClassVar[BitProperty]  # value = <BitProperty.SplitAfter: 17>
    SplitBefore: typing.ClassVar[BitProperty]  # value = <BitProperty.SplitBefore: 16>
    StreamId: typing.ClassVar[BitProperty]  # value = <BitProperty.StreamId: 92>
    SubType: typing.ClassVar[BitProperty]  # value = <BitProperty.SubType: 81>
    SymLink: typing.ClassVar[BitProperty]  # value = <BitProperty.SymLink: 54>
    TailSize: typing.ClassVar[BitProperty]  # value = <BitProperty.TailSize: 87>
    TimeType: typing.ClassVar[BitProperty]  # value = <BitProperty.TimeType: 40>
    TotalPhySize: typing.ClassVar[BitProperty]  # value = <BitProperty.TotalPhySize: 79>
    TotalSize: typing.ClassVar[BitProperty]  # value = <BitProperty.TotalSize: 56>
    Type: typing.ClassVar[BitProperty]  # value = <BitProperty.Type: 20>
    UnpackSize: typing.ClassVar[BitProperty]  # value = <BitProperty.UnpackSize: 78>
    UnpackVer: typing.ClassVar[BitProperty]  # value = <BitProperty.UnpackVer: 33>
    User: typing.ClassVar[BitProperty]  # value = <BitProperty.User: 25>
    Va: typing.ClassVar[BitProperty]  # value = <BitProperty.Va: 48>
    VirtualSize: typing.ClassVar[BitProperty]  # value = <BitProperty.VirtualSize: 77>
    Volume: typing.ClassVar[BitProperty]  # value = <BitProperty.Volume: 34>
    VolumeIndex: typing.ClassVar[BitProperty]  # value = <BitProperty.VolumeIndex: 80>
    VolumeName: typing.ClassVar[BitProperty]  # value = <BitProperty.VolumeName: 59>
    Warning: typing.ClassVar[BitProperty]  # value = <BitProperty.Warning: 73>
    WarningFlags: typing.ClassVar[BitProperty]  # value = <BitProperty.WarningFlags: 72>
    ZerosTailIsAllowed: typing.ClassVar[BitProperty]  # value = <BitProperty.ZerosTailIsAllowed: 86>
class DeletePolicy(enum.Enum):
    ItemOnly: typing.ClassVar[DeletePolicy]  # value = <DeletePolicy.ItemOnly: 0>
    RecurseDirs: typing.ClassVar[DeletePolicy]  # value = <DeletePolicy.RecurseDirs: 1>
class EncryptionScope(enum.Enum):
    DataAndHeaders: typing.ClassVar[EncryptionScope]  # value = <EncryptionScope.DataAndHeaders: 1>
    DataOnly: typing.ClassVar[EncryptionScope]  # value = <EncryptionScope.DataOnly: 0>
class FilterPolicy(enum.Enum):
    Exclude: typing.ClassVar[FilterPolicy]  # value = <FilterPolicy.Exclude: 1>
    Include: typing.ClassVar[FilterPolicy]  # value = <FilterPolicy.Include: 0>
class FilterResult(enum.Enum):
    AbortOperation: typing.ClassVar[FilterResult]  # value = <FilterResult.AbortOperation: 2>
    ProcessItem: typing.ClassVar[FilterResult]  # value = <FilterResult.ProcessItem: 0>
    SkipItem: typing.ClassVar[FilterResult]  # value = <FilterResult.SkipItem: 1>
class FolderPathPolicy(enum.Enum):
    KeepName: typing.ClassVar[FolderPathPolicy]  # value = <FolderPathPolicy.KeepName: 1>
    KeepPath: typing.ClassVar[FolderPathPolicy]  # value = <FolderPathPolicy.KeepPath: 2>
    Strip: typing.ClassVar[FolderPathPolicy]  # value = <FolderPathPolicy.Strip: 0>
class FormatFeatures(enum.Enum):
    CompressionLevel: typing.ClassVar[FormatFeatures]  # value = <FormatFeatures.CompressionLevel: 4>
    Encryption: typing.ClassVar[FormatFeatures]  # value = <FormatFeatures.Encryption: 8>
    HeaderEncryption: typing.ClassVar[FormatFeatures]  # value = <FormatFeatures.HeaderEncryption: 16>
    MultipleFiles: typing.ClassVar[FormatFeatures]  # value = <FormatFeatures.MultipleFiles: 1>
    MultipleMethods: typing.ClassVar[FormatFeatures]  # value = <FormatFeatures.MultipleMethods: 32>
    SolidArchive: typing.ClassVar[FormatFeatures]  # value = <FormatFeatures.SolidArchive: 2>
class OverwriteMode(enum.Enum):
    NoneOverwrite: typing.ClassVar[OverwriteMode]  # value = <OverwriteMode.NoneOverwrite: 0>
    Overwrite: typing.ClassVar[OverwriteMode]  # value = <OverwriteMode.Overwrite: 1>
    Skip: typing.ClassVar[OverwriteMode]  # value = <OverwriteMode.Skip: 2>
class SymlinkPolicy(enum.Enum):
    DoNotFollow: typing.ClassVar[SymlinkPolicy]  # value = <SymlinkPolicy.DoNotFollow: 1>
    Follow: typing.ClassVar[SymlinkPolicy]  # value = <SymlinkPolicy.Follow: 0>
class UpdateMode(enum.Enum):
    """
    Warning: value Overwrite is deprecated!
    """
    Append: typing.ClassVar[UpdateMode]  # value = <UpdateMode.Append: 1>
    NoneUpdate: typing.ClassVar[UpdateMode]  # value = <UpdateMode.NoneUpdate: 0>
    Update: typing.ClassVar[UpdateMode]  # value = <UpdateMode.Update: 2>
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
VERSION_INFO: str = '0.1.1'
