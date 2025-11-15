# F_OPEN ($9a)

## Description
Open a file.

## Entry Parameters

| Register | Description |
|----------|-------------|
| `A` | Drive specifier (`'*'`=default, `'$'`=system)<br>(overridden if filespec includes a drive) |
| `IX` | Filespec, null-terminated<br>(`HL` from dot command) |
| `B` | Access modes (see table below) |
| `DE` | 8-byte buffer with/for +3DOS header data (if specified in mode)<br>(NB: filetype will be set to `$ff` if headerless file was opened) |

## Access Modes (Register B)

### Read/Write Modes
| Mode | Value | Description |
|------|-------|-------------|
| `esx_mode_read` | `$01` | Request read access |
| `esx_mode_write` | `$02` | Request write access |
| `esx_mode_use_header` | `$40` | Read/write +3DOS header |

### File Creation Modes
| Mode | Value | Description |
|------|-------|-------------|
| `esx_mode_open_exist` | `$00` | Only open existing file |
| `esx_mode_open_creat` | `$08` | Open existing or create file |
| `esx_mode_creat_noexist` | `$04` | Create new file, error if exists |
| `esx_mode_creat_trunc` | `$0c` | Create new file, delete existing |

## Exit Conditions

### Success
- `Fc=0`
- `A=file handle`

### Failure
- `Fc=1`
- `A=error code`


### Links 

https://gitlab.com/thesmog358/tbblue/-/tree/master/docs/nextzxos


