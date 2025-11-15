# F_SEEK ($9f)

## Description
Seek to position in file.

## Entry Parameters

| Register | Description |
|----------|-------------|
| `A` | File handle |
| `BCDE` | Bytes to seek |
| `IXL` | Seek mode (see table below)<br>(`L` from dot command) |

## Seek Modes

| Mode | Value | Description |
|------|-------|-------------|
| `esx_seek_set` | `$00` | Set the file position to `BCDE` |
| `esx_seek_fwd` | `$01` | Add `BCDE` to the file position |
| `esx_seek_bwd` | `$02` | Subtract `BCDE` from the file position |

## Exit Conditions

### Success
- `Fc=0`
- `BCDE=current position`

### Failure
- `Fc=1`
- `A=error code`

## Notes

> **Important:** Attempts to seek past beginning/end of file leave `BCDE=position=0/filesize` respectively, with no error.

## Links

https://gitlab.com/thesmog358/tbblue/-/tree/master/docs/nextzxos

