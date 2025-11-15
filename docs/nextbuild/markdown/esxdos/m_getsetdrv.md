# M_GETSETDRV ($89)

## Description
Get or set the default drive.

## Entry Parameters

| Register | Description |
|----------|-------------|
| `A` | Operation:<br>`0` = get the default drive<br>`<>0` = set the default drive to `A`<br><br>For setting drive:<br>bits 7..3 = drive letter (0=A...15=P)<br>bits 2..0 = ignored (use 1 to ensure A<>0) |

## Exit Conditions

### Success
- `Fc=0`
- `A=default drive`, encoded as:
  - bits 7..3 = drive letter (0=A...15=P)
  - bits 2..0 = 0

### Failure
- `Fc=1`
- `A=error code`

## Notes

> **Note:** This call isn't often useful, as it is not necessary to provide a specific drive to calls which need a drive/filename.
>
> For such calls, you can instead provide:
> - `A='*'` use the default drive
> - `A='$'` use the system drive (C:, where the NEXTZXOS and BIN dirs are)
> - Any drive provided in such calls is also overridden by any drive letter that is specified in the filename (eg "D:/myfile.txt\0").

> **Note:** When setting a drive, this call only affects the default drive seen by other esxDOS and NextZXOS API calls. It does *not* change the default LOAD/SAVE drives used by NextBASIC, which are stored in the LODDRV and SAVDRV system variables.

## Links

https://gitlab.com/thesmog358/tbblue/-/tree/master/docs/nextzxos

