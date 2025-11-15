# ESXDOS API

## Introduction

ZX Basic Compiler already comes with an ESXDOS library, and documentation can be found 

This is the ESXDOS API documentation. THE esxDOS API is a set of functions that allow you to interact with the Next's SD card. A number of wrapper functions are provided to make it easier to use, but for reference the raw API is also documented.

## Commands 

| Call Code | Command | Description |
|-----------|---------|-------------|
| `$85` (133) | [disk_filemap](disk_filemap.md) | obtain file allocation map |
| `$86` (134) | [disk_strmstart](disk_strmstart.md) | start streaming operation |
| `$87` (135) | [disk_strmend](disk_strmend.md) | end streaming operation |
| `$88` (136) | [m_dosversion](m_dosversion.md) | get NextZXOS version/mode information |
| `$89` (137) | [m_getsetdrv](m_getsetdrv.md) | get/set default drive |
| `$8b` (139) | [m_tapein](m_tapein.md) | tape redirection control (input) |
| `$8c` (140) | [m_tapeout](m_tapeout.md) | tape redirection control (output) |
| `$8d` (141) | [m_gethandle](m_gethandle.md) | get handle for current dot command |
| `$8e` (142) | [m_getdate](m_getdate.md) | get current date/time |
| `$8f` (143) | [m_execcmd](m_execcmd.md) | execute a dot command |
| `$90` (144) | [m_autoload](m_autoload.md) | load a BASIC program from tape or disk |
| `$91` (145) | [m_setcaps](m_setcaps.md) | set additional capabilities |
| `$92` (146) | [m_drvapi](m_drvapi.md) | access API for installable drivers |
| `$93` (147) | [m_geterr](m_geterr.md) | get or generate error message |
| `$94` (148) | [m_p3dos](m_p3dos.md) | execute +3DOS/IDEDOS/NextZXOS call |
| `$95` (149) | [m_errh](m_errh.md) | register dot command error handler |
| `$9a` (154) | [f_open](f_open.md) | open file |
| `$9b` (155) | [f_close](f_close.md) | close file |
| `$9c` (156) | [f_sync](f_sync.md) | sync file changes to disk |
| `$9d` (157) | [f_read](f_read.md) | read file |
| `$9e` (158) | [f_write](f_write.md) | write file |
| `$9f` (159) | [f_seek](f_seek.md) | set file position |
| `$a0` (160) | [f_fgetpos](f_fgetpos.md) | get file position |
| `$a1` (161) | [f_fstat](f_fstat.md) | get open file information |
| `$a2` (162) | [f_ftruncate](f_ftruncate.md) | truncate/extend open file |
| `$a3` (163) | [f_opendir](f_opendir.md) | open directory for reading |
| `$a4` (164) | [f_readdir](f_readdir.md) | read directory entry |
| `$a5` (165) | [f_telldir](f_telldir.md) | get directory position |
| `$a6` (166) | [f_seekdir](f_seekdir.md) | set directory position |
| `$a7` (167) | [f_rewinddir](f_rewinddir.md) | rewind to start of directory |
| `$a8` (168) | [f_getcwd](f_getcwd.md) | get current working directory |
| `$a9` (169) | [f_chdir](f_chdir.md) | change directory |
| `$aa` (170) | [f_mkdir](f_mkdir.md) | make directory |
| `$ab` (171) | [f_rmdir](f_rmdir.md) | remove directory |
| `$ac` (172) | [f_stat](f_stat.md) | get unopen file information |
| `$ad` (173) | [f_unlink](f_unlink.md) | delete file |
| `$ae` (174) | [f_truncate](f_truncate.md) | truncate/extend unopen file |
| `$af` (175) | [f_chmod](f_chmod.md) | change file attributes |
| `$b0` (176) | [f_rename](f_rename.md) | rename/move file |
| `$b1` (177) | [f_getfree](f_getfree.md) | get free space |


## Error Codes

| Code | Constant | Description |
|------|----------|-------------|
| 0 | `esx_ok` | Unknown error |
| 1 | `esx_eok` | OK |
| 2 | `esx_nonsense` | Nonsense in esxDOS |
| 3 | `esx_estend` | Statement end error |
| 4 | `esx_ewrtype` | Wrong file type |
| 5 | `esx_enoent` | No such file or dir |
| 6 | `esx_eio` | I/O error |
| 7 | `esx_einval` | Invalid filename |
| 8 | `esx_eacces` | Access denied |
| 9 | `esx_enospc` | Drive full |
| 10 | `esx_enxio` | Invalid i/o request |
| 11 | `esx_enodrv` | No such drive |
| 12 | `esx_enfile` | Too many files open |
| 13 | `esx_ebadf` | Bad file number |
| 14 | `esx_enodev` | No such device |
| 15 | `esx_eoverflow` | File pointer overflow |
| 16 | `esx_eisdir` | Is a directory |
| 17 | `esx_enotdir` | Not a directory |
| 18 | `esx_eexist` | Already exists |
| 19 | `esx_epath` | Invalid path |
| 20 | `esx_esys` | Missing system |
| 21 | `esx_enametoolong` | Path too long |
| 22 | `esx_enocmd` | No such command |
| 23 | `esx_einuse` | In use |
| 24 | `esx_erdonly` | Read only |
| 25 | `esx_everify` | Verify failed |
| 26 | `esx_eloadingko` | Sys file load error |
| 27 | `esx_edirinuse` | Directory in use |
| 28 | `esx_emapramactive` | MAPRAM is active |
| 29 | `esx_edrivebusy` | Drive busy |
| 30 | `esx_efsunknown` | Unknown filesystem |
| 31 | `esx_edevicebusy` | Device busy |

Typical usage would involve the following steps:

### Example 1
```
    ' open a file and get the file handle 
    asm 
        ld      a, "$"
        rst     8 
        db      m_getserdrv
        xor     a 
        ld      ix, filename
        ld      b, f_read 
        rst     8 
        db      f_open
    end asm 
    
```

## Description

DESCRIPTION

## Examples

```
EXAMPLE
```


## Remarks

## See also

* [OTHERKEYWORD](OTHERKEYWORD.md)
