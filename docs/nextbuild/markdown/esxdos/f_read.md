# F_READ ($9d)

## Description
Read bytes from file.

## Entry Parameters

| Register | Description |
|----------|-------------|
| `A` | File handle |
| `IX` | Address<br>(`HL` from dot command) |
| `BC` | Bytes to read |

## Exit Conditions

### Success
- `Fc=0`
- `BC=bytes actually read` (also in `DE`)
- `HL=address following bytes read`

### Failure
- `Fc=1`
- `BC=bytes actually read`
- `A=error code`

## Notes

> **Important:** EOF is not an error. Check `BC` to determine if all bytes requested were read.

## Links

https://gitlab.com/thesmog358/tbblue/-/tree/master/docs/nextzxos

