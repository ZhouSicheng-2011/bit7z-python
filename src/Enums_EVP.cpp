/*
This file binds the enums in bit7z.
Author: ZhouSicheng-2011
Time: 2026-02-23
License: This project is under the Apache-2.0 Lincense, see LICENSE for more details.
*/
#include <API.hpp>
#include <pybind11/native_enum.h>

void init_enums(py::module_& mod){
    /*
    Init the enums of bit7z
    In order to avoid problem, we exported all the enums in bit7z, even some might never be used.
    If some of the enums won't be used, will comment them out in the future.
    */

    //Bind BitCompressionLevel
    py::native_enum<bit7z::BitCompressionLevel>(mod, "BitCompressionLevel", "enum.Enum")
        .value("None", bit7z::BitCompressionLevel::None)
        .value("Fastest", bit7z::BitCompressionLevel::Fastest)
        .value("Fast", bit7z::BitCompressionLevel::Fast)
        .value("Normal", bit7z::BitCompressionLevel::Normal)
        .value("Max", bit7z::BitCompressionLevel::Max)
        .value("Ultra", bit7z::BitCompressionLevel::Ultra)
        .finalize();
    
    //Bind BitCompressionMethod
    py::native_enum<bit7z::BitCompressionMethod>(mod, "BitCompressionMethod", "enum.Enum")
        .value("Deflate", bit7z::BitCompressionMethod::Deflate)
        .value("Deflate64", bit7z::BitCompressionMethod::Deflate64)
        .value("LZMA", bit7z::BitCompressionMethod::Lzma)
        .value("LZMA2", bit7z::BitCompressionMethod::Lzma2)
        .value("PPMD", bit7z::BitCompressionMethod::Ppmd)
        .value("Copy", bit7z::BitCompressionMethod::Copy)
        .value("BZip2", bit7z::BitCompressionMethod::BZip2)
        .finalize();
    
    //Bind BitError
    py::native_enum<bit7z::BitError>(mod, "BitError", "enum.Enum")
        .value("Fail", bit7z::BitError::Fail)
        .value("FilterNotSpecified", bit7z::BitError::FilterNotSpecified)
        .value("FormatFeatureNotSupported", bit7z::BitError::FormatFeatureNotSupported)
        .value("IndicesNotSpecified", bit7z::BitError::IndicesNotSpecified)
        .value("InvalidArchivePath", bit7z::BitError::InvalidArchivePath)
        .value("InvalidOutputBufferSize", bit7z::BitError::InvalidOutputBufferSize)
        .value("InvalidCompressionMethod", bit7z::BitError::InvalidCompressionMethod)
        .value("InvalidDictionarySize", bit7z::BitError::InvalidDictionarySize)
        .value("InvalidIndex", bit7z::BitError::InvalidIndex)
        .value("InvalidWordSize", bit7z::BitError::InvalidWordSize)
        .value("ItemIsAFolder", bit7z::BitError::ItemIsAFolder)
        .value("ItemMarkedAsDeleted", bit7z::BitError::ItemMarkedAsDeleted)
        .value("NoMatchingItems", bit7z::BitError::NoMatchingItems)
        .value("NoMatchingSignature", bit7z::BitError::NoMatchingSignature)
        .value("NonEmptyOutputBuffer", bit7z::BitError::NonEmptyOutputBuffer)
        .value("NullOutputBuffer", bit7z::BitError::NullOutputBuffer)
        .value("RequestedWrongVariantType", bit7z::BitError::RequestedWrongVariantType)
        .value("UnsupportedOperation", bit7z::BitError::UnsupportedOperation)
        .value("UnsupportedVariantType", bit7z::BitError::UnsupportedVariantType)
        .value("WrongUpdateMode", bit7z::BitError::WrongUpdateMode)
        .value("InvalidZipPassword", bit7z::BitError::InvalidZipPassword)
        .finalize();

    //Bind BitFaliureSource
    py::native_enum<bit7z::BitFailureSource>(mod, "BitFailureSource", "enum.Enum")
        .value("CRCError", bit7z::BitFailureSource::CRCError)
        .value("DataAfterEnd", bit7z::BitFailureSource::DataAfterEnd)
        .value("DataError", bit7z::BitFailureSource::DataError)
        .value("InvalidArchive", bit7z::BitFailureSource::InvalidArchive)
        .value("InvalidArgument", bit7z::BitFailureSource::InvalidArgument)
        .value("FormatDetectionError", bit7z::BitFailureSource::FormatDetectionError)
        .value("HeadersError", bit7z::BitFailureSource::HeadersError)
        .value("NoSuchItem", bit7z::BitFailureSource::NoSuchItem)
        .value("OperationNotSupported", bit7z::BitFailureSource::OperationNotSupported)
        .value("OperationNotPermitted", bit7z::BitFailureSource::OperationNotPermitted)
        .value("UnavailableData", bit7z::BitFailureSource::UnavailableData)
        .value("UnexpectedEnd", bit7z::BitFailureSource::UnexpectedEnd)
        .value("WrongPassword", bit7z::BitFailureSource::WrongPassword)
        .finalize();
    
    //Bind BitProperty
    py::native_enum<bit7z::BitProperty>(mod, "BitProperty", "enum.Enum")
        .value("NoProperty", bit7z::BitProperty::NoProperty)
        .value("MainSubfile", bit7z::BitProperty::MainSubfile)
        .value("HandlerItemIndex", bit7z::BitProperty::HandlerItemIndex)
        .value("Path", bit7z::BitProperty::Path)
        .value("Name", bit7z::BitProperty::Name)
        .value("Extension", bit7z::BitProperty::Extension)
        .value("IsDir", bit7z::BitProperty::IsDir)
        .value("Size", bit7z::BitProperty::Size)
        .value("PackSize", bit7z::BitProperty::PackSize)
        .value("Attrib", bit7z::BitProperty::Attrib)
        .value("CTime", bit7z::BitProperty::CTime)
        .value("ATime", bit7z::BitProperty::ATime)
        .value("MTime", bit7z::BitProperty::MTime)
        .value("Solid", bit7z::BitProperty::Solid)
        .value("Commented", bit7z::BitProperty::Commented)
        .value("Encrypted", bit7z::BitProperty::Encrypted)
        .value("SplitBefore", bit7z::BitProperty::SplitBefore)
        .value("SplitAfter", bit7z::BitProperty::SplitAfter)
        .value("DictionarySize", bit7z::BitProperty::DictionarySize)
        .value("CRC", bit7z::BitProperty::CRC)
        .value("Type", bit7z::BitProperty::Type)
        .value("IsAnti", bit7z::BitProperty::IsAnti)
        .value("Method", bit7z::BitProperty::Method)
        .value("HostOS", bit7z::BitProperty::HostOS)
        .value("FileSystem", bit7z::BitProperty::FileSystem)
        .value("User", bit7z::BitProperty::User)
        .value("Group", bit7z::BitProperty::Group)
        .value("Block", bit7z::BitProperty::Block)
        .value("Comment", bit7z::BitProperty::Comment)
        .value("Position", bit7z::BitProperty::Position)
        .value("Prefix", bit7z::BitProperty::Prefix)
        .value("NumSubDirs", bit7z::BitProperty::NumSubDirs)
        .value("NumSubFiles", bit7z::BitProperty::NumSubFiles)
        .value("UnpackVer", bit7z::BitProperty::UnpackVer)
        .value("Volume", bit7z::BitProperty::Volume)
        .value("IsVolume", bit7z::BitProperty::IsVolume)
        .value("Offset", bit7z::BitProperty::Offset)
        .value("Links", bit7z::BitProperty::Links)
        .value("NumBlocks", bit7z::BitProperty::NumBlocks)
        .value("NumVolumes", bit7z::BitProperty::NumVolumes)
        .value("TimeType", bit7z::BitProperty::TimeType)
        .value("Bit64", bit7z::BitProperty::Bit64)
        .value("BigEndian", bit7z::BitProperty::BigEndian)
        .value("Cpu", bit7z::BitProperty::Cpu)
        .value("PhySize", bit7z::BitProperty::PhySize)
        .value("HeadersSize", bit7z::BitProperty::HeadersSize)
        .value("Checksum", bit7z::BitProperty::Checksum)
        .value("Characts", bit7z::BitProperty::Characts)
        .value("Va", bit7z::BitProperty::Va)
        .value("Id", bit7z::BitProperty::Id)
        .value("ShortName", bit7z::BitProperty::ShortName)
        .value("CreatorApp", bit7z::BitProperty::CreatorApp)
        .value("SectorSize", bit7z::BitProperty::SectorSize)
        .value("PosixAttrib", bit7z::BitProperty::PosixAttrib)
        .value("SymLink", bit7z::BitProperty::SymLink)
        .value("Error", bit7z::BitProperty::Error)
        .value("TotalSize", bit7z::BitProperty::TotalSize)
        .value("FreeSpace", bit7z::BitProperty::FreeSpace)
        .value("ClusterSize", bit7z::BitProperty::ClusterSize)
        .value("VolumeName", bit7z::BitProperty::VolumeName)
        .value("LocalName", bit7z::BitProperty::LocalName)
        .value("Provider", bit7z::BitProperty::Provider)
        .value("NtSecure", bit7z::BitProperty::NtSecure)
        .value("IsAltStream", bit7z::BitProperty::IsAltStream)
        .value("IsAux", bit7z::BitProperty::IsAux)
        .value("IsDeleted", bit7z::BitProperty::IsDeleted)
        .value("IsTree", bit7z::BitProperty::IsTree)
        .value("Sha1", bit7z::BitProperty::Sha1)
        .value("Sha256", bit7z::BitProperty::Sha256)
        .value("ErrorType", bit7z::BitProperty::ErrorType)
        .value("NumErrors", bit7z::BitProperty::NumErrors)
        .value("ErrorFlags", bit7z::BitProperty::ErrorFlags)
        .value("WarningFlags", bit7z::BitProperty::WarningFlags)
        .value("Warning", bit7z::BitProperty::Warning)
        .value("NumStreams", bit7z::BitProperty::NumStreams)
        .value("NumAltStreams", bit7z::BitProperty::NumAltStreams)
        .value("AltStreamsSize", bit7z::BitProperty::AltStreamsSize)
        .value("VirtualSize", bit7z::BitProperty::VirtualSize)
        .value("UnpackSize", bit7z::BitProperty::UnpackSize)
        .value("TotalPhySize", bit7z::BitProperty::TotalPhySize)
        .value("VolumeIndex", bit7z::BitProperty::VolumeIndex)
        .value("SubType", bit7z::BitProperty::SubType)
        .value("ShortComment", bit7z::BitProperty::ShortComment)
        .value("CodePage", bit7z::BitProperty::CodePage)
        .value("IsNotArcType", bit7z::BitProperty::IsNotArcType)
        .value("PhySizeCantBeDetected", bit7z::BitProperty::PhySizeCantBeDetected)
        .value("ZerosTailIsAllowed", bit7z::BitProperty::ZerosTailIsAllowed)
        .value("TailSize", bit7z::BitProperty::TailSize)
        .value("EmbeddedStubSize", bit7z::BitProperty::EmbeddedStubSize)
        .value("NtReparse", bit7z::BitProperty::NtReparse)
        .value("HardLink", bit7z::BitProperty::HardLink)
        .value("INode", bit7z::BitProperty::INode)
        .value("Streamld", bit7z::BitProperty::StreamId)
        .value("ReadOnly", bit7z::BitProperty::ReadOnly)
        .value("OutName", bit7z::BitProperty::OutName)
        .value("CopyLink", bit7z::BitProperty::CopyLink)
        .finalize();
    
    //Bind BitPropVariantType
    py::native_enum<bit7z::BitPropVariantType>(mod, "BitPropVariantType", "enum.Enum")
        .value("Empty", bit7z::BitPropVariantType::Empty)
        .value("Bool", bit7z::BitPropVariantType::Bool)
        .value("String", bit7z::BitPropVariantType::String)
        .value("UInt8", bit7z::BitPropVariantType::UInt8)
        .value("UInt16", bit7z::BitPropVariantType::UInt16)
        .value("UInt32", bit7z::BitPropVariantType::UInt32)
        .value("UInt64", bit7z::BitPropVariantType::UInt64)
        .value("Int8", bit7z::BitPropVariantType::Int8)
        .value("Int16", bit7z::BitPropVariantType::Int16)
        .value("Int32", bit7z::BitPropVariantType::Int32)
        .value("Int64", bit7z::BitPropVariantType::Int64)
        .value("FileTime", bit7z::BitPropVariantType::FileTime)
        .finalize();

    //Bind BitFormatFeatures
    py::native_enum<bit7z::FormatFeatures>(mod, "FormatFeature", "enum.Enum")
        .value("MultipleFiles", bit7z::FormatFeatures::MultipleFiles)
        .value("SolidArchive", bit7z::FormatFeatures::SolidArchive)
        .value("CompressionLevel", bit7z::FormatFeatures::CompressionLevel)
        .value("Encryption", bit7z::FormatFeatures::Encryption)
        .value("HeaderEncryption", bit7z::FormatFeatures::HeaderEncryption)
        .value("MultipleMethods", bit7z::FormatFeatures::MultipleMethods)
        .finalize();

    //Bind OverwriteMode
    py::native_enum<bit7z::OverwriteMode>(mod, "OverwriteMode", "enum.Enum")
        .value("None", bit7z::OverwriteMode::None)
        .value("Overwrite", bit7z::OverwriteMode::Overwrite)
        .value("Skip", bit7z::OverwriteMode::Skip)
        .finalize();

    //Bind UpdateMode
    py::native_enum<bit7z::UpdateMode>(mod, "UpdateMode", "enum.Enum")
        .value("None", bit7z::UpdateMode::None)
        .value("Append", bit7z::UpdateMode::Append)
        .value("Update", bit7z::UpdateMode::Update)
        .finalize();

    //Bind FilterPolicy
    py::native_enum<bit7z::FilterPolicy>(mod, "FilterPolicy", "enum.Enum")
        .value("Include", bit7z::FilterPolicy::Include)
        .value("Exclude", bit7z::FilterPolicy::Exclude)
        .finalize();
    
    //Bind ArchiveStartOffset
    py::native_enum<bit7z::ArchiveStartOffset>(mod, "ArchiveStartOffset", "enum.Enum")
        .value("None", bit7z::ArchiveStartOffset::None)
        .value("FileStart", bit7z::ArchiveStartOffset::FileStart)
        .finalize();

    //Bind EncryptionScope
    py::native_enum<bit7z::EncryptionScope>(mod, "EncryptionScope", "enums.Enum")
        .value("DataOnly", bit7z::EncryptionScope::DataOnly)
        .value("DataAndHeaders", bit7z::EncryptionScope::DataAndHeaders)
        .finalize();

    //Bind DeletePolicy
    py::native_enum<bit7z::DeletePolicy>(mod, "DeletePolicy", "enums.Enum")
        .value("ItemOnly", bit7z::DeletePolicy::ItemOnly)
        .value("RecurseDirs", bit7z::DeletePolicy::RecurseDirs)
        .finalize();

    //Bind SymlinkPolicy 
    py::native_enum<bit7z::SymlinkPolicy>(mod, "SymlinkPolicy", "enums.Enum")
        .value("Follow", bit7z::SymlinkPolicy::Follow)
        .value("DoNotFollow", bit7z::SymlinkPolicy::DoNotFollow)
        .finalize();

    //Bind FilterResult
    py::native_enum<bit7z::FilterResult>(mod, "FilterResult", "enums.Enum")
        .value("ProcessItem", bit7z::FilterResult::ProcessItem)
        .value("SkipItem", bit7z::FilterResult::SkipItem)
        .value("AbortOperation", bit7z::FilterResult::AbortOperation)
        .finalize();

}

