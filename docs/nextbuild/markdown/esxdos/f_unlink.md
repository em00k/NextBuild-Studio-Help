# F_UNLINK ($ad)

## Description
Delete file.

## Entry Parameters

| Register | Description |
|----------|-------------|
| `A` | Drive specifier (`'*'`=default, `'$'`=system)<br>(overridden if filespec includes a drive) |
| `IX` | Filespec, null-terminated<br>(`HL` from dot command) |

## Exit Conditions

### Success
- `Fc=0`

### Failure
- `Fc=1`
- `A=error code`

## Notes

> **Important:** This call only deletes the base file, not any associated metadata file.
>
> Use the +3DOS call `DOS_DELETE` to ensure any associated metadata file is also deleted.

## Links

https://gitlab.com/thesmog358/tbblue/-/tree/master/docs/nextzxos

